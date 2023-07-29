import os
import requests

TEQUILA_API = os.environ["TEQUILA_API"]
TEQUILA_ENDPOINT = os.environ["TEQUILA_ENDPOINT"]


class FlightData:
    def __init__(self, row_city):
        self.tequila_api = TEQUILA_API
        self.tequila_endpoint = TEQUILA_ENDPOINT
        self.headers = {
            'apikey': self.tequila_api
        }
        self.params = {
            'term': row_city
        }
        self.iata_code = ''

    def get_kiwi_data(self):
        response = requests.get(url=self.tequila_endpoint, headers=self.headers, params=self.params)
        self.iata_code = response.json()['locations'][0]['code']
