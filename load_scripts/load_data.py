#2007 load script
#
import psycopg2
import psycopg2.extras
from collections import OrderedDict
import json
import csv
import sys

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

def load_rows(cur,conn, data, table, spec, fields):
	count = 0
	if int(year) >= 1990 and int(year) <=2011:
		with open(data) as f:
			rows = f.readlines()
	elif int(year) >= 2012 and int(year) <=2014:
		rows = csv.reader(open(data))

	for row in rows:
		print "loading row: ",count, year
		parsed_row =  parse_row(row, year, spec, fields)
		try:
			if int(year) < 1990:
				print "invalid year selection"
			elif int(year) >= 1990 and int(year) < 2004:
				write_row_90_03(cur, conn, tuple(parsed_row), table)
			elif int(year) >= 2004 and int(year) < 2012:
				write_row_04_11(cur, conn, tuple(parsed_row), table)
			elif int(year) > 2011 and int(year) < 2015:
				write_row_12_14(cur,conn, tuple(parsed_row), table)
			else:
				print "invalid selection", year
			count +=1
			#if count > 100: #remove this section when done testing
			#	break
		except psycopg2.Error as e:
			print "data load problem: ", e
			sys.exit(0)
	conn.commit() #commits the transaction
	print "transaction commited"

def parse_row(row, year, spec, fields):
	delta_parsed = []
	parsed = []
	if int(year) < 2012:
		for key in fields:
			parsed.append(row[spec[key]['start']:spec[key]['stop']])
		for item in parsed:
			item = "'"+ item + "'" #use a to string command in the append function?
			delta_parsed.append(item)

	elif int(year) > 2011:
		#print len(fields)
		for key in fields:
			parsed.append(row[spec[key]['parse_position']])
		for item in parsed:
			item = "'"+ item + "'" #use a to string command in the append function?
			delta_parsed.append(item)
	return delta_parsed

def write_row_90_03(cur, conn, row, table):
	SQL = "SET CLIENT_ENCODING TO Latin1; INSERT INTO " + table + """ (year, rid, agency, loan_type, loan_purpose, occupancy, amount, action, msa, state, county,
	tract, race, co_race, sex, co_sex, income, purchaser, denial1, denial2, denial3, edit_status, sequence) VALUES ("""
	#print row
	for value in row:
		SQL = SQL + value + ', '
	SQL = SQL[:-2] + ');'
	cur.execute(SQL,)

def write_row_04_11(cur, conn, row, table): #format should hold for 2004 to 2011
	SQL = "INSERT INTO " + table + """ (year, rid, agency, loan_type, loan_purpose, occupancy, amount,
		action, msa, state, county, tract, sex, co_sex, income, purchaser, denial1, denial2, denial3, edit_status, property_type,
		preapproval, ethnicity, co_ethnicity, race1, race2, race3, race4, race5, co_race1, co_race2, co_race3, co_race4, co_race5,
		rate_spread, hoepa, lien, sequence) VALUES ("""
	for value in row:
		SQL = SQL + value +', '
	SQL = SQL[:-2] + ');'
	cur.execute(SQL,)

def write_row_12_14(cur, conn, row, table): #format for 2012 through 2017
	SQL = "INSERT INTO " + table + """(year, rid, agency, loan_type, property_type, loan_purpose, occupancy, preapproval, amount, action, msa, state, county,
	tract, ethnicity, co_ethnicity, race1, race2, race3, race4, race5, co_race1, co_race2, co_race3, co_race4, co_race5,
	sex, co_sex, income, purchaser, denial1, denial2, denial3, rate_spread, hoepa, lien, edit_status, sequence, population,
	min_population_pct, median_income, tract_to_msa_income_pct, num_owner_occ_units, num_single_fam_units, app_date_ind) VALUES ("""
	for value in row:
		SQL = SQL + value +', '
	SQL = SQL[:-2] + ');'
	cur.execute(SQL,)




#field list for 1990 to 2003
fields_90_03 = ('year', 'rid', 'agency', 'loan_type', 'loan_purpose', 'occupancy', 'amount', 'action', 'msa', 'state', 'county',
	'tract', 'race', 'co_race', 'sex', 'co_sex', 'income', 'purchaser', 'denial1', 'denial2', 'denial3', 'edit_status', 'sequence')
#field list for 2004 to 2011
fields_04_11 = ('year', 'rid', 'agency', 'loan_type', 'loan_purpose', 'occupancy', 'amount', 'action', 'msa', 'state', 'county',
	'tract', 'sex', 'co_sex', 'income', 'purchaser', 'denial1', 'denial2', 'denial3', 'edit_status', 'property_type', 'preapproval',
	'ethnicity', 'co_ethnicity', 'race1', 'race2', 'race3', 'race4', 'race5', 'co_race1', 'co_race2', 'co_race3', 'co_race4', 'co_race5',
	'rate_spread', 'hoepa', 'lien', 'sequence')
#field list for 2012 to 2014
fields_12_14 = ('year', 'rid', 'agency', 'loan_type', 'property_type', 'loan_purpose', 'occupancy', 'preapproval', 'amount', 'action', 'msa', 'state', 'county',
	'tract', 'ethnicity', 'co_ethnicity', 'race1', 'race2', 'race3', 'race4', 'race5', 'co_race1', 'co_race2', 'co_race3', 'co_race4', 'co_race5',
	'sex', 'co_sex', 'income', 'purchaser', 'denial1', 'denial2', 'denial3', 'rate_spread', 'hoepa', 'lien', 'edit_status', 'sequence', 'population',
	'min_population_pct', 'median_income', 'tract_to_msa_income_pct', 'num_owner_occ_units', 'num_single_fam_units', 'app_date_ind')

# fields_12_14 = fields_04_11
#table and file variables - use config file to pull these from a json object
#convert these to use the input_file.json map
with open('config.json', 'r') as in_years:
	years = json.load(in_years)

with open('input_file.json', 'r') as parse_spec:
	hmda_map = json.load(parse_spec)

for year in years['load_years']:
	table = hmda_map['hmda'+year]['table']
	data_file =  hmda_map['hmda' +year]['data']
	spec_file = hmda_map['hmda'+year]['spec']

	with open(spec_file) as specification:
		spec = json.load(specification) #load the json file specification

	print
	print
	print int(year)

	if int(year) >= 1990 and int(year) <= 2003:
		fields = fields_90_03
	elif int(year) >= 2004 and int(year) <= 2011:
		fields = fields_04_11
	elif int(year) >= 2012 and int(year) <= 2014:
		fields = fields_12_14
	else:
		print "invalid selection", year

	conn, cur = connect() #connect to the locally hosted DB
	load_rows(cur,conn, data_file, table, spec, fields)

cur.close()
conn.close()

