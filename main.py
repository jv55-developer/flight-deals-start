import requests
#
# api_key = 'QEj6o5nJJ0Lcfhb2vOzoa-9IVeu4jWob'  # Replace with your Tequila Kiwi API key
#
# url = 'https://api.tequila.kiwi.com/locations/query'
# headers = {
#     'apikey': api_key
# }
#
# sheety_get_endpoint = 'https://api.sheety.co/6c0887c27fe16c2892977f767bcbbd82/flightDeals/sheet1'
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