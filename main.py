from flask import Flask, render_template, request
from PIL import Image, ImageDraw
import numpy

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/Hassan/')
def Hassan():
    return render_template("Hassan.html")

@app.route('/Evan/')
def Evan():
    return render_template("Evan.html")

@app.route('/Abby/')
def Abby():
    return render_template("Abby.html")

@app.route('/Natalie/')
def Natalie():
    return render_template("Natalie.html")

@app.route('/Binary/', methods=['GET', 'POST'])
def Binary():
    return render_template("Binary.html")

@app.route('/Wireframes/')
def Wireframes():
    return render_template("Wireframes.html")

@app.route('/Journals/')
def Journals():
    return render_template("Journals.html")

@app.route('/rgb', methods=["GET", "POST"])
def rgb():
    return render_template('rgb.html', colors=color_data())



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
