from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

def test_connection():
    try:
        # Load environment variables from .env file
        load_dotenv()

        # Fetch database connection details from environment variables
        db_user = os.getenv('DB_USER')
        db_password = os.getenv('DB_PASSWORD')
        db_host = os.getenv('DB_HOST', 'localhost')
        db_port = os.getenv('DB_PORT', '8000')
        db_name = os.getenv('DB_NAME', 'covid_db')

        # Create the SQLAlchemy engine using environment variables
        engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

        # Attempt to establish a connection to the database
        connection = engine.connect()
        print("Connection successful!")
        connection.close()

    except Exception as e:
        print("Connection failed!")
        print(e)

if __name__ == "__main__":
    test_connection()
