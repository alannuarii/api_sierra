from app import app
from flask import jsonify, request
from app.controller.irradiance import Irradiance
from app.controller.weather import Weather
from app.controller.rom import ROM
from app.controller.user import User
from app.controller.prediction import prediction, get_arr_irradiance


@app.route("/login", methods=["GET", "POST"])
def login():
    object_user = User()
    if request.method == "POST":
        try:
            result = object_user.login()
            return jsonify(result), 200

        except Exception as e:
            error_message = {"message": "Terjadi kesalahan", "error": str(e)}
            return jsonify(error_message), 500
    
    response = {"message": "Metode HTTP yang diperlukan: POST"}
    return jsonify(response), 405


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        try:
            object_user = User()
            result = object_user.register()

        except Exception as e:
            error_response = {"message": "Data gagal terkirim", "error": str(e)}
            return jsonify(error_response), 500

    response = {"message": "Data berhasil dikirim", "result": result}
    return jsonify(response), 200


@app.route("/irradiance", methods=["GET", "POST"])
def upload_irradiance():
    if request.method == "POST":
        try:
            object_irradiance = Irradiance()
            object_irradiance.upload_file()

        except Exception as e:
            error_response = {"message": "Data gagal terkirim", "error": str(e)}
            return jsonify(error_response), 500

    response = {"message": "Data berhasil dikirim"}
    return jsonify(response), 200


@app.route("/irradiance/<tanggal>")
def get_irradiance(tanggal):
    try:
        object_irradiance = Irradiance()
        result = object_irradiance.get_irradiance(tanggal)

        response = {"message": "Sukses", "data": result}
        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Terjadi kesalahan", "error": str(e)}
        return jsonify(error_response), 500


@app.route("/irradiance-array/<tanggal>")
def get_array_irradiance(tanggal):
    try:
        data = get_arr_irradiance(tanggal)

        response = {"message": "Sukses", "data": data}
        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Terjadi kesalahan", "error": str(e)}
        return jsonify(error_response), 500


@app.route("/weather-today")
def get_weather_today():
    try:
        object_weather = Weather()
        weather = object_weather.get_weather("12")
        temperature = object_weather.get_temperature("12")
        humidity = object_weather.get_humidity("12")
        wind = object_weather.get_wind("12")

        response = {
            "message": "Sukses",
            "data": {
                "weather": weather,
                "temperature": temperature,
                "humidity": humidity,
                "wind": wind,
            },
        }
        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Terjadi kesalahan", "error": str(e)}
        return jsonify(error_response), 500


@app.route("/weather-tomorrow")
def get_weather_tomorrow():
    try:
        object_weather = Weather()
        weather = object_weather.get_weather("36")
        temperature = object_weather.get_temperature("36")
        humidity = object_weather.get_humidity("36")
        wind = object_weather.get_wind("36")

        response = {
            "message": "Sukses",
            "data": {
                "weather": weather,
                "temperature": temperature,
                "humidity": humidity,
                "wind": wind,
            },
        }

        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Terjadi kesalahan", "error": str(e)}
        return jsonify(error_response), 500


@app.route("/rom", methods=["GET", "POST"])
def upload_rom():
    if request.method == "POST":
        try:
            object_rom = ROM()
            object_rom.upload_rom()

        except Exception as e:
            error_response = {"message": "Data gagal terkirim", "error": str(e)}
            return jsonify(error_response), 500

    response = {"message": "Data berhasil dikirim"}
    return jsonify(response), 200


@app.route("/rompltd/<tanggal>")
def get_rompltd(tanggal):
    try:
        object_rom = ROM()
        result = object_rom.get_pltd(tanggal)

        response = {"message": "Sukses", "data": result}
        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Terjadi kesalahan", "error": str(e)}
        return jsonify(error_response), 500


@app.route("/rompltd/week")
def get_rompltd_week():
    try:
        object_rom = ROM()
        result = object_rom.get_pltd_week()

        response = {"message": "Sukses", "data": result}
        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Terjadi kesalahan", "error": str(e)}
        return jsonify(error_response), 500


@app.route("/rompv/<tanggal>")
def get_rompv(tanggal):
    try:
        object_rom = ROM()
        result = object_rom.get_pv(tanggal)

        response = {"message": "Sukses", "data": result}
        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Terjadi kesalahan", "error": str(e)}
        return jsonify(error_response), 500


@app.route("/rompv/week")
def get_rompv_week():
    try:
        object_rom = ROM()
        result = object_rom.get_pv_week()

        response = {"message": "Sukses", "data": result}
        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Terjadi kesalahan", "error": str(e)}
        return jsonify(error_response), 500


@app.route("/rombss/<tanggal>")
def get_rombss(tanggal):
    try:
        object_rom = ROM()
        result = object_rom.get_bss(tanggal)

        response = {"message": "Sukses", "data": result}
        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Terjadi kesalahan", "error": str(e)}
        return jsonify(error_response), 500


@app.route("/rombss/week")
def get_rombss_week():
    try:
        object_rom = ROM()
        result = object_rom.get_bss_week()

        response = {"message": "Sukses", "data": result}
        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Terjadi kesalahan", "error": str(e)}
        return jsonify(error_response), 500


@app.route("/irradiance/tanggal")
def get_irradiance_4days():
    try:
        object_irradiance = Irradiance()
        result = object_irradiance.get_4days()

        response = {"message": "Sukses", "data": result}
        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Terjadi kesalahan", "error": str(e)}
        return jsonify(error_response), 500


@app.route("/forcast-today/<tanggal>")
def get_forcast_today(tanggal):
    try:
        today = prediction(tanggal, "12")

        response = {"message": "Sukses", "data": today}
        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Terjadi kesalahan", "error": str(e)}
        return jsonify(error_response), 500


@app.route("/forcast-tomorrow/<tanggal>")
def get_forcast_tomorrow(tanggal):
    try:
        tomorrow = prediction(tanggal, "36")

        response = {"message": "Sukses", "data": tomorrow}
        return jsonify(response), 200

    except Exception as e:
        error_response = {"message": "Terjadi kesalahan", "error": str(e)}
        return jsonify(error_response), 500
