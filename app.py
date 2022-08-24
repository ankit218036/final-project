from flask import Flask , render_template
from sqlalchemy import create_engine
import pandas as pd


app = Flask(__name__)

Server='DESKTOP-5B2U0BF\SQLEXPRESS'
Database='merdata'
Driver='ODBC Driver 17 for SQL Server'
Database_Con=f'mssql://@{Server}/{Database}?driver={Driver}'

engine=create_engine(Database_Con)
con=engine.connect()

df=pd.read_sql_query("select * from [dbo].[antnenadata]",con)
print(df)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/ts13_16.html")
def TS13_16():
    return render_template("ts13_16.html")

@app.route("/ts17_20.html")
def TS17_20():
    return render_template("ts17_20.html")

@app.route("/ts21_24.html")
def TS21_24():
    return render_template("ts21_24.html")

@app.route("/ts25_28.html")
def TS25_28():
    return render_template("ts25_28.html")

@app.route("/ts29_32.html")
def TS29_32():
    return render_template("ts29_32.html")

@app.route("/ts33_36.html")
def TS33_36():
    return render_template("ts33_36.html")

    if __name__("__main__"):
        app.run(debug=True)