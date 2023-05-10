from app import app
from flask import jsonify, request
from app.controller.irradiance import Irradiance
from app.controller.weather import Weather
from app.controller.rom import ROM
from app.controller.user import User


@app.route('/login', methods=['GET','POST'])
def login():
    object_user = User()
    if request.method == 'POST':
        result = object_user.login()

    return jsonify(result), 200


@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        object_user = User()
        result = object_user.register()

    response = {
        'message':'Data berhasil dikirim',
        'result': result
    }

    return jsonify(response), 200


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


@app.route('/weather-today')
def get_weather_today():
    object_weather = Weather()
    weather = object_weather.get_weather('12')
    temperature = object_weather.get_temperature('12')
    humidity = object_weather.get_humidity('12')
    wind = object_weather.get_wind('12')

    response = {
        'message':'Sukses',
        'data': {
        'weather': weather,
        'temperature': temperature,
        'humidity': humidity,
        'wind': wind
        }
    }   
    
    return jsonify(response), 200


@app.route('/weather-tomorrow')
def get_weather_tomorrow():
    object_weather = Weather()
    weather = object_weather.get_weather('36')
    temperature = object_weather.get_temperature('36')
    humidity = object_weather.get_humidity('36')
    wind = object_weather.get_wind('36')

    response = {
        'message':'Sukses',
        'data': {
        'weather': weather,
        'temperature': temperature,
        'humidity': humidity,
        'wind': wind
        }
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


@app.route('/rompltd/week')
def get_rompltd_week():
    object_rom = ROM()
    result = object_rom.get_pltd_week()

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


@app.route('/rompv/week')
def get_rompv_week():
    object_rom = ROM()
    result = object_rom.get_pv_week()

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


@app.route('/rombss/week')
def get_rombss_week():
    object_rom = ROM()
    result = object_rom.get_bss_week()

    response = {
        'message':'Sukses',
        'data': result
    }   
    
    return jsonify(response), 200


@app.route('/irradiance/tanggal')
def get_irradiance_4days():
    object_irradiance = Irradiance()
    result = object_irradiance.get_4days()

    response = {
        'message':'Sukses',
        'data': result
    }   
    
    return jsonify(response), 200