from sqlalchemy import create_engine
import pandas as pd
import time

Server='DESKTOP-5B2U0BF\SQLEXPRESS'
Database='merdata'
Driver='ODBC Driver 17 for SQL Server'
user='user1'
password='123456'
Database_Con=f'mssql://{user}:{password}@{Server}/{Database}?driver={Driver}'

engine=create_engine(Database_Con)
con=engine.connect()

id=149

while(id<=202):
    str(id)
    str1= " select * from [dbo].[antnenadata] where ID= \' " +str(id)+ " \' "
    df=pd.read_sql_query(str1,con)
    print(df)
    id+=1
    time.sleep(2)