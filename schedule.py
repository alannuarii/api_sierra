#!/usr/bin/env python3

from app.controller.weather import Weather

def post_weather():
    object_weather = Weather()
    object_weather.insert_weather()

if __name__ == "__main__":
    post_weather()