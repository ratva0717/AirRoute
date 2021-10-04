import matplotlib.pyplot as plt
import seaborn as sns
import base64
import io
import pandas as pd
import sys
import matplotlib
matplotlib.use('Agg')

sns.set()

feature_keys = ['temp',
                'dewp',
                'humid',
                'wind_dir',
                'wind_speed',
                'pressure',
                'time_hour']

data = pd.read_csv('scripts_driver\Hourly_weather_data.csv')
data = data[feature_keys]

def draw_plot(val):
    plt.rcParams["figure.figsize"] = (20,12)
    data.plot(x='time_hour', y = val )
    plt.show()
    img = io.BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    return plot_url
