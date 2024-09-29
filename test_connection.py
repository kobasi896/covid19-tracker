from sqlalchemy import create_engine

def test_connection():
    try:
        engine = create_engine('postgresql://your_username:your_password@localhost:5432/covid_db')
        connection = engine.connect()
        print("Connection successful!")
        connection.close()
    except Exception as e:
        print("Connection failed!")
        print(e)

if __name__ == "__main__":
    test_connection()
