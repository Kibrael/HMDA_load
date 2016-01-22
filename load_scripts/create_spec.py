#Creates a JSON output of the 2007 HMDA LAR file specification

from collections import OrderedDict
import json

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

#write file specs for 1990 to 2003
write_spec('../specs/spec_1990.json', build_json(fields_90_03, lengths_90_03))
write_spec('../specs/spec_1991.json', build_json(fields_90_03, lengths_90_03))
write_spec('../specs/spec_1992.json', build_json(fields_90_03, lengths_90_03))
write_spec('../specs/spec_1993.json', build_json(fields_90_03, lengths_90_03))
write_spec('../specs/spec_1994.json', build_json(fields_90_03, lengths_90_03))
write_spec('../specs/spec_1995.json', build_json(fields_90_03, lengths_90_03))
write_spec('../specs/spec_1996.json', build_json(fields_90_03, lengths_90_03))
write_spec('../specs/spec_1997.json', build_json(fields_90_03, lengths_90_03))
write_spec('../specs/spec_1998.json', build_json(fields_90_03, lengths_90_03))
write_spec('../specs/spec_1999.json', build_json(fields_90_03, lengths_90_03))
write_spec('../specs/spec_1990.json', build_json(fields_90_03, lengths_90_03))
write_spec('../specs/spec_2000.json', build_json(fields_90_03, lengths_90_03))
write_spec('../specs/spec_2001.json', build_json(fields_90_03, lengths_90_03))
write_spec('../specs/spec_2002.json', build_json(fields_90_03, lengths_90_03))
write_spec('../specs/spec_2003.json', build_json(fields_90_03, lengths_90_03))

#write file specs for 2004 to 2011
write_spec('../specs/spec_2004.json', build_json(fields_04_11, lengths_04_11))
write_spec('../specs/spec_2005.json', build_json(fields_04_11, lengths_04_11))
write_spec('../specs/spec_2006.json', build_json(fields_04_11, lengths_04_11))
write_spec('../specs/spec_2007.json', build_json(fields_04_11, lengths_04_11))
write_spec('../specs/spec_2008.json', build_json(fields_04_11, lengths_04_11))
write_spec('../specs/spec_2009.json', build_json(fields_04_11, lengths_04_11))
write_spec('../specs/spec_2010.json', build_json(fields_04_11, lengths_04_11))
write_spec('../specs/spec_2011.json', build_json(fields_04_11, lengths_04_11))

#write file specs for 2011 to 2014
write_spec('../specs/spec_2012.json', build_json(fields_12_14, lengths_12_14))
write_spec('../specs/spec_2013.json', build_json(fields_12_14, lengths_12_14))
write_spec('../specs/spec_2014.json', build_json(fields_12_14, lengths_12_14))
