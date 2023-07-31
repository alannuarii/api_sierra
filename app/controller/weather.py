import requests
from bs4 import BeautifulSoup as bs
from db import connection
from datetime import datetime


class Weather:
    url = "https://data.bmkg.go.id/DataMKG/MEWS/DigitalForecast/DigitalForecast-SulawesiUtara.xml"
    response = requests.get(url, verify=True)
    r = response.text
    sangihe = bs(r, "xml")

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

    def insert_weather(self):
        tanggal = datetime.today().strftime("%Y-%m-%d")
        if self.get_kode_weather(tanggal):
            if self.get_kode_weather(tanggal)[0]['kode'] != int(self.get_weather('12')):
                self.update_kode_weather(tanggal)
            else:
                pass
        else:
            kode = int(self.get_weather("12"))
            query = f"INSERT INTO weather (tanggal, kode) VALUES (%s, %s)"
            value = [tanggal, kode]
            connection(query, "insert", value)

    def get_kode_weather(self, tanggal):
        query = f"SELECT kode FROM weather WHERE tanggal = %s"
        value = [tanggal]
        result = connection(query, 'select', value)
        return result
    
    def get_weather_month(self, bulan):
        query = f"SELECT tanggal, kode FROM weather WHERE DATE_FORMAT(tanggal, '%Y-%m') = %s"
        value = [bulan]
        result = connection(query, 'select', value)
        return result
    
    def update_kode_weather(self, tanggal):
        query = f"UPDATE weather SET kode = %s WHERE tanggal = %s"
        value = [self.get_weather('12'), tanggal]
        connection(query, 'update', value)
