# 사용자의 요청에 응답하는 서버 개발 : 백엔드 + 화면
# 프레임워크 - 필요한 기능들을 부품화해서 조립하는 방식
# templates - html, static - css, js

from flask import Flask, render_template, request

app = Flask(__name__)

# 기능
# 배포서술자(deployment descriptor: 함수와 주소의 쌍)
@app.route("/hello")
def aaa():
    # 플라스크 함수의 리턴은 반드시 문자열
    return render_template("index.html")

# 어떤 작업을 하려면 화면을 보여준다(get) + 결과를 출력한다(post)
# 이름을 입력받아 출력
@app.route("/name", methods=['get'])
def name_input():
    return render_template("name_input.html")


@app.route("/name", methods=['post'])
def name_print():
    # get방식 요청 데이터 : request.args
    # post방식 요청 데이터 : request.form
    name = request.form["irum"]
    nai = request.form['nai']
    return render_template("name_result.html", name=name, nai=nai)


# 현재 서버의 모든 url을 출력하라
print(app.url_map)

#실행되는 url : 127.0.0.1:5000
app.run(debug=True)