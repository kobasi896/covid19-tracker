from flask import Flask, render_template
from sqlalchemy import create_engine
import pandas as pd
from etl import etl_process
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Run ETL process on startup
etl_process()

# Database connection setup
# db_user = os.getenv('DB_USER')
# db_host = os.getenv('DB_HOST', 'localhost')
# db_password = os.getenv('DB_PASSWORD')
# db_port = os.getenv('DB_PORT', '5432')
# db_name = os.getenv('DB_NAME', 'covid_db')

# # Create the SQLAlchemy engine once at startup
# engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')



def get_data():
    db_url = os.getenv('DATABASE_URL', 'postgresql://user:EcH5C1RXceVILUZUJtAcvLX8bdM3ibG3@dpg-crslure8ii6s73eeoqf0-a.oregon-postgres.render.com/dbname_t5s9')
    engine = create_engine(db_url)
    query = "SELECT * FROM covid_stats"
    try:
        df = pd.read_sql(query, engine)
        if df.empty:
            return pd.DataFrame(columns=['No Data Available'])
        return df
    except Exception as e:
        print(f"Error fetching data: {e}")
        return pd.DataFrame(columns=['Error Fetching Data'])

@app.route('/')
def home():
    df = get_data()
    return render_template('index.html', tables=[df.to_html(classes='data', index=False)], titles=df.columns.values)

if __name__ == "__main__":
    app.run(debug=True)
