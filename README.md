COVID-19 Tracker
A web application that tracks COVID-19 statistics for various countries. The app fetches data from a public API, processes it using an ETL (Extract, Transform, Load) pipeline, and stores the information in a PostgreSQL database. The frontend displays the data using a Flask web server.

Features
Fetches live COVID-19 data from a public API.
ETL pipeline to clean and store data in a PostgreSQL database.
Displays data in a web interface using Flask.
Deployable on cloud platforms like Render or Heroku.
Technologies Used
Python
Flask
PostgreSQL (can use SQLite as an alternative for local development)
SQLAlchemy
Pandas
Gunicorn (for production)
dotenv (for environment variable management)
Installation
Prerequisites
Python 3.11+
PostgreSQL (or SQLite for local development)
A terminal/command line interface
Steps
Clone the repository:


git clone https://github.com/kobasi896/covid19-tracker.git
cd covid19-tracker

Install dependencies:

pip install -r requirements.txt
Set up environment variables:

Create a .env file in the root of your project and add your database configuration:

bash
Copy code
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=covid_db
If using SQLite for local development, you can skip the above and the application will automatically use SQLite.

Run the ETL Process:

Before starting the app, run the ETL process to populate your database with data:

python etl.py
Run the application locally:

For local development:

python app.py
Access the app at http://127.0.0.1:5000.

Deployment
On Render
Ensure gunicorn is listed in your requirements.txt.

Modify the Procfile for deployment. It should contain:


web: gunicorn app:app
Push the project to your repository and link it to the Render dashboard for deployment.

On Docker (Optional)
To run the application using Docker, ensure you have Docker installed, and create a Dockerfile like this:
run pip install -r requirements.txt
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]

Run the container:
docker build -t covid19-tracker .
docker run -p 5000:5000 covid19-tracker