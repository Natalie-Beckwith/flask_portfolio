import requests
from flask import Flask, render_template, request
from pathlib import Path  # https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f

app = Flask(__name__)

# connects default URL to render index.html`
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

@app.route('/greet/', methods=['GET', 'POST'])
def greet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("greet.html", name=name)
    # starting and empty input default
    return render_template("greet.html", name="World")

@app.route('/rgb/', methods=["GET", "POST"])
def rgb():
    path = Path(app.root_path) / "static" / "img"
    from algorithm.image import image_data
    return render_template('rgb.html', images=image_data(path))

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/logicGates/')
def logicGates():
    return render_template("logicGates.html")

@app.route('/map/')
def map():
    return render_template("map.html")

@app.route('/colorCodes/')
def colorCodes():
    return render_template("colorCodes.html")

@app.route('/joke', methods=['GET', 'POST'])
def joke():
    """
    # use this url to test on and make modification on you own machine
    url = "http://127.0.0.1:5222/api/joke"
    """
    url = "https://csp.nighthawkcodingsociety.com/api/joke"
    response = requests.request("GET", url)
    return render_template("joke.html", joke=response.json())

@app.route('/jokes', methods=['GET', 'POST'])
def jokes():
    """
    # use this url to test on and make modification on you own machine
    url = "http://127.0.0.1:5222/api/jokes"
    """
    url = "https://csp.nighthawkcodingsociety.com/api/jokes"

    response = requests.request("GET", url)
    return render_template("starter/jokes.html", jokes=response.json())

@app.route('/geolocation/')
def geolocation():
    return render_template("geolocation.html")

@app.route('/temp/')
def temp():
    return render_template("temp.html")

if __name__ == "__main__":
    app.run(debug=True)
#anything after this line will not work