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

ordered_fields_90_03 =  ('year', 'rid', 'agency', 'loan_type', 'loan_purpose', 'occupancy', 'amount', 'action', 'msa', 'state', 'county',
	'tract', 'race', 'co_race', 'sex', 'co_sex', 'income', 'purchaser', 'denial1', 'denial2', 'denial3', 'edit_status', 'sequence')

ordered_fields_04_11 = ('year', 'rid', 'agency', 'loan_type', 'loan_purpose', 'occupancy', 'amount', 'action', 'msa', 'state', 'county',
		'tract', 'sex', 'co_sex', 'income', 'purchaser', 'denial1', 'denial2', 'denial3', 'edit_status', 'property_type', 'preapproval',
		'ethnicity', 'co_ethnicity', 'race1', 'race2', 'race3', 'race4', 'race5', 'co_race1', 'co_race2', 'co_race3', 'co_race4', 'co_race5',
		'rate_spread', 'hoepa', 'lien', 'sequence')

ordered_fields_12_16 =  ('year', 'rid', 'agency', 'loan_type', 'property_type', 'loan_purpose', 'occupancy', 'preapproval', 'amount', 'action', 'msa', 'state', 'county',
	'tract', 'ethnicity', 'co_ethnicity', 'race1', 'race2', 'race3', 'race4', 'race5', 'co_race1', 'co_race2', 'co_race3', 'co_race4', 'co_race5',
	'sex', 'co_sex', 'income', 'purchaser', 'denial1', 'denial2', 'denial3', 'rate_spread', 'hoepa', 'lien', 'edit_status', 'sequence', 'population',
	'min_population_pct', 'median_income', 'tract_to_msa_income_pct', 'num_owner_occ_units', 'num_single_fam_units', 'app_date_ind')

#ordered_fields_12_14 = ordered_fields_04_11
with open('config.json', 'r') as years_file:
	years = json.load(years_file)

years_90_03 = []
years_04_11 = []
years_12_16 = []
path = '../specs/' #relative folder path to json file specs for parsing

#build list of years for creating tables
for year in years['load_years']:
	if int(year) >= 1990 and int(year) <= 2003:
		years_90_03.append(year)
	elif int(year) >= 2004 and int(year) <= 2011:
		years_04_11.append(year)
	elif int(year) >= 2012 and int(year) <= 2016:
		years_12_16.append(year)
	else:
		print "Invalid year selected"

with open('input_file.json', 'r') as f:
	inputs = json.load(f)

for year in years_90_03:
	spec_name = path + 'spec_' + year + '.json'
	table_name = inputs['hmda' + year]['table']
	create_table(spec_name, table_name, ordered_fields_90_03) #remove comment to run

for year in years_04_11:
	spec_name = path + 'spec_' + year+ '.json'
	table_name = inputs['hmda' + year]['table']
	create_table(spec_name, table_name, ordered_fields_04_11) #remove comment to run

for year in years_12_16:
	spec_name = path + 'spec_' + year + '.json'
	table_name =  inputs['hmda' + year]['table']
	create_table(spec_name, table_name, ordered_fields_12_16) #remove comment to run


