from re import DEBUG, sub
from flask import Flask, render_template, request, redirect, send_file, url_for
from werkzeug.utils import secure_filename, send_from_directory
import os
import subprocess
from scripts_driver.visualize import plot_wind, plot_temp, plot_pressure, plot_humidity
from scripts_driver.svm_model import *
from scripts_driver.NB_model import *
from scripts_driver.viz import *
from scripts_driver.timeseries import predict
import pickle
import requests
import configparser
import time

app = Flask(__name__)


@app.route('/')
def index():
    # Performence
    NB_Accuracy, NB_Precision, NB_Recall = NB_PredictionMeasure()
    SVM_Accuracy, SVM_Precision, SVM_Recall = SVM_PredictionMeasure()

    return render_template('index.html',
                           NB_Accuracy=NB_Accuracy, NB_Precision=NB_Precision, NB_Recall=NB_Recall,
                           SVM_Accuracy=SVM_Accuracy, SVM_Precision=SVM_Precision, SVM_Recall=SVM_Recall)


@app.route('/eda', methods=['GET'])
def eda():
    # visualization
    w_fig = plot_wind()
    t_fig = plot_temp()
    p_fig = plot_pressure()
    h_fig = plot_humidity()
    return render_template('eda.html', ws_url=w_fig, tmp_url=t_fig, p_url=p_fig, h_url=h_fig,threaded=True)


@app.route('/classifier', methods=['GET', 'POST'])
def classify():
    return render_template('classifier.html')


@app.route('/classifierResult', methods=['GET','POST'])
def result():
    val = []
    result_val = ''
    if request.method == 'POST':
        zip_code = request.form['airportName']
        classifier = request.form['classifier']
        api_key = get_api_key()
        data = get_weather_data(zip_code, api_key)
        val.append("{0:.2f}".format(data["main"]["temp"]))
        val.append("{0:.2f}".format(data["main"]["humidity"]))
        val.append("{0:.2f}".format(data["wind"]["speed"]))
        val.append("{0:.2f}".format(data["main"]["pressure"]))
        if classifier == 'SVM':
            result = SVM_predict(val)
        else:
            result = NB_predict(val)
        if result[0] == 1:
            result_val = 'Voila! We can make a trip..'
        else:
            result_val = 'Ohh no! The weather seems bad.'
        
    return render_template('classifier.html', anchor="box-view", val=val, result=result_val,threaded=True)

@app.route('/timeSeries', methods=['GET', 'POST'])
def ts():
    temp, dew, humid, wd, ws, pressure  = predict(2)
    # time_data_2, temp_arr_2, dewp_2, humid_2, wind_dir_2, wind_speed_2, pressure_2 = new_data(predict(2))
    # time_data_3, temp_arr_3, dewp_3, humid_3, wind_dir_3, wind_speed_3, pressure_3 = new_data(predict(3))
    # time_data_4, temp_arr_4, dewp_4, humid_4, wind_dir_4, wind_speed_4, pressure_4 = new_data(predict(4))
    return render_template('timeseries.html', temp=temp, dew=dew, humid=humid, wd=wd, ws=ws, pressure=pressure)


@app.route('/landing', methods=['GET', 'POST'])
def landing():
    return render_template('landing.html')


def get_api_key():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config['openweathermap']['api']


def get_weather_data(zip_code, api_key):
    r = ''
    while r == '':
        try:
            api_url = "https://api.openweathermap.org/data/2.5/weather?zip={},us&appid={}".format(zip_code, api_key)
            r = requests.get(api_url)
            break
        except:
            print("Connection refused by the server..")
            print("Let me sleep for 5 seconds")
            time.sleep(5)
            print("Was a nice sleep, now let me continue...")
            continue
    return r.json()


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=8000)
