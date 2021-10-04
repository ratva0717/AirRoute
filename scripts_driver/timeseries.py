import pickle
from statsmodels.tsa.vector_ar.var_model import VAR
import pandas as pd
import matplotlib.pyplot  as plt
import base64
import io

def predict(val):
    d = {}
    t_arr = []
    d_arr = []
    h_arr = []
    ws=[]
    wd = []
    pressure = []
    model_fit = pickle.load(open('model_ts.pkl','rb'))
    yhat = model_fit.forecast(model_fit.y, steps=val)
    for i in range(len(yhat)):
        for j in range(len(yhat[0])):
            if j == 0:
                t_arr.append(yhat[i][j])
            elif j == 1:
                d_arr.append(yhat[i][j])
            elif j == 2:
                h_arr.append(yhat[i][j])
            elif j == 3:
                wd.append(yhat[i][j])
            elif j == 4:
                ws.append(yhat[i][j])
            else:
                pressure.append(yhat[i][j])
    d['temp'] = t_arr
    d['dewp'] = d_arr
    d['humid'] = h_arr
    d['wind_dir'] = wd
    d['wind_speed'] = ws
    d['pressure'] = pressure
    return d



    

