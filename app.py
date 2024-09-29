# app.py
from flask import Flask, render_template
from sqlalchemy import create_engine
import pandas as pd
from etl import etl_process
import os

app = Flask(__name__)

# Run ETL process on startup
etl_process()

def get_data():
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST', 'localhost')
    db_port = os.getenv('DB_PORT', '5432')
    db_name = os.getenv('DB_NAME', 'covid_db')

    engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
    query = "SELECT * FROM covid_stats"
    df = pd.read_sql(query, engine)
    return df

@app.route('/')
def home():
    df = get_data()
    return render_template('index.html', tables=[df.to_html(classes='data', index=False)], titles=df.columns.values)

if __name__ == "__main__":
    app.run(debug=True)
