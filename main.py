from data_manager import DataManager
from flight_search import FlightSearch
import os

MY_AIRPORT = os.environ["MY_AIRPORT"]       #Your closest airport IATA Code
MY_EMAIL = os.environ["MY_EMAIL"]           #Your email address (sender and receiver)
EMAIL_PASS = os.environ["EMAIL_PASS"]       #Your email app password
API_KEY = os.environ["API_KEY"]             #kiwi.com api key
SHEETY_END = os.environ["SHEETY_END"]       #Your google-sheet end link. Sheet format: "City"/"IATA Code"/"Lowest Price"
SHEETY_PASS = os.environ["SHEETY_PASS"]     #Sheety Basic Authentication password

dataman = DataManager(sheetyend=SHEETY_END,sheetypass=SHEETY_PASS)
city_lst = dataman.page_data

for route in city_lst:

    try:
        FlightSearch(
            apikey=API_KEY,
            from_airport= MY_AIRPORT,
            to_airport= route["iataCode"],
            price= route["lowestPrice"],
            n_days= 30,                         #Look for deals up to "n_days"
            stopovers= 0,                       #Maximum stopovers 0 for direct flights
            email= MY_EMAIL,
            email_pass= EMAIL_PASS
            )
    except IndexError:
        print("Couldn't find a deal.")
        break
