from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager

# From data_manager Class
data = DataManager()
get_sheety_data = data.get_sheety_data()
sheety_data = data.sheety_data

# From flight_search Class
flight_search = FlightSearch()

# From notification_manager import Class
notification_manager = NotificationManager()

# Get IATA codes for Google sheet from Kiwi and populate Google Sheet
for location in sheety_data:
    row_city = location['city']
    row_id = location['id']

    # From flight_data Class
    flight_data = FlightData(row_city=row_city)

    # Request to Tequila Kiwi API for iata codes of Airports
    flight_data.get_kiwi_data()
    iata_code = flight_data.iata_code

    # Request to update Excel sheet iata column in Excel sheet
    data.put_sheety_data(row_id=row_id, iata_code=iata_code)

# Loop through all sheety items and run an api search for flight prices using city, iata code and price
for location in sheety_data:
    iata_code = location['iataCode']
    lowest_price = location['lowestPrice']
    city = location['city']

    flight_search.get_flight_date(iata_code=iata_code)
    flight_search_data = flight_search.flight_search_data
    date_from = flight_search.date_from
    date_to = flight_search.date_to
    price = flight_search_data['data'][0]['price']
    city_from = flight_search_data['data'][0]['cityFrom']
    fly_from = flight_search_data['data'][0]['flyFrom']

    if price < lowest_price:
        print(f'price is lower for {city}')
        notification_manager.send_sms(price, city, date_from, date_to, iata_code, city_from, fly_from)
    else:
        print(f'No lower price found for {city}')
