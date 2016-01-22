#Creates a JSON output for the selected years of the HMDA LAR file specification
from collections import OrderedDict
import json
#write the file spec to a json file that includes field name, length, and start/stop positions
def write_spec(name, data):
	with open(name, 'w') as outfile: #writes the JSON structure to a file for the path named by report's header structure
		json.dump(data, outfile, indent=4, ensure_ascii = False)

#build the file spec as a dictionary that includes field names, length, and start/stop positions
def build_json(fields, lengths):
	for field in fields:
		field_list[field] = {}
	position = 0
	for x in range(0,len(fields)):
		field_list[fields[x]]['start'] = position
		field_list[fields[x]]['stop'] = lengths[x] + position
		field_list[fields[x]]['length'] = field_list[fields[x]]['stop']  - field_list[fields[x]]['start']
		position += lengths[x]
	return field_list

#setup for building the JSON object
field_list = OrderedDict({})
end_points = {'start': 0, 'stop': 0}

#lists of fields from FFIEC data specifications at the national archive
fields_90_03 = ('year', 'rid', 'agency', 'loan_type', 'loan_purpose', 'occupancy', 'amount', 'action', 'msa', 'state', 'county',
	'tract', 'race', 'co_race', 'sex', 'co_sex', 'income', 'purchaser', 'denial1', 'denial2', 'denial3', 'edit_status', 'sequence')

fields_04_11 = ('year', 'rid', 'agency', 'loan_type', 'loan_purpose', 'occupancy', 'amount', 'action', 'msa', 'state', 'county',
	'tract', 'sex', 'co_sex', 'income', 'purchaser', 'denial1', 'denial2', 'denial3', 'edit_status', 'property_type', 'preapproval',
	'ethnicity', 'co_ethnicity', 'race1', 'race2', 'race3', 'race4', 'race5', 'co_race1', 'co_race2', 'co_race3', 'co_race4', 'co_race5',
	'rate_spread', 'hoepa', 'lien', 'sequence')

fields_12_14 = ('year', 'rid', 'agency', 'loan_type', 'property_type', 'loan_purpose', 'occupancy', 'preapproval', 'amount', 'action', 'msa', 'state', 'county',
	'tract', 'ethnicity', 'co_ethnicity', 'race1', 'race2', 'race3', 'race4', 'race5', 'co_race1', 'co_race2', 'co_race3', 'co_race4', 'co_race5',
	'sex', 'co_sex', 'income', 'purchaser', 'denial1', 'denial2', 'denial3', 'rate_spread', 'hoepa', 'lien', 'edit_status', 'sequence', 'population',
	'min_population_pct', 'median_income', 'tract_to_msa_income_pct', 'num_owner_occ_units', 'num_single_fam_units', 'app_date_ind')

#lengths of fields from FFIEC data specifications national archive
lengths_90_03 = (4,10,1,1,1,1,5,1,4,2,3,7,1,1,1,1,4,1,1,1,1,1,7)
lengths_04_11 = (4,10,1,1,1,1,5,1,5,2,3,7,1,1,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1,7)
lengths_12_14 = (4,10,1,1,1,1,1,5,1,1,5,2,3,7,1,1,1,1,1,1,1,1,1,1,1,1,1,1,4,1,1,1,1,5,1,1,1,7,8,6,8,6,8,8,1)


with open('config.json', 'r') as years_file:
	years = json.load(years_file)

years_90_03 = []
years_04_11 = []
years_12_14 = []
path = '../specs/' #relative folder path to json file specs for parsing

#build list of years for creating tables
for year in years['load_years']:
	if int(year) >= 1990 and int(year) <= 2003:
		years_90_03.append(year)
	elif int(year) >= 2004 and int(year) <= 2011:
		years_04_11.append(year)
	elif int(year) >= 2012 and int(year) <= 2014:
		years_12_14.append(year)
	else:
		print "Invalid year selected"

#write file specs for 1990 to 2003
for year in years_90_03:
	write_spec('../specs/spec_' + year + '.json', build_json(fields_90_03, lengths_90_03))

#write file specs for 2004 to 2011
for year in years_04_11:
	write_spec('../specs/spec_' + year + '.json', build_json(fields_04_11, lengths_04_11))

#write file specs for 2011 to 2014
for year in years_12_14:
	write_spec('../specs/spec_' + year + '.json', build_json(fields_12_14, lengths_12_14))
