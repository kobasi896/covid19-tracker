# extract.py
import requests

def fetch_covid_data():
    url = "https://disease.sh/v3/covid-19/countries"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
