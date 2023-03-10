from flask import request
from db import connection
from datetime import datetime, timedelta, date
import pandas as pd

class Irradiance:
    time_average = ['5','6','7','8','9','10','11','12','13','14','15','16','17','18','19']

    def upload_file(self):
        tanggal = request.form['tanggal']
        file = request.files['irradiance']

        data_csv = pd.read_csv(file)
        data_dict = data_csv.iloc[0].to_dict()

        unwanted_keys = []

        for key in data_dict:
            if not key.endswith('_Average'):
                unwanted_keys.append(key)

        for key in unwanted_keys:
            data_dict.pop(key)

        value_irradiance = list(data_dict.values())
            
        for i in range(len(self.time_average)):
            self.insert_irradiance(tanggal, self.time_average[i], value_irradiance[i])

    def insert_irradiance(self, tanggal, waktu, value):
        query = f"INSERT INTO irradiance (tanggal, waktu, value) VALUES ('{tanggal}', '{waktu}', {value})"
        connection(query, 'insert')

    def get_irradiance(self, tanggal):
        tanggal_plus = datetime.strptime(tanggal, '%Y-%m-%d')
        full_awal = tanggal_plus - timedelta(days=3)
        full_akhir = tanggal_plus - timedelta(days=1)
        awal = full_awal.strftime('%Y-%m-%d')
        akhir = full_akhir.strftime('%Y-%m-%d')
        query = f"SELECT waktu, value FROM irradiance WHERE tanggal BETWEEN '{awal}' AND '{akhir}'"
        result = connection(query, 'select')
        return result
    
    def get_4days(self):
        query = f"SELECT tanggal FROM irradiance WHERE tanggal BETWEEN DATE_SUB(CURDATE(), INTERVAL 3 DAY) AND CURDATE() GROUP BY tanggal"
        result = connection(query, 'select')
        return result

   