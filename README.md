## HMDA Data Load
This repository contains links to the FFIEC and NARA (National Archives) HMDA data assets and the code to load them into a SQL database (after some minor modification).

## Requirements
- [Python 3.5](https://www.python.org/) or greater
- [Jupyter notebooks](http://jupyter.org/)
- [Psycopg2](https://pypi.python.org/pypi/psycopg2)
- [PostgreSQL](https://www.postgresql.org/)

Jupyter and Psycopg2 can be installed using pip commands that come with Python installations.
For example `pip install psycopg2`

I used verstion 9.4 of Postgres as it supported by PGAdmin3 which I prefer to PGAdmin4.

Jupyter notebooks are used mainly for code testing.

## Using this repository
#### Download Data:
Before running any code, data files must be downloaded. Links to these files can be found in [data_links.md](https://github.com/Kibrael/HMDA_load/blob/master/data_links.md). The FFIEC maintains the most recent 3 years of data on its site. The file formats of these datasets differ from those in the National Archives, requiring separate SQL scripts to load the data.

The links to NARA data are all to ultimate files. These files contain all changes due to resubmission of data by financial institution and are considered closed and authoritiative. Another NARA version of the HMDA data exists, the Final version. Final is not as final as Ultimate as it does not contain a full two years of file resubmissions.

Loan Applicaiton Register (LAR) files are records of applications and loans that were HMDA reportable. These files are large (over 2GB) and must be unzipped once downloaded.

Panel files are datasets of institutions that filed HMDA and include identifiers that can be used to link these institutions to other datasets, such as the National Information Center.

Transmittal Sheet files are datasets of metadata for institutions and the LAR filing submitted by each of those institutions.

### File Renaming
The naming conventions of the files are inconsistent between NARA and FFIEC and renaming them facilitated programmatic loading of the data.

Two naming conventions are used for each dataset (LAR/Panel/TS), one for NARA and one for FFIEC data. These naming conventions are expected by the Python code and deviations will require changes so that table names are set correctly.

LAR naming:
- FFIEC: lar_{year}.csv
- NARAL: lar_ult_{year}.dat

TS naming:
- FFIEC: ts_{year}.txt
- NARA: ts_ult_{year}.dat

Panel naming:
- FFIEC: panel_{year}.tsv
- NARA: panel_ult_{year}.dat

### Data Cleaning
The 2016 Transmittal Sheet file has an extra tab on line 2674. This tab can be removed by loading the data in Excel, finding the empty cell on line 2074 and deleting it and left shifting the remaining data on that row.

### Loading Data
- Set up the directory structure for your data such that LAR, TS, and Panel data are placed in sub-folders. For example base_path/lar/ will contain all LAR data files. The Python code variable "base_path" can then be set to this path.
- Run the Python code (as a Jupyter notebook or a .py script). The code will make a list of files present in each of the three subdirectories (lar/ts/panel) and load each file to a local Postgres instance.





