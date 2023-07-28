#!/usr/bin/env python3

from app.controller.weather import Weather
from app.controller.rom import ROM

def post_schedule():
    object_weather = Weather()
    object_rom = ROM()
    object_weather.insert_weather()
    object_rom.auto_upload_rom('rompltd')
    object_rom.auto_upload_rom('rompv')
    object_rom.auto_upload_rom('rombss')

if __name__ == "__main__":
    post_schedule()