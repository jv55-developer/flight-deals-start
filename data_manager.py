import os
import requests

SHEETY_GET_ENDPOINT = os.environ["SHEETY_GET_ENDPOINT"]


class DataManager:
    def __init__(self):
        self.sheety_get_endpoint = SHEETY_GET_ENDPOINT
        self.sheety_data = []

    def get_sheety_data(self):
        response = requests.get(url=self.sheety_get_endpoint)
        self.sheety_data = response.json()['sheet1']

    def put_sheety_data(self, row_id, iata_code):
        put_params = {
            'sheet1': {
                'iataCode': iata_code
            }
        }
        response = requests.put(url=f"{self.sheety_get_endpoint}/{row_id}", json=put_params)
        return response
