import requests
import os
from datetime import datetime, timedelta
from twilio.rest import Client
from data_manager import DataManager

data = DataManager()
get_sheety_data = data.get_sheety_data()
sheety_data = data.sheety_data

TEQUILA_API = os.environ["TEQUILA_API"]
TEQUILA_ENDPOINT = os.environ["TEQUILA_ENDPOINT"]
TEQUILA_API_SEARCH = os.environ["TEQUILA_API_SEARCH"]

url = TEQUILA_ENDPOINT
url_2 = TEQUILA_API_SEARCH
headers = {
    'apikey': TEQUILA_API
}

# Twilio data
account_sid = os.environ["TWILIO_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
from_number = os.environ["FROM_NUMBER"]
to_number = os.environ["TO_NUMBER"]

client = Client(account_sid, auth_token)
current_datetime = datetime.now()

# Get IATA codes for Google sheet from Kiwi and populate Google Sheet
for location in sheety_data:
    row_city = location['city']
    row_id = location['id']
    params = {
        'term': row_city,  # Replace with the location term you want to search for
    }

    response = requests.get(url, headers=headers, params=params)
    iata_code = response.json()['locations'][0]['code']

    put_params = {
        'sheet1': {
            'iataCode': iata_code
        }
    }
    sheety_put_response = requests.put(url=f"{DataManager().sheety_get_endpoint}/{row_id}", json=put_params)


# Loop through all sheety items and run an api search for flight prices using city, iata code and price
# for location in sheety_get_data:
#     iata = location['iataCode']
#     price = location['lowestPrice']
#     city = location['city']
#
#     params = {
#         'fly_from': 'LHR',
#         'fly_to': iata,
#         'date_from': current_datetime.strftime("%d/%m/%Y"),
#         'date_to': (current_datetime + timedelta(days=15)).strftime("%d/%m/%Y")
#     }
#
#     flight_search_response = requests.get(url=url_2, headers=headers, params=params)
#     flight_search_data = flight_search_response.json()
#
#     if flight_search_data['data'][0]['price'] < price:
#         print(f'price is lower for {city}')
#         sms_message = f"Low price alert! Only {flight_search_data['data'][0]['price']} to fly from {city}-{iata} to " \
#                       f"f{flight_search_data['data'][0]['cityFrom']}-f{flight_search_data['data'][0]['flyFrom']}, " \
#                       f"from f{current_datetime.strftime('%d/%m/%Y')} " \
#                       f"to f{(current_datetime + timedelta(days=15)).strftime('%d/%m/%Y')}"
#         message = client.messages.create(
#             from_=from_number,
#             body=sms_message,
#             to=to_number
#         )
#     else:
#         print(f'No lower price found for {city}')

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.