from flask import Flask, render_template, request
from scripts_driver.visualize import plot_wind, plot_temp, plot_pressure, plot_humidity
from scripts_driver.svm_model import *
from scripts_driver.NB_model import *
import pickle
import pandas as pd

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    #visualization
    w_fig = plot_wind()
    t_fig = plot_temp()
    p_fig = plot_pressure()
    h_fig = plot_humidity()
    #model
    # svm = predict()

    #Performence
    NB_Accuracy, NB_Precision, NB_Recall = NB_PredictionMeasure()
    SVM_Accuracy, SVM_Precision, SVM_Recall = SVM_PredictionMeasure()

    return render_template('index.html', ws_url=w_fig, tmp_url=t_fig, p_url=p_fig, h_url=h_fig,
                           NB_Accuracy = NB_Accuracy, NB_Precision = NB_Precision, NB_Recall = NB_Recall,
                           SVM_Accuracy = SVM_Accuracy, SVM_Precision = SVM_Precision, SVM_Recall = SVM_Recall)


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8000)
