import requests
# import os
#
# TEQUILA_API = os.environ["TEQUILA_API"]
# TEQUILA_ENDPOINT = os.environ["TEQUILA_ENDPOINT"]
# SHEETY_GET_ENDPOINT = os.environ["SHEETY_GET_ENDPOINT"]
#
# url = TEQUILA_ENDPOINT
# headers = {
#     'apikey': TEQUILA_API
# }
#
# sheety_get_endpoint = SHEETY_GET_ENDPOINT
#
# sheety_get_response = requests.get(url=sheety_get_endpoint)
#
# sheety_get_data = sheety_get_response.json()['sheet1']
#
# for location in sheety_get_data:
#     row_city = location['city']
#     row_id = location['id']
#     params = {
#         'term': row_city,  # Replace with the location term you want to search for
#     }
#
#     response = requests.get(url, headers=headers, params=params)
#     iata_code = response.json()['locations'][0]['code']
#
#     print(iata_code)















#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.