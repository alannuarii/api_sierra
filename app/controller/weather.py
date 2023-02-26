import requests
from bs4 import BeautifulSoup as bs

class Weather:
    def get_weather(self):
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