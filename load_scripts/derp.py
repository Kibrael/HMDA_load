import json

with open('input_file.json', 'r') as f:
	map_dict = json.load(f)

print map_dict['hmda1991']