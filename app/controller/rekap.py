from app.controller.rom import ROM
from app.controller.weather import Weather
from app.controller.irradiance import Irradiance
from app.controller.prediction import (
    get_arr_irradiance,
    new_prediction,
    get_month_prediction,
)
from datetime import datetime, timedelta
from db import connection
import random


def get_mode_operasi(tanggal):
    query = f"SELECT mode FROM mode_operasi WHERE tanggal = %s"
    value = [tanggal]
    result = connection(query, 'select', value)
    return result


def update_mode_operasi(mode, tanggal):
    query = f"UPDATE mode_operasi SET mode = %s WHERE tanggal = %s"
    value = [mode, tanggal]
    connection(query, 'update', value)


def delete_correction(tanggal):
    query = f"DELETE from correction WHERE tanggal = %s"
    value = [tanggal]
    connection(query, 'delete', value)


def post_max_irradiance():
    start_date = Irradiance().get_last_max_irradiance()[0]["tanggal"] + timedelta(
        days=1
    )
    end_date = Irradiance().get_last_irradiance()[0]["tanggal"] + timedelta(days=1)

    while start_date <= end_date:
        max_irr = max(get_arr_irradiance(start_date.strftime("%Y-%m-%d")))
        query = "INSERT INTO max_irradiance (tanggal, value) VALUES (%s, %s)"
        value = [start_date.strftime("%Y-%m-%d"), max_irr]
        connection(query, "insert", value)
        start_date += timedelta(days=1)


def post_mode_operasi():
    query = f"SELECT tanggal, mode FROM mode_operasi ORDER BY tanggal DESC LIMIT %s"
    value = [1]
    last_data = connection(query, "select", value)
    start_date = last_data[0]["tanggal"] + timedelta(days=1)
    end_date = Irradiance().get_last_max_irradiance()[0]["tanggal"]

    while start_date <= end_date:
        mode = new_prediction(start_date.strftime("%Y-%m-%d"))
        query = "INSERT INTO mode_operasi (tanggal, mode) VALUES (%s, %s)"
        value = [start_date.strftime("%Y-%m-%d"), mode]
        connection(query, "insert", value)
        start_date += timedelta(days=1)


def mode_correction():
    query = f"SELECT tanggal FROM correction ORDER BY tanggal"
    value = []
    result = connection(query, "select", value)
    start_date = result[0]["tanggal"]
    end_date = result[-1]["tanggal"]

    while start_date <= end_date:
        if get_mode_operasi(start_date.strftime("%Y-%m-%d"))[0]['mode'] != new_prediction(start_date.strftime("%Y-%m-%d")):
            update_mode_operasi(new_prediction(start_date.strftime("%Y-%m-%d")), start_date.strftime("%Y-%m-%d"))
        delete_correction(start_date.strftime("%Y-%m-%d"))
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
