import requests

class DataManager:
    """Get the information from the google-sheet."""
    """It needs the Sheety end-point and a password."""

    def __init__(self,sheetyend,sheetypass) -> None:
        
        HEADER = {
            "Content-Type": "application/json",
            "Authorization": sheetypass
        }

        response = requests.get(url=sheetyend,headers=HEADER)
        page = response.json()
        for key,value in page.items():
            self.page_data = value
        