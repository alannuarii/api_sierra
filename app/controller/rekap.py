from app.controller.rom import ROM
from app.controller.weather import Weather
from app.controller.irradiance import Irradiance
from app.controller.prediction import prediction, get_arr_irradiance
from datetime import datetime, timedelta
from db import connection


def rekap_data(bulan):
    # irr = []
    mode = []
    tahun, bulan = map(int, bulan.split("-"))
    tanggal_awal = datetime(year=tahun, month=bulan, day=1)
    if bulan == 12:
        tanggal_akhir = datetime(year=tahun + 1, month=1, day=1) - timedelta(days=1)
    else:
        tanggal_akhir = datetime(year=tahun, month=bulan + 1, day=1) - timedelta(days=1)

    while tanggal_awal <= tanggal_akhir:
        tanggal = tanggal_awal.strftime("%Y-%m-%d")
        # irr.append(max(get_arr_irradiance(tanggal)))
        mode.append(prediction(tanggal, '12'))
        tanggal_awal += timedelta(days=1)
    
    return mode

def post_max_irradiance():
    start = "2022-10-06"
    end = "2023-07-21"
    start_date = datetime.strptime(start, "%Y-%m-%d")
    end_date = datetime.strptime(end, "%Y-%m-%d")
    
    while start_date <= end_date:
        max_irr = max(get_arr_irradiance(start_date.strftime("%Y-%m-%d")))
        query = "INSERT INTO max_irradiance (tanggal, value) VALUES (%s, %s)"
        value = [start_date.strftime("%Y-%m-%d"), max_irr]
        connection(query, 'insert', value)
        start_date += timedelta(days=1)
