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

The links to NARA data are all to ultimate files. These files contain all changes due to resubmission of data by financial institution and are considered closed and authoritiative.

Loan Applicaiton Register (LAR) files are records of applications and loans that were HMDA reportable. These files are large (over 2GB) and must be unzipped once downloaded.

Panel files are datasets of institutions that filed HMDA and include identifiers that can be used to link these institutions to other datasets, such as the National Information Center.

Transmittal Sheet files are datasets of metadata for institutions and the LAR filing submitted by each of those institutions.

### File Renaming
The naming conventions of the files are inconsistent between NARA and FFIEC and renaming them facilitated programmatic loading of the data.

Two naming conventions are used for each dataset (LAR/Panel/TS), one for NARA and one for FFIEC data.



