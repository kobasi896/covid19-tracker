import os
import pandas as pd
from sqlalchemy import create_engine
from extract import fetch_covid_data
from dotenv import load_dotenv

def etl_process():
    # Load environment variables
    load_dotenv()

    # Fetch data
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

        # db_user = os.getenv('DB_USER')
        # db_password = os.getenv('DB_PASSWORD')
        # db_host = os.getenv('DB_HOST', 'localhost')
        # db_port = os.getenv('DB_PORT', '5432')
        # db_name = os.getenv('DB_NAME', 'covid_db')

        # engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
        
        db_url = os.getenv('DATABASE_URL', 'postgresql://user:EcH5C1RXceVILUZUJtAcvLX8bdM3ibG3@dpg-crslure8ii6s73eeoqf0-a.oregon-postgres.render.com/dbname_t5s9')
        engine = create_engine(db_url)
    
        try:
            # Load data into the database, creating the table if it doesn't exist
            df.to_sql('covid_stats', engine, if_exists='replace', index=False)
            print("Data loaded successfully.")
        except Exception as e:
            print(f"This is the error: {e}")
    else:
        print("Failed to fetch data.")

if __name__ == "__main__":
    etl_process()
