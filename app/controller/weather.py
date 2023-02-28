import requests
from bs4 import BeautifulSoup as bs

class Weather:
    def get_tomorrow(self):
        url = "https://data.bmkg.go.id/DataMKG/MEWS/DigitalForecast/DigitalForecast-SulawesiUtara.xml"
        response = requests.get(url,verify=True)
        r = response.text

        sangihe = bs(r,"xml")
        cuaca_sangihe = sangihe.find(id="501536").find(id="weather")

        # h6 = cuaca_sangihe.find(h='6').value.string
        h36 = cuaca_sangihe.find(h='36').value.string
        # h18 = cuaca_sangihe.find(h='18').value.string

        result = h36

        return result
    
    def get_today(self):
        url = "https://data.bmkg.go.id/DataMKG/MEWS/DigitalForecast/DigitalForecast-SulawesiUtara.xml"
        response = requests.get(url,verify=True)
        r = response.text

        sangihe = bs(r,"xml")
        cuaca_sangihe = sangihe.find(id="501536").find(id="weather")

        # h6 = cuaca_sangihe.find(h='6').value.string
        h12 = cuaca_sangihe.find(h='12').value.string
        # h18 = cuaca_sangihe.find(h='18').value.string

        result = h12

        return result