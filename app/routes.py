from app import app
from flask import jsonify, request
from app.controller.irradiance import Irradiance
from app.controller.weather import Weather
from app.controller.rom import ROM

@app.route('/irradiance', methods=['GET','POST'])
def upload_irradiance():
    if request.method == 'POST':
        object_irradiance = Irradiance()
        object_irradiance.upload_file()

    response = {
        'message':'Data berhasil dikirim'
    }

    return jsonify(response), 200


@app.route('/irradiance/<tanggal>')
def get_irradiance(tanggal):
    object_irradiance = Irradiance()
    result = object_irradiance.get_irradiance(tanggal)

    response = {
        'message':'Sukses',
        'data': result
    }

    return jsonify(response), 200


@app.route('/weather-tomorrow')
def get_weather_tomorrow():
    object_weather = Weather()
    result = object_weather.get_tomorrow()

    response = {
        'message':'Sukses',
        'data': result
    }   
    
    return jsonify(response), 200


@app.route('/weather-today')
def get_weather_tomorrow():
    object_weather = Weather()
    result = object_weather.get_today()

    response = {
        'message':'Sukses',
        'data': result
    }   
    
    return jsonify(response), 200


@app.route('/rom', methods=['GET','POST'])
def upload_rom():
    if request.method == 'POST':
        object_rom = ROM()
        object_rom.upload_rom()

    response = {
        'message':'Data berhasil dikirim'
    }

    return jsonify(response), 200


@app.route('/rompltd/<tanggal>')
def get_rompltd(tanggal):
    object_rom = ROM()
    result = object_rom.get_pltd(tanggal)

    response = {
        'message':'Sukses',
        'data': result
    }   
    
    return jsonify(response), 200


@app.route('/rompv/<tanggal>')
def get_rompv(tanggal):
    object_rom = ROM()
    result = object_rom.get_pv(tanggal)

    response = {
        'message':'Sukses',
        'data': result
    }   
    
    return jsonify(response), 200


@app.route('/rombss/<tanggal>')
def get_rombss(tanggal):
    object_rom = ROM()
    result = object_rom.get_bss(tanggal)

    response = {
        'message':'Sukses',
        'data': result
    }   
    
    return jsonify(response), 200