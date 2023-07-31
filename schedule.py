#!/usr/bin/env python3

from app.controller.weather import Weather
from app.controller.rom import ROM
from app.controller.rekap import post_max_irradiance, post_mode_operasi, mode_correction

def post_schedule():
    object_weather = Weather()
    object_rom = ROM()
    object_weather.insert_weather()
    object_rom.auto_upload_rom('rompltd')
    object_rom.auto_upload_rom('rompv')
    object_rom.auto_upload_rom('rombss')
    post_max_irradiance()
    post_mode_operasi()
    mode_correction()

if __name__ == "__main__":
    post_schedule()