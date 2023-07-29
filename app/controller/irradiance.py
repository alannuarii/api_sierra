from flask import request
from db import connection
from datetime import datetime, timedelta, date
import pandas as pd

class Irradiance:
    time_average = ['5','6','7','8','9','10','11','12','13','14','15','16','17','18','19']

    def upload_file(self):
        tanggal = request.form['tanggal']
        file = request.files['irradiance']

        check_tanggal = self.get_date_irradiance(tanggal)
        if check_tanggal:
            self.delete_irradiance(tanggal)

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
        query = f"INSERT INTO irradiance (tanggal, waktu, value) VALUES (%s, %s, %s)"
        value = [tanggal, waktu, value]
        connection(query, 'insert', value)

    def delete_irradiance(self, tanggal):
        query = f"DELETE FROM irradiance WHERE tanggal = %s"
        value = [tanggal]
        connection(query, 'delete', value)


    def get_date_irradiance(self, tanggal):
        query = f"SELECT tanggal FROM irradiance WHERE tanggal = %s GROUP BY tanggal"
        value = [tanggal]
        result = connection(query, 'select', value)
        return result

    def get_irradiance(self, tanggal):
        tanggal_plus = datetime.strptime(tanggal, '%Y-%m-%d')
        full_awal = tanggal_plus - timedelta(days=3)
        full_akhir = tanggal_plus - timedelta(days=1)
        awal = full_awal.strftime('%Y-%m-%d')
        akhir = full_akhir.strftime('%Y-%m-%d')
        query = f"SELECT waktu, value FROM irradiance WHERE tanggal BETWEEN %s AND %s ORDER BY tanggal"
        value = [awal, akhir]
        result = connection(query, 'select', value)
        return result
    
    def get_4days(self):
        query = f"SELECT tanggal FROM irradiance WHERE tanggal BETWEEN DATE_SUB(CURDATE(), INTERVAL %s DAY) AND CURDATE() GROUP BY tanggal"
        value = [3]
        result = connection(query, 'select', value)
        return result
    
    def get_last_irradiance(self):
        query = f"SELECT tanggal FROM irradiance ORDER BY tanggal DESC LIMIT %s"
        value = [1]
        result = connection(query, 'select', value)
        return result
    
    def get_month_max_irradiance(self, bulan):
        month = int(bulan[5:])
        query = f"SELECT tanggal, value FROM max_irradiance WHERE EXTRACT(MONTH FROM tanggal) = %s"
        value = [month]
        result = connection(query, 'select', value)
        return result
    
    def get_max_irradiance(self, tanggal):
        query = f"SELECT value FROM max_irradiance WHERE tanggal = %s"
        value = [tanggal]
        result = connection(query, 'select', value)
        return result
    
    def get_last_max_irradiance(self):
        query = f"SELECT tanggal FROM max_irradiance ORDER BY tanggal DESC LIMIT %s"
        value = [1]
        result = connection(query, 'select', value)
        return result
    

   