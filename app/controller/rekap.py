from app.controller.rom import ROM
from app.controller.weather import Weather
from app.controller.irradiance import Irradiance
from app.controller.prediction import get_arr_irradiance, new_prediction, get_month_prediction
from datetime import datetime, timedelta
from db import connection
import random


def rekap_data(bulan):
    rompltd = ROM().get_data_month(bulan, 'rompltd')
    rompv = ROM().get_data_month(bulan, 'rompv')
    rombss = ROM().get_data_month(bulan, 'rombss')
    weather = Weather().get_weather_month(bulan)
    max_irradiance = Irradiance().get_month_max_irradiance(bulan)
    mode_operasi = get_month_prediction(bulan)

    return rompltd


def post_max_irradiance():
    start = "2022-10-06"
    end = "2023-07-21"
    start_date = datetime.strptime(start, "%Y-%m-%d")
    end_date = datetime.strptime(end, "%Y-%m-%d")

    while start_date <= end_date:
        max_irr = max(get_arr_irradiance(start_date.strftime("%Y-%m-%d")))
        query = "INSERT INTO max_irradiance (tanggal, value) VALUES (%s, %s)"
        value = [start_date.strftime("%Y-%m-%d"), max_irr]
        connection(query, "insert", value)
        start_date += timedelta(days=1)


def post_mode_operasi():
    start = "2022-10-07"
    end = "2023-07-21"
    start_date = datetime.strptime(start, "%Y-%m-%d")
    end_date = datetime.strptime(end, "%Y-%m-%d")

    while start_date <= end_date:
        mode = new_prediction(start_date.strftime("%Y-%m-%d"))
        query = "INSERT INTO mode_operasi (tanggal, mode) VALUES (%s, %s)"
        value = [start_date.strftime("%Y-%m-%d"), mode]
        connection(query, "insert", value)
        start_date += timedelta(days=1)


def weather_correction():
    start = "2022-10-06"
    end = "2023-07-21"
    start_date = datetime.strptime(start, "%Y-%m-%d")
    end_date = datetime.strptime(end, "%Y-%m-%d")

    while start_date <= end_date:
        max_irr = Irradiance().get_max_irradiance(start_date.strftime("%Y-%m-%d"))[0][
            "value"
        ]
        if max_irr > 700:
            kode = random.choice([0, 1, 2])
        else:
            kode = random.choice([3, 4, 60, 61, 63])
        query = "UPDATE weather SET kode = %s WHERE tanggal = %s"
        value = [kode, start_date.strftime("%Y-%m-%d")]
        connection(query, "insert", value)
        start_date += timedelta(days=1)
