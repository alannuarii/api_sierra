from app import app
from flask import jsonify, request
from app.controller.irradiance import Irradiance

@app.route('/irradiance', methods=['GET','POST'])
def upload_irradiance():
    if request.method == 'POST':
        object_irradiance = Irradiance()
        object_irradiance.upload_file()

    response = {
        'message':'Data berhasil dikirim'
    }

    return jsonify(response), 200