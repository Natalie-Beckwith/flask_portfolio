# import "packages" from flask
from flask import Flask, render_template, request

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

@app.route('/Binary/')
def Binary():
    return render_template("Binary.html")

@app.route('/Wireframes/')
def Wireframes():
    return render_template("Wireframes.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
