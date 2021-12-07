import pickle
from statsmodels.tsa.vector_ar.var_model import VAR
import pandas as pd
import matplotlib.pyplot  as plt
import base64
import io


df = pd.read_csv('scripts_driver\last_24.csv')
temp = df['temp'].values.tolist()
dew = df['dewp'].values.tolist()
humid = df['humid'].values.tolist()
winddirection = df['wind_dir'].values.tolist()
windspeed = df['wind_speed'].values.tolist()
pressure = df['pressure'].values.tolist()
y = 2
def predict(val):
    t_arr = []
    d_arr = []
    h_arr  = []
    ws = []
    wd = []
    press = []
    model_fit = pickle.load(open('model_ts.pkl','rb'))
    yhat = model_fit.forecast(y = model_fit.y, steps=val)
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
                press.append(yhat[i][j])
    temp.extend(t_arr)
    dew.extend(d_arr)
    humid.extend(h_arr)
    winddirection.extend(wd)
    windspeed.extend(ws)
    pressure.extend(pressure)
    
    return temp, dew, humid, winddirection, windspeed, pressure



    

