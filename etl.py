# etl.py
import os
import pandas as pd
from sqlalchemy import create_engine
from extract import fetch_covid_data

def etl_process():
    data = fetch_covid_data()
    if data:
        df = pd.DataFrame(data)
        df = df[['country', 'cases', 'todayCases', 'deaths', 'todayDeaths', 'recovered']]
        df.rename(columns={
            'country': 'Country',
            'cases': 'Total Cases',
            'todayCases': 'Today Cases',
            'deaths': 'Total Deaths',
            'todayDeaths': 'Today Deaths',
            'recovered': 'Recovered'
        }, inplace=True)
        
        db_user = os.getenv('DB_USER')
        db_password = os.getenv('DB_PASSWORD')
        db_host = os.getenv('DB_HOST', 'localhost')
        db_port = os.getenv('DB_PORT', '5432')
        db_name = os.getenv('DB_NAME', 'covid_db')

        engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
        df.to_sql('covid_stats', engine, if_exists='replace', index=False)
        print("Data loaded successfully.")
    else:
        print("Failed to fetch data.")

if __name__ == "__main__":
    etl_process()
