# import "packages" from flask
from flask import Flask, render_template

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render kangaroos.html
@app.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")


@app.route('/walruses/')
def walruses():
    return render_template("walruses.html")


@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")



@app.route('/Abby/')
def Abby():
    return render_template("Abby.html")



@app.route('/Evan/')
def Evan():
    return render_template("Evan.html")


@app.route('/Natalie/')
def Natalie():
    return render_template("Natalie.html")


@app.route('/Hassan/')
def Hassan():
    return render_template("Hassan.html")

# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
