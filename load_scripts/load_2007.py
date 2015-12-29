#2007 load script
#
import psycopg2
import psycopg2.extras
from collections import OrderedDict
import json

def connect():
	#parameter format for local use
	params = {
	'dbname':'hmdamaster',
	'user':'roellk',
	'password':'',
	'host':'localhost',}
	try:
		conn = psycopg2.connect(**params)
		print "i'm connected"
	except psycopg2.Error as e: #if database connection results in an error print the following
		print "I am unable to connect to the database: ", e
	return  conn, conn.cursor()#(cursor_factory=psycopg2.extras.DictCursor) #return a dictionary cursor object

def load_rows(cur, conn, data, table):
	count = 0
	with open(data) as f:
		rows = f.readlines()
		for row in rows: #limited to 10 rows for testing
			print "loading row: ",count
			parsed_row =  parse_row(row, spec_2007)
			write_row(cur, conn, tuple(parsed_row), table)
			count +=1

def parse_row(row, spec):
	delta_parsed = []
	parsed = []
	for key in ordered_fields:
		parsed.append(row[spec[key]['start']:spec[key]['stop']])
	for item in parsed:
		item = "'"+ item + "'"
		delta_parsed.append(item)
	return delta_parsed

def write_row(cur, conn, row, table): #format should hold for 2004 to 2008
	SQL = "INSERT INTO " + table + """(year, rid, agency, loan_type, loan_purpose, occupancy, amount,
		action, msa, state, county, tract, sex, co_sex, income, purchaser, denial1, denial2, denial3, edit_status, property_type,
		preapproval, ethnicity, co_ethnicity, race1, race2, race3, race4, race5, co_race1, co_race2, co_race3, co_race4, co_race5,
		rate_spread, hoepa, lien, sequence) VALUES ("""
	for value in row:
		SQL = SQL + value +', '
	SQL = SQL[:-2] + ');'
	cur.execute(SQL,)

#2007 field list, should hold for 2004 to 2008
ordered_fields = ('year', 'rid', 'agency', 'loan_type', 'loan_purpose', 'occupancy', 'amount', 'action', 'msa', 'state', 'county',
	'tract', 'sex', 'co_sex', 'income', 'purchaser', 'denial1', 'denial2', 'denial3', 'edit_status', 'property_type', 'preapproval',
	'ethnicity', 'co_ethnicity', 'race1', 'race2', 'race3', 'race4', 'race5', 'co_race1', 'co_race2', 'co_race3', 'co_race4', 'co_race5',
	'rate_spread', 'hoepa', 'lien', 'sequence')

data_file = '../dat/HMDA2007.dat'
with open('../specs/spec_2007.json') as spec:
	spec_2007 = json.load(spec) #load the json file specification

table = "HMDAPUB2007"
conn, cur = connect() #connect to the locally hosted DB
load_rows(cur, conn, data_file, table) #read the data file and insert rows
conn.commit() #commits the transaction


