import json
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from datetime import date
from app.data.training import training_data
from app.controller.rom import ROM
from app.controller.weather import Weather
from app.controller.irradiance import Irradiance

def get_arr_irradiance(tanggal):
    object_irradiance = Irradiance()
    data = object_irradiance.get_irradiance(tanggal)

    period = 3  # Jumlah periode waktu yang digunakan untuk menghitung EMA

    ema_values = []  # Menyimpan nilai-nilai EMA
    times = []  # Menyimpan waktu

    prev_ema = data[0]["value"]  # Nilai EMA pertama diinisialisasi dengan nilai pertama dalam data
    multiplier = 2 / (period + 1)  # Menghitung faktor pengali EMA

    for i in range(len(data)):
        value = data[i]["value"]
        waktu = data[i]["waktu"]
        ema = (value * multiplier) + (prev_ema * (1 - multiplier))
        ema_values.append(ema)
        times.append(waktu)
        prev_ema = ema

    result = ema_values[-15:]
    return result

def prediction(tanggal):
    # today = date.today()

    object_rom = ROM()
    object_weather = Weather()

    pltd = object_rom.get_pltd(tanggal)
    pv = object_rom.get_pv(tanggal)
    bss = object_rom.get_bss(tanggal)

    total_pltd = pltd[0]['status'] + pltd[1]['status']
    total_pv = pv[0]['status'] + pv[1]['status']
    total_bss = bss[0]['status'] + bss[1]['status']

    weather_today = int(object_weather.get_weather('12'))

    if weather_today == 0 or weather_today == 1 or weather_today == 2:
        weather_today = 1
    else:
        weather_today = 0

    irr = max(get_arr_irradiance(tanggal))
    
    features = ['pltd', 'pv', 'bss', 'cuaca', 'irr']
    target = 'mode'

    if irr > 700:
        irr = 1
    else:
        irr = 0

    data_testing = {
    'pv': total_pv,
    'bss': total_bss,
    'pltd': total_pltd,
    'cuaca': weather_today,
    'irr': irr,
    }

    X = [[data[f] for f in features] for data in training_data]
    y = [data[target] for data in training_data]

    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)

    y_pred = clf.predict(X_test)

    X_test = [[data_testing[f] for f in features]]
    y_pred = clf.predict(X_test)

    mode_predicted = label_encoder.inverse_transform(y_pred)

    return mode_predicted[0]
