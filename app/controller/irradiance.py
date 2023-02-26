from flask import request
import pandas as pd

class Irradiance:
    def upload_file(self):
        tanggal = request.form['tanggal']
        file = request.files['irradiance']

        data_csv = pd.read_csv(file)

        data = data_csv.iloc[0].to_dict()

        unwanted_keys = []

        # loop untuk menghapus key dan value yang tidak diinginkan
        for key in data:
            if not key.endswith('_Average'):
                unwanted_keys.append(key)

        for key in unwanted_keys:
            data.pop(key)
            
        print(data)
   