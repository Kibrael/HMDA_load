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

def create_table(spec, table_name, fields): #spec name must include folder path
#this module should work for 2004-2008 LAR data
	with open(spec) as spec:
		file_spec = json.load(spec)

	table_attributes = []
	for field in fields:
		string = field + ' varchar(' + str(file_spec[field]['length'])+ '), '
		table_attributes.append(string)

	create = 'DROP TABLE IF EXISTS ' + table_name + '; commit; CREATE TABLE ' + table_name + '(' + ' '.join(table_attributes)[:-2] + ') '
	cur, conn = connect() #create cursor and connection objects

	try:
		cur.execute(create,)
		conn.commit() #commits the transaction
		print "transaction successful"
	except psycopg2.Error as e:
		print 'error: ', e
	cur.close()
	conn.close()

ordered_fields_04_11 = ('year', 'rid', 'agency', 'loan_type', 'loan_purpose', 'occupancy', 'amount', 'action', 'msa', 'state', 'county',
		'tract', 'sex', 'co_sex', 'income', 'purchaser', 'denial1', 'denial2', 'denial3', 'edit_status', 'property_type', 'preapproval',
		'ethnicity', 'co_ethnicity', 'race1', 'race2', 'race3', 'race4', 'race5', 'co_race1', 'co_race2', 'co_race3', 'co_race4', 'co_race5',
		'rate_spread', 'hoepa', 'lien', 'sequence')

ordered_fields_90_03 =  ('year', 'rid', 'agency', 'loan_type', 'loan_purpose', 'occupancy', 'amount', 'action', 'msa', 'state', 'county',
	'tract', 'race', 'co_race', 'sex', 'co_sex', 'income', 'purchaser', 'denial1', 'denial2', 'denial3', 'edit_status', 'sequence')

#function calls
years_90_03 = [str(x+1990) for x in range(0,14)]
years_04_11 = [str(x+2004) for x in range(0,8)]

path = '../specs/'
for year in years_04_11:
	spec_name = path + 'spec_' + year+ '.json'
	table_name = 'HMDAPub'+year
	#create_table(spec_name, table_name, ordered_fields_04_11) #remove comment to run

for year in years_90_03:
	spec_name = path + 'spec_' + year + '.json'
	table_name = 'HMDAPub' + year
	#create_table(spec_name, table_name, ordered_fields_90_03) #remove comment to run




