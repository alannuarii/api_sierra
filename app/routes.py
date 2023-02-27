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


@app.route('/weather')
def get_weather():
    object_weather = Weather()
    result = object_weather.get_weather()

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