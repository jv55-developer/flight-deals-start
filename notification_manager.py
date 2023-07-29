import os
from twilio.rest import Client

ACCOUNT_SID = os.environ["TWILIO_SID"]
AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
FROM_NUMBER = os.environ["FROM_NUMBER"]
TO_NUMBER = os.environ["TO_NUMBER"]


class NotificationManager:

    def __init__(self):
        self.account_sid = ACCOUNT_SID
        self.auth_token = AUTH_TOKEN
        self.from_number = FROM_NUMBER
        self.to_number = TO_NUMBER

    def send_sms(self, price, city, date_from, date_to, iata_code, city_from, fly_from):
        client = Client(self.account_sid, self.auth_token)
        sms_message = f"Low price alert! Only £{price} to fly from {city}-{iata_code} to {city_from}-{fly_from}, " \
                      f"from {date_from} to {date_to}"
        message = client.messages.create(
            from_=self.from_number,
            body=sms_message,
            to=self.to_number
        )
        return message
