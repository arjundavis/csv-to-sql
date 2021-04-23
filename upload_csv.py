# Short python script for inserting a csv into an MS SQL table
# Created by Arjun David Rao

import pandas as pd
import pyodbc
import sqlalchemy

csv = input("csv filename : ")
if not csv.endswith('.csv'):
    csv = input("Please insert filename with csv extension : ")
table = input("SQL table name : ")
svr = input("Server name : ")
db = input("Database name : ")


def SQL_connect(csv_file, table_name, server, database):
    df = pd.read_csv(csv_file, index_col=None)
    print(df)

    

    engine = sqlalchemy.create_engine('mssql+pyodbc://' + server + '/' + database + '?trusted_connection=yes&driver=ODBC+Driver+13+for+SQL+Server')

    # write the DataFrame to a table in the sql database
    df.to_sql(table, engine, if_exists='append', index = False)

if __name__ == "__main__":
    SQL_connect(csv, table, svr, db)
