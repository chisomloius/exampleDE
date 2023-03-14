# import libraries
from sqlalchemy import create_engine
import pyodbc
import pandas as pd
import os #for using environ variable
import config

# set password
#pwd= os.environ['']
#uni= os.envrion['']
pwd= config.PASSWORD
uid= config.USERNAME


#SQL DB
driver = "{ODBC Driver 17 for SQL Server}"
server = "BNY-2105"
database = "AdventureWorksDW2019"

# extract data from sql server
def extract_data():
    #try block
    try:
        strConn = pyodbc.connect('DRIVER=' + driver +'; SERVER' + server + '; DATABASE=' + database + ';UID=' + uid + ';PWD=' + pwd + ';Trusted_Connection=yes')
        conn = strConn.cursor()
        # exexcute query
        conn.execute("""" SELECT t.name as table_name
                           FROM sys.tables t where t.name in ('DimProduct','DimProductSubcategory','DimProductCategory',
                                                              'DimSalesTerritory','FactInternetSales', 'FactFinance') 
                    """
                     )
        src_tables = conn.fetchall()
        for tbl in src_tables:
            #query and load save data to dataframe
            df = pd.read_sql_query(f'SELECT * FROM {tbl[0]}', strConn)
            load_data(df, tbl[0])

    except Exception as e:
        print("Data extract error: " + str(e))

    finally:
        strConn.close()

#load data to postgres
def load_data(df, tbl):
    
    try:
        rowsImported = 0
        engine = create_engine(f'postgresql://{uid}:{pwd}@{server}:5432/AdventureWorks')
        print(f'importing rows {rowsImported} to {rowsImported + len(df)}... for table {tbl}')

        # save df to postgres
        df.to_sql(f'stg_{tbl}', engine, if_exists='replace', index=False)
        rowsImported += len(df)

        # add elapsed time to final print out
        print("Data imported successful")

    except Exception as e:
        print("Data load error: " + str(e))

try:
    #call extract function
    extract_data()
except Exception as e:
    print("Error while extracting data: " + str(e))