import requests
from bs4 import BeautifulSoup as bs

class Weather:
    url = "https://data.bmkg.go.id/DataMKG/MEWS/DigitalForecast/DigitalForecast-SulawesiUtara.xml"
    response = requests.get(url,verify=True)
    r = response.text
    sangihe = bs(r,"xml")


    def get_weather(self, hour):
        cuaca = self.sangihe.find(id="501536").find(id="weather")
        h12 = cuaca.find(h=hour).value.string
        result = h12
        return result

    
    def get_temperature(self, hour):
        temperature = self.sangihe.find(id="501536").find(id="t")
        h12 = temperature.find(h=hour).value.string
        result = h12
        return result
    

    def get_humidity(self, hour):
        humidity = self.sangihe.find(id="501536").find(id="hu")
        h12 = humidity.find(h=hour).value.string
        result = h12
        return result
    

    def get_wind(self, hour):
        humidity = self.sangihe.find(id="501536").find(id="ws")
        h12 = humidity.find(h=hour).value.string
        result = h12
        return result

