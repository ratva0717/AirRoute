from flask import Flask, render_template, request
from scripts_driver.visualize import plot_wind, plot_temp

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    w_fig = plot_wind()
    t_fig = plot_temp()
    return render_template('index.html', ws_url=w_fig, tmp_url=t_fig)


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=8000)
