import os
import requests
from datetime import datetime, timedelta

TEQUILA_API = os.environ["TEQUILA_API"]
TEQUILA_ENDPOINT_SEARCH = os.environ["TEQUILA_API_SEARCH"]


class FlightSearch:

    def __init__(self):
        self.tequila_search_endpoint = TEQUILA_ENDPOINT_SEARCH
        self.tequila_api = TEQUILA_API
        self.headers = {
            'apikey': self.tequila_api
        }
        self.current_date = datetime.now()
        self.date_from = self.current_date.strftime("%d/%m/%Y")
        self.date_to = (self.current_date + timedelta(days=15)).strftime("%d/%m/%Y")
        self.flight_search_data = []

    def get_flight_date(self, iata_code):
        params = {
            'fly_from': 'LHR',
            'fly_to': iata_code,
            'date_from': self.date_from,
            'date_to': self.date_to
        }
        response = requests.get(url=self.tequila_search_endpoint, headers=self.headers, params=params)
        self.flight_search_data = response.json()
