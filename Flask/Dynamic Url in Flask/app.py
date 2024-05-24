# Dynamic URL
# Redirect is used to redirect the page to another page and url_for is used to give the url to the redirecting page
from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/success/<int:score>")
def success(score):
    return "Pass " + str(score)


@app.route("/fail/<int:score>")
def fail(score):
    return "Failed " + str(score)


# Result Checker


@app.route("/result/<int:marks>")
def result(marks):
    if marks > 50:
        result = "success"
    else:
        result = "fail"

    return redirect(url_for(result, score=marks))


if __name__ == "__main__":
    app.run(debug=True)  # Dynamic URL

from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/success/<int:score>")
def success(score):
    return "Pass " + str(score)


@app.route("/fail/<int:score>")
def fail(score):
    return "Failed " + str(score)


# Result Checker


@app.route("/result/<int:marks>")
def result(marks):
    if marks > 50:
        result = "success"
    else:
        result = "fail"

    return redirect(url_for(result, score=marks))


if __name__ == "__main__":
    app.run(debug=True)
