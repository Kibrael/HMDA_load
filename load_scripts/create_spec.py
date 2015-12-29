#Creates a JSON output of the 2007 HMDA LAR file specification

from collections import OrderedDict
import json

field_list = OrderedDict({})
end_points = {'start': 0, 'stop': 0}

master_list ={'year': 4, 'rid': 10, 'agency':1, 'loan_type':1, 'loan_purpose':1, 'occupancy':1, 'amount':5, 'action':1,
	'msa':5, 'state':2, 'county':3, 'tract':7, 'sex':1, 'co_sex':1, 'income':4, 'purchaser' :1, 'denial1' :1,
	'denial2':1, 'denial3':1, 'edit_status':1, 'property_type':1, 'preapproval':1, 'ethnicity':1, 'co_ethnicity':1,
	'race1':1, 'race2':1, 'race3':1, 'race4':1, 'race5':1, 'co_race1':1, 'co_race2':1, 'co_race3':1, 'co_race4':1, 'co_race5':1,
	'rate_spread':5, 'HOEPA':1, 'lien':1, 'sequence':7}

fields = ('year', 'rid', 'agency', 'loan_type', 'loan_purpose', 'occupancy', 'amount', 'action', 'msa', 'state', 'county',
	'tract', 'sex', 'co_sex', 'income', 'purchaser', 'denial1', 'denial2', 'denial3', 'edit_status', 'property_type', 'preapproval',
	'ethnicity', 'co_ethnicity', 'race1', 'race2', 'race3', 'race4', 'race5', 'co_race1', 'co_race2', 'co_race3', 'co_race4', 'co_race5',
	'rate_spread', 'hoepa', 'lien', 'sequence')

lengths = (4,10,1,1,1,1,5,1,5,2,3,7,1,1,4,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,1,7)

for field in fields:
	field_list[field] = {}
position = 0
for x in range(0,len(fields)):
	field_list[fields[x]]['start'] = position
	field_list[fields[x]]['stop'] = lengths[x] + position
	field_list[fields[x]]['length'] = field_list[fields[x]]['stop']  - field_list[fields[x]]['start']
	position += lengths[x]

with open('../specs/spec_2007.json', 'w') as outfile: #writes the JSON structure to a file for the path named by report's header structure
	json.dump(field_list, outfile, indent=4, ensure_ascii = False)