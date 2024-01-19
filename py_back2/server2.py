from flask import Flask, request,render_template

app = Flask(__name__)

@app.route("/city", methods=['get'])
def city_input():
    return render_template("city_input.html")

@app.route("/city", methods=['post'])
def city_print():
    name = request.form['irum']
    city = request.form['city']
    return render_template("city_result.html", name=name, city=city)

app.run()