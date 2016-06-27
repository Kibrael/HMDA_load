# HMDA_load
Contains file specifications and load scripts for HMDA data. The scripts will load HMDA LAR data from 1990 to 2014 into a local PostgreSQL instance.

Specifications will be converted from FFIEC/FRB PDF to JSON format using [create_spec.py](https://github.com/Kibrael/HMDA_load/blob/master/load_scripts/create_spec.py)
JSON specification files are located [here](https://github.com/Kibrael/HMDA_load/tree/master/specs)

#### Order of Operations:

1) in the [config.json](https://github.com/Kibrael/HMDA_load/blob/master/load_scripts/config.json) file, specify which years of HMDA data are to be loaded. Years are to be in string format.
2) In [input_file.json]() specify the location of the data downloaded from the [national archives](https://catalog.archives.gov/id/2456161?q=2456161). The specs files will be created and loaded into the proper relative folder structure.
3) Run [create_spec.py](https://github.com/Kibrael/HMDA_load/blob/master/load_scripts/create_spec.py) to create a set of JSON files containing the HMDA file specifications
4) Run [create_tables.py](https://github.com/Kibrael/HMDA_load/blob/master/load_scripts/create_table.py) to create the PostgreSQL tables to hold the HMDA LAR data
5) Run [load_data.py](https://github.com/Kibrael/HMDA_load/blob/master/load_scripts/load_data.py) to load the HMDA LAR data into the PostgreSQL tables, this process can take multiple hours per table, especially for 2007 which has ~42 million rows

## Known Issues:
The file spec for 2013 and 2014 is not parsing correctly, resulting in two field names being swapped
1990 and 1991 data have invalid characters causing them not to parse and load
[file_test.py](https://github.com/Kibrael/HMDA_load/blob/master/load_scripts/file_test.py) is used to isolate the bad characters in the LAR files


