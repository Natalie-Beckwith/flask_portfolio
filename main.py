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

@app.route('/Abby/')
def Abby():
    return render_template("Abby.html")

@app.route('/Evan', methods=['GET', 'POST'])
def Evan():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Evan.html", name=name)
    # starting and empty input default
    return render_template("Natalie.html", name="World")

@app.route('/Natalie/', methods=['GET', 'POST'])
def Natalie():
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Natalie.html", name=name)
    # starting and empty input default
    return render_template("Natalie.html", name="World")

@app.route('/greet', methods=['GET', 'POST'])
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
