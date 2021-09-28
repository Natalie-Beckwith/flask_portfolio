from flask import Flask, render_template, request
from PIL import Image, ImageDraw
import numpy

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/Hassan/', methods=['GET', 'POST'])
def Hassan():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Hassan.html", name=name)
    # starting and empty input default
    return render_template("Hassan.html", name="User")

@app.route('/Evan/', methods=['GET', 'POST'])
def Evan():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Evan.html", name=name)
    # starting and empty input default
    return render_template("Evan.html", name="User")

@app.route('/Abby/', methods=['GET', 'POST'])
def Abby():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Abby.html", name=name)
    # starting and empty input default
    return render_template("Abby.html", name="User")

@app.route('/Natalie/', methods=['GET', 'POST'])
def Natalie():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Natalie.html", name=name)
    # starting and empty input default
    return render_template("Natalie.html", name="World")

@app.route('/Binary/', methods=['GET', 'POST'])
def Binary():
    bitWidth = 8;
    if request.form:
        bitWidthText = request.form.get("bitWidth")
        if len(bitWidthText) != 0:  # input field has content
            bitWidth = int (bitWidthText)
            return render_template("Binary.html", BITS=bitWidth, imgBulbOn="/static/assets/bulbon.png", imgBulbOff="/static/assets/bulboff.png")

    # starting and empty input default
    return render_template("Binary.html", BITS= bitWidth, imgBulbOn="/static/assets/bulbon.png", imgBulbOff="/static/assets/bulboff.png")

@app.route('/Wireframes/')
def Wireframes():
    return render_template("Wireframes.html")

@app.route('/overview/')
def overview():
    return render_template("overview.html")

@app.route('/Journals/')
def Journals():
    return render_template("Journals.html")


@app.route('/rgb/', methods=["GET", "POST"])
def rgb():
    return render_template("rgb.html", name="World")


@app.route('/greet/', methods=['GET', 'POST'])
def greet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("greet.html", name=name)
    # starting and empty input default
    return render_template("greet.html", name="World")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
