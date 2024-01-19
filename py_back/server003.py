from flask import Flask, request, render_template
import datetime
app = Flask(__name__)

# 태어난 연도를 입력받아 나이를 출력
# 년도를 입력하는 화면
@app.route("/nai_view")
def nai_view():
    return render_template("nai_view.html")

#결과를 출력하는 화면
@app.route("/nai_result")
def nai_result():
    this_year = datetime.datetime.now().year
    birth_year = int(request.args['birth_year'])
    nai = this_year - birth_year
    return render_template("nai_result.html", nai=nai)

app.run()

#200 -성공 -> 오류가 없음
# 400 - 잘못된 요청(작업 시작 x)
# 403 - 권한 없음
# 404- not found
# 405 - method 오류(get/post)
# 500 - 작업 중 오류