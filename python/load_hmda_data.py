
# coding: utf-8

# In[ ]:


#This workbook contains code used to load FFIEC and National Archives HMDA data
#HMDA data has 3 files per year, the Transmittal Sheet (sometimes known as Institutions Record Data), 
#the Panel, and Loan Application Register.

#The TS contains information about the institutions that submitted data and some metadata about their associated LAR
#file.

#The Panel contains information used to group financial institutions as well as identifiers that can link HMDA assets
# to other datasets such as those provided by the National Information Center (NIC).

#The Loan Application Register (LAR) file contains the loan records submitted by each institution.

#National Archives (NARA) files have different formats than those published on the FFIEC website. The TS in NARA are 
# a different schema than the Institutions Records published by the FFIEC.
#Data Notes:
#FFIEC TS 2016 contains an extra tab on one line that must be removed before the data will load
#Latin1 required instead of utf8 for several datasets



# In[2]:


from collections import OrderedDict
import json
from os import listdir
from os.path import isfile, join
import psycopg2


# In[3]:


with open("../../pg_pw.txt", 'r') as pw_file:
    pw = pw_file.readline()

params = {
    'dbname':'postgres',
    'user':'postgres',
    'password':pw,
    'host':'localhost'}

def connect(params=params):
    """Creates a connection to a local PG database."""
    #parameter format for local use
 
    try:
        conn = psycopg2.connect(**params)
        print("Connected")
        return conn.cursor(), conn #returns connection and cursor
    except psycopg2.Error as e: #if database connection results in an error print the following
        print("I am unable to connect to the database: ", e)
    


# In[4]:



#build lists of data files for loading into db
base_path = "/HMDA_Data/"
ts_data_path = base_path + "ts/"
ts_files = [f for f in listdir(ts_data_path) if isfile(join(ts_data_path, f))]
ts_files = [f for f in ts_files if f!=".DS_Store"]
panel_data_path = base_path + "panel/"
panel_files = [f for f in listdir(panel_data_path) if isfile(join(panel_data_path, f))]
panel_files = [f for f in panel_files if f!=".DS_Store"]
lar_data_path = base_path + "lar/"
lar_files = [f for f in listdir(lar_data_path) if isfile(join(lar_data_path, f))]
lar_files = [f for f in lar_files if f!=".DS_Store"]


# In[27]:


def load_lar_dat():
    """Loads National Archives fixed width DAT files of HMDA LAR data to Postgres"""
    cur, pg_conn = connect()
    for file in lar_files:
        if file[-3:] == "dat":
            table_name = "lar_"+file[8:12] + "_ffiec"
            print(table_name)
            with open("../sql/lar_2004_2013.sql") as sql_file: #get sql script
                sql = sql_file.read()
            sql = sql.format(table=table_name, data_file=lar_data_path+file)
            cur.execute(sql,) #execute SQL to database
        else:
            print("not a dat file")
    pg_conn.close()
    

def load_ts_dat():
    """Loads National Archives fixed width DAT files of HMDA TS data to Postgres"""
    cur, pg_conn = connect()
    for file in ts_files:
        if file[-3:] == "dat":
            table_name = "ts_"+file[7:11] + "_ffiec"
            print(table_name)
            with open("../sql/ts_2004_2013.sql") as sql_file: #get sql script
                sql = sql_file.read()
            sql = sql.format(table=table_name, data_file=ts_data_path+file)
            cur.execute(sql,) #execute SQL to database
        else:
            print("not a dat file")
    pg_conn.close()
    
def load_panel_dat():
    """Loads National Archives and FFIEC fixed width DAT files of HMDA Panel data to Postgres"""
    cur, pg_conn = connect()
    for file in panel_files:
        if int(file[-8:-4]) < 2014:
            table_name = "panel_"+ file[10:14] + "_ffiec"
            print(table_name)
            with open("../sql/panel_2004_2013.sql") as sql_file: #get sql script
                sql = sql_file.read()
            sql = sql.format(table=table_name, data_file=panel_data_path+file)
            cur.execute(sql,) #execute SQL to database
        else:
            print("not a dat file")
    pg_conn.close()

def load_panel_latest():
    """Loads FFIEC TSV HMDA Panel files to Postgres"""
    cur, pg_conn = connect()
    for file in panel_files:
        if file[-3:] == "tsv":
            table_name = "panel_"+file[-8:-4] + "_ffiec"
            print(table_name)
            with open("../sql/panel_latest.sql") as sql_file: #get sql script
                sql = sql_file.read()
            sql = sql.format(table=table_name, data_file=panel_data_path+file)
            cur.execute(sql,) #execute SQL to database
        else:
            print("not a dat file")
    pg_conn.close()
def load_lar_csv():
    """Loads FFIEC CSV HMDA LAR files to Postgres"""
    cur, pg_conn = connect()
    for file in lar_files:
        if file[-3:] == "csv":
            table_name = "lar_"+file[4:8] + "_ffiec"
            print(table_name)
            with open("../sql/lar_csv.sql") as sql_file:
                sql = sql_file.read()
            sql = sql.format(table=table_name, data_file=lar_data_path + file)
            cur.execute(sql,)
        else:
            print("not a csv file")
            
def load_ts_csv():
    """Loads FFIEC TST HMDA TS files to Postgres"""
    cur, pg_conn = connect()
    for file in ts_files:
        if file[-3:] == "txt":
            table_name = "ts_"+file[3:7] + "_ffiec"
            print(table_name)
            with open("../sql/ts_csv.sql") as sql_file:
                sql = sql_file.read()
            sql = sql.format(table=table_name, data_file=ts_data_path + file)
            cur.execute(sql,)
        else:
            print("not a csv file")


# In[ ]:


load_panel_latest()
load_panel_dat()
load_ts_dat()
load_ts_csv()
load_lar_csv()
load_lar_dat()
load_lar_dat()


# In[28]:




