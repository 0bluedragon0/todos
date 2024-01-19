
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/hello")
def aaa():
    return render_template("index.html")

@app.route('/hello')
def bbb():
    return render_template('name_view.html')

#실행되는 url : 127.0.0.1:5000
app.run(debug=True)