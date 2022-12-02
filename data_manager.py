import requests

class DataManager:
    def __init__(self,sheetyend,sheetypass) -> None:
        
        HEADER = {
            "Content-Type": "application/json",
            "Authorization": sheetypass
        }

        response = requests.get(url=sheetyend,headers=HEADER)
        page = response.json()
        for key,value in page.items():
            self.page_data = value
        