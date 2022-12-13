import requests
import datetime
from notification_manager import NotificationManager

class FlightSearch:
    """It searches for flights regarding given parameters using the Tequila API."""

    def __init__(
        self,
        apikey,
        from_airport,
        to_airport,
        n_days,
        price,
        stopovers,
        email,
        email_pass
        ) -> None:

        KIWI_END = "https://api.tequila.kiwi.com/v2/search"
        self.n_days = n_days

        header = {
            "apikey": apikey,
            "Content-Type": "application/json"
        }

        parameters = {
            "fly_from": from_airport,
            "fly_to": to_airport,
            "date_from": self.get_date(True),
            "date_to": self.get_date(False),
            "curr": "EUR",
            "price_to": price,
            "max_stopovers": stopovers,
            "one_per_date": 1, 
        }

        response = requests.get(url=KIWI_END,headers=header,params=parameters)
        flight_data = response.json()

        #------Subtract relevant data out of .json file ----------
        #------ then format into a message              ----------
        for item in flight_data["data"]:
            apf = [item["cityFrom"],item["flyFrom"]]
            ap_from = "-".join(apf)
            apt = [item["cityTo"],item["flyTo"]]
            ap_to = "-".join(apt)
            f_price = f'{item["conversion"]["EUR"]}'+' EUR'
            utc_d = self.format_time(item["utc_departure"])
            utc_a = self.format_time(item["utc_arrival"])
            msg = f'Subject: Hey, Listen! \n\nLow price alert! \n{ap_from} - {ap_to}\n only for {f_price}\nUTC Departure time: {utc_d}\nUTC Arrival time: {utc_a}'
        #------ Send email -----------------------------------------   
            NotificationManager(my_email=email,my_pass=email_pass,message=msg)


    #------Get todays date or n_days after-----
    """This function is only needed because the API requires 
    the date in this format: DD/MM/YYYY and .datetime ouput is: YYYY-MM-DD"""
    def get_date(self,bool):
        if bool:
            today = str(datetime.datetime.now().date()).split("-")
        else:
            today = str(datetime.datetime.now().date()+datetime.timedelta(days=self.n_days)).split("-")
        return "/".join(today[::-1])
    #---------------------------------------------

    #------Convert ISO-8601 time-format to common time-format
    def format_time(self,dtime):
        cutshort = dtime[0:-5]
        n = cutshort.split("T")
        return " ".join(n)
    #----------------------------------------------

    
    