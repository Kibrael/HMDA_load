#SQL table creation script

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
	except psycopg2.Error as e: #if database connection results in an error print the following
		print "I am unable to connect to the database: ", e
	return conn.cursor(), conn #returns connection and cursor

with open('../specs/spec_2007.json') as spec: #open the json file specification as a dictionary
	spec_2007 = json.load(spec)

ordered_fields = ('year', 'rid', 'agency', 'loan_type', 'loan_purpose', 'occupancy', 'amount', 'action', 'msa', 'state', 'county',
	'tract', 'sex', 'co_sex', 'income', 'purchaser', 'denial1', 'denial2', 'denial3', 'edit_status', 'property_type', 'preapproval',
	'ethnicity', 'co_ethnicity', 'race1', 'race2', 'race3', 'race4', 'race5', 'co_race1', 'co_race2', 'co_race3', 'co_race4', 'co_race5',
	'rate_spread', 'hoepa', 'lien', 'sequence')

table_attributes = []

for field in ordered_fields:
	string = field + ' varchar(' + str(spec_2007[field]['length'])+ '), '
	table_attributes.append(string)

create = '''CREATE TABLE HMDAPub2007 (''' + ' '.join(table_attributes)[:-2] + ') '

cur, conn = connect()

cur.execute(create,)

conn.commit() #commits the transaction

