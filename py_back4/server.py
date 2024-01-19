from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/weather", methods=['get'])
def month_input():
    return render_template("/start.html", type=str)

@app.route('/weather', methods=['post'])
def month_print():
    month = request.form.get('month',type=int)
    season = '겨울'
    weather_color = "winter"
    if 3<= month and month<=5:
        season='봄'
        weather_color = "spring"
    elif 6<= month <= 8:
        season = "여름"
        weather_color = "summer"
    elif 9<=month < 11:
        season = "가을"
        weather_color = "autumn"
    return render_template("/wait.html",season=season, weather_color=weather_color)


app.run()