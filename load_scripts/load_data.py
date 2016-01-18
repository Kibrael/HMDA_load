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

def load_rows_04_11(cur, conn, data, table, spec, fields):
	count = 0
	with open(data) as f:
		rows = f.readlines()
		for row in rows:
			print "loading row: ",count
			parsed_row =  parse_row(row, spec, fields)
			try:
				write_row_04_11(cur, conn, tuple(parsed_row), table)
				count +=1
			except psycopg2.Error as e:
				print "data load problem: ", e

def load_rows_90_03(cur, conn, data, table, spec, fields):
	count = 0
	with open(data) as f:
		rows = f.readlines()
		for row in rows:
			print "loading row: ",count
			parsed_row =  parse_row(row, spec, fields)
			try:
				write_row_90_03(cur, conn, tuple(parsed_row), table)
				count +=1
			except psycopg2.Error as e:
				print "data load problem: ", e

def parse_row(row, spec, fields):
	delta_parsed = []
	parsed = []
	for key in fields:
		parsed.append(row[spec[key]['start']:spec[key]['stop']])
		#if len(row[spec[key]['start']:spec[key]['stop']]) == 4:
		#	print row[spec[key]['start']:spec[key]['stop']], type(row[spec[key]['start']:spec[key]['stop']]), len(row[spec[key]['start']:spec[key]['stop']])
	for item in parsed:
		item = "'"+ item + "'"
		delta_parsed.append(item)
	return delta_parsed

def write_row_04_11(cur, conn, row, table): #format should hold for 2004 to 2008
	SQL = "INSERT INTO " + table + """ (year, rid, agency, loan_type, loan_purpose, occupancy, amount,
		action, msa, state, county, tract, sex, co_sex, income, purchaser, denial1, denial2, denial3, edit_status, property_type,
		preapproval, ethnicity, co_ethnicity, race1, race2, race3, race4, race5, co_race1, co_race2, co_race3, co_race4, co_race5,
		rate_spread, hoepa, lien, sequence) VALUES ("""
	for value in row:
		SQL = SQL + value +', '
	SQL = SQL[:-2] + ');'
	cur.execute(SQL,)

def write_row_90_03(cur, conn, row, table):
	SQL = "SET CLIENT_ENCODING TO Latin1; INSERT INTO " + table + """ (year, rid, agency, loan_type, loan_purpose, occupancy, amount, action, msa, state, county,
	tract, race, co_race, sex, co_sex, income, purchaser, denial1, denial2, denial3, edit_status, sequence) VALUES ("""

	for value in row:
		SQL = SQL + value + ', '
	SQL = SQL[:-2] + ');'
	#print SQL
	cur.execute(SQL,)

#field list for 2004 to 2011
fields_04_11 = ('year', 'rid', 'agency', 'loan_type', 'loan_purpose', 'occupancy', 'amount', 'action', 'msa', 'state', 'county',
	'tract', 'sex', 'co_sex', 'income', 'purchaser', 'denial1', 'denial2', 'denial3', 'edit_status', 'property_type', 'preapproval',
	'ethnicity', 'co_ethnicity', 'race1', 'race2', 'race3', 'race4', 'race5', 'co_race1', 'co_race2', 'co_race3', 'co_race4', 'co_race5',
	'rate_spread', 'hoepa', 'lien', 'sequence')

#field list for 1990 to 2003
fields_90_03 = ('year', 'rid', 'agency', 'loan_type', 'loan_purpose', 'occupancy', 'amount', 'action', 'msa', 'state', 'county',
	'tract', 'race', 'co_race', 'sex', 'co_sex', 'income', 'purchaser', 'denial1', 'denial2', 'denial3', 'edit_status', 'sequence')

#field list for 2012 to 2014
fields_12_14 = ()

#table and file variables - use config file to pull these from a json object
#convert these to use the input_file.json map
with open('config.json', 'r') as in_years:
	years = json.load(in_years)

with open('input_file.json', 'r') as f:
	hmda_map = json.load(f)

for year in years['load_years']:
	table = hmda_map['hmda'+year]['table']
	data_file = '../dat/HMDA'+year + '.dat'
	spec_file = '../specs/spec_' + year + '.json'

	with open(spec_file) as specification:
		spec = json.load(specification) #load the json file specification

	conn, cur = connect() #connect to the locally hosted DB
	if int(year) < 1990:
		print "invalid year selection"
	elif int(year) >= 1990 and int(year) < 2004:
		load_rows_90_03(cur, conn, data_file, table, spec, fields_90_03) # read the data file and insert rows for the specifid year (use for 1990 to 2003)
	elif int(year) >= 2004 and int(year) < 2012:
		load_rows_04_11(cur, conn, data_file, table, spec, fields_04_11)
	elif int(year) > 2011:
		print "functions not yet available"
	conn.commit() #commits the transaction
cur.close()
conn.close()

