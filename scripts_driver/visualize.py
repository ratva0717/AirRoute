import base64
import io
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


def plot_wind():
  # Function to perform visualization of weather data
    # wind speed vs month
    airport_df = pd.read_csv('scripts_driver/M1_final.csv')

    sns.set(style='darkgrid')
    fig, (ax1) = plt.subplots(nrows=1, figsize=(15, 8))
    sns.barplot(
        y='Wind Speed',
        x='MONTH',
        hue='DAY_OF_MONTH',
        data=airport_df,
        palette='light:#5A9'
    )
    ax1.set(ylabel="WIND SPEED",
            xlabel="DAY OF MONTHS")

    img = io.BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    return plot_url


def plot_pressure():
    airport_df = pd.read_csv('scripts_driver/M1_final.csv')
    # air pressure vs month
    sns.set(style='white')
    fig, ax = plt.subplots(nrows=1, figsize=(15, 8))
    sns.barplot(
        x='MONTH',
        y='Pressure',
        hue='DAY_OF_MONTH',
        data=airport_df,
        palette='flare',
    )
    ax.set(ylabel="AIR PRESSURE",
           xlabel="DAY OF MONTHS")
    img = io.BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    return plot_url


def plot_temp():
    airport_df = pd.read_csv('scripts_driver/M1_final.csv')
    # air pressure vs month
    sns.set(style='white')
    fig, ax = plt.subplots(nrows=1, figsize=(15, 8))
    sns.barplot(
        x='MONTH',
        y='Temperature',
        hue='DAY_OF_MONTH',
        data=airport_df,
        palette='pastel',
    )
    ax.set(ylabel="TEMPERATURE",
           xlabel="DAY OF MONTHS")
    img = io.BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    return plot_url


def plot_humidity():
    airport_df = pd.read_csv('scripts_driver/M1_final.csv')
    # air pressure vs month
    sns.set(style='white')
    fig, ax = plt.subplots(nrows=1, figsize=(15, 8))
    sns.barplot(
        x='MONTH',
        y='Humidity',
        hue='DAY_OF_MONTH',
        data=airport_df,
        palette='Set2',
    )
    ax.set(ylabel="HUMIDITY",
           xlabel="DAY OF MONTHS")
    img = io.BytesIO()
    plt.savefig(img, format='png')
    plt.close()
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')
    return plot_url
