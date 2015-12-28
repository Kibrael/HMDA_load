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
	return conn.cursor(cursor_factory=psycopg2.extras.DictCursor) #return a dictionary cursor object


ordered_fields = ('year', 'rid', 'agency', 'loan_type', 'loan_purpose', 'occupancy', 'amount', 'action', 'msa', 'state', 'county',
	'tract', 'sex', 'co-sex', 'income', 'purchaser', 'denial1', 'denial2', 'denail3', 'edit_status', 'property_type', 'preapprova',
	'ethnicity', 'co-ethnicity', 'race1', 'race2', 'race3', 'race4', 'race5', 'co-race1', 'co-race2', 'co-race3', 'co-race4', 'co-race5',
	'rate_spread', 'hoepa', 'lien', 'sequence')

def read_row(data):
	count = 0

	with open(data) as f:
		rows = f.readlines()

		for row in rows[:10]: #limited to 10 rows for testing
			parse_row(row, spec_2007)
			print


def parse_row(row, spec):
	#print row
	for key in ordered_fields:
		#print key,
		print key, row[spec[key]['start']:spec[key]['stop']],

def write_row(row):
	pass


data_file = '../dat/lars.ultimate.2007.dat'
with open('../specs/spec_2007.json') as spec:
	spec_2007 = json.load(spec)


read_row(data_file)

