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


ordered_fields = ('year', 'rid', 'agency', 'loan_type', 'loan_purpose', 'occupancy', 'amount', 'action', 'msa', 'state', 'county',
	'tract', 'sex', 'co_sex', 'income', 'purchaser', 'denial1', 'denial2', 'denial3', 'edit_status', 'property_type', 'preapproval',
	'ethnicity', 'co_ethnicity', 'race1', 'race2', 'race3', 'race4', 'race5', 'co_race1', 'co_race2', 'co_race3', 'co_race4', 'co_race5',
	'rate_spread', 'hoepa', 'lien', 'sequence')
text_fields = ()
def read_row(cur, conn, data):
	count = 0

	with open(data) as f:
		rows = f.readlines()
		for row in rows[:10]: #limited to 10 rows for testing
			parsed_row =  parse_row(row, spec_2007)
			write_row(cur, conn, tuple(parsed_row), 'hmdapub2007')

def parse_row(row, spec):
	parsed = []
	for key in ordered_fields:
		#print key, row[spec[key]['start']:spec[key]['stop']],
		parsed.append(row[spec[key]['start']:spec[key]['stop']])
		for x in range(0, len(parsed)):
			if parsed[x] == ' ':
				parsed[x] = 'NULL'
	return parsed

def write_row(cur, conn, row, table):
	SQL = cur.mogrify("""INSERT INTO HMDAPUB2007  (year, rid, agency, loan_type, loan_purpose, occupancy, amount,
		action, msa, state, county, tract, sex, co_sex, income, purchaser, denial1, denial2, denial3, edit_status, property_type,
		preapproval, ethnicity, co_ethnicity, race1, race2, race3, race4, race5, co_race1, co_race2, co_race3, co_race4, co_race5,
		rate_spread, hoepa, lien, sequence) VALUES """)+"%%s;" #% (row)
	print SQL
	cur.execute(SQL, row)
	#cur.execute(SQL,)
data_file = '../dat/lars.ultimate.2007.dat'
with open('../specs/spec_2007.json') as spec:
	spec_2007 = json.load(spec)


conn, cur = connect()
read_row(cur, conn, data_file)
conn.commit()
#write_row(cur, conn, read_row(data_file), 'hmdapub2007')

