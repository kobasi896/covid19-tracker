import requests

def fetch_covid_data():
    url = "https://disease.sh/v3/covid-19/countries"
    try:
        response = requests.get(url, timeout=10)  # Set timeout to 10 seconds
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Log HTTP error
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Error connecting to the API: {conn_err}")  # Log connection error
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error: {timeout_err}")  # Log timeout error
    except requests.exceptions.RequestException as req_err:
        print(f"An error occurred: {req_err}")  # Log any other request errors
    return None  # Return None if an error occurs
