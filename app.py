from flask import Flask, render_template, request
from flatlib.chart import Chart
from flatlib.datetime import Datetime
from flatlib.geopos import GeoPos
from flatlib import const

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    chart_data = None
    if request.method == 'POST':
        name = request.form.get('name')
        date = request.form.get('date')
        time = request.form.get('time')
        lat = request.form.get('lat')
        lon = request.form.get('lon')

        dt = Datetime(date, time, '+03:00')
        pos = GeoPos(lat, lon)
        chart = Chart(dt, pos, hsys=const.HOUSES_WHOLE_SIGN)

        chart_data = [(obj, chart.get(obj).sign, chart.get(obj).lon) for obj in chart.objects]

    return render_template('index.html', chart=chart_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)