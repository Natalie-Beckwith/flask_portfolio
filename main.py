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
            return render_template("About Us/Hassan.html", name=name)
    # starting and empty input default
    return render_template("About Us/Hassan.html", name="User")

@app.route('/Evan/', methods=['GET', 'POST'])
def Evan():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("About Us/Evan.html", name=name)
    # starting and empty input default
    return render_template("About Us/Evan.html", name="User")

@app.route('/Abby/', methods=['GET', 'POST'])
def Abby():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("About Us/Abby.html", name=name)
    # starting and empty input default
    return render_template("About Us/Abby.html", name="User")

@app.route('/Natalie/', methods=['GET', 'POST'])
def Natalie():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("About Us/Natalie.html", name=name)
    # starting and empty input default
    return render_template("About Us/Natalie.html", name="World")

@app.route('/Binary/', methods=['GET', 'POST'])
def Binary():
    bitWidth = 8;
    if request.form:
        bitWidthText = request.form.get("bitWidth")
        if len(bitWidthText) != 0:  # input field has content
            bitWidth = int (bitWidthText)
            return render_template("Minilabs/Binary.html", BITS=bitWidth, imgBulbOn="/static/assets/bulbon.png", imgBulbOff="/static/assets/bulboff.png")

    # starting and empty input default
    return render_template("Minilabs/Binary.html", BITS= bitWidth, imgBulbOn="/static/assets/bulbon.png", imgBulbOff="/static/assets/bulboff.png")

@app.route('/Wireframes/')
def Wireframes():
    return render_template("Minilabs/Wireframes.html")

@app.route('/overview/')
def overview():
    return render_template("overview.html")

@app.route('/Journals/')
def Journals():
    return render_template("Minilabs/Journals.html")

@app.route('/greet/', methods=['GET', 'POST'])
def greet():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Minilabs/greet.html", name=name)
    # starting and empty input default
    return render_template("Minilabs/greet.html", name="World")

@app.route('/rgb/', methods=["GET", "POST"])
def rgb():
    path = Path(app.root_path) / "static" / "img"
    from algorithm.image import image_data
    return render_template('Minilabs/rgb.html', images=image_data(path))

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/logicGates/')
def logicGates():
    return render_template("Minilabs/logicGates.html")

@app.route('/tempconditionals/')
def tempconditionals():
    return render_template("Projects/tempconditionals.html")

@app.route('/map/')
def map():
    return render_template("Projects/map.html")

@app.route('/covidapi/')
def covidapi():
    return render_template("API/covidapi.html")


@app.route('/colorCodes/')
def colorCodes():
    return render_template("Minilabs/colorCodes.html")

@app.route('/joke', methods=['GET', 'POST'])
def joke():
    """
    # use this url to test on and make modification on you own machine
    url = "http://127.0.0.1:5222/api/joke"
    """
    url = "https://csp.nighthawkcodingsociety.com/api/joke"
    response = requests.request("GET", url)
    return render_template("API/joke.html", joke=response.json())

@app.route('/jokes', methods=['GET', 'POST'])
def jokes():
    """
    # use this url to test on and make modification on you own machine
    url = "http://127.0.0.1:5222/api/jokes"
    """
    url = "https://csp.nighthawkcodingsociety.com/api/jokes"

    response = requests.request("GET", url)
    return render_template("API/starter/jokes.html", jokes=response.json())

@app.route('/geolocation/')
def geolocation():
    return render_template("API/geolocation.html")

@app.route('/temp/')
def temp():
    return render_template("Projects/temp.html")

@app.route('/dnhsMapBuildings/admin')
def admin():
    return render_template("/dnhsMapBuildings/admin.html")

@app.route('/dnhsMapBuildings/basketball')
def basketball():
    return render_template("/dnhsMapBuildings/basketball.html")

@app.route('/dnhsMapBuildings/buildingA')
def buildingA():
    return render_template("/dnhsMapBuildings/buildingA.html")

@app.route('/dnhsMapBuildings/buildingBGym')
def buildingBGym():
    return render_template("/dnhsMapBuildings/buildingBGym.html")

@app.route('/dnhsMapBuildings/buildingD')
def buildingD():
    return render_template("/dnhsMapBuildings/buildingD.html")

@app.route('/dnhsMapBuildings/buildingE')
def buildingE():
    return render_template("/dnhsMapBuildings/buildingE.html")

@app.route('/dnhsMapBuildings/buildingG')
def buildingG():
    return render_template("/dnhsMapBuildings/buildingG.html")

@app.route('/dnhsMapBuildings/buildingJ')
def buildingJ():
    return render_template("/dnhsMapBuildings/buildingJ.html")

@app.route('/dnhsMapBuildings/buildingK')
def buildingK():
    return render_template("/dnhsMapBuildings/buildingK.html")

@app.route('/dnhsMapBuildings//buildingL')
def buildingL():
    return render_template("/dnhsMapBuildings/buildingL.html")

@app.route('/dnhsMapBuildings/buildingM')
def buildingM():
    return render_template("/dnhsMapBuildings/buildingM.html")

@app.route('/dnhsMapBuildings/buildingN')
def buildingN():
    return render_template("/dnhsMapBuildings/buildingN.html")

@app.route('/dnhsMapBuildings/buildingP')
def buildingP():
    return render_template("/dnhsMapBuildings/buildingP.html")

@app.route('/dnhsMapBuildings/buildingR')
def buildingR():
    return render_template("/dnhsMapBuildings/buildingR.html")

@app.route('/dnhsMapBuildings/foodService')
def foodService():
    return render_template("/dnhsMapBuildings/foodService.html")

@app.route('/dnhsMapBuildings/library')
def library():
    return render_template("/dnhsMapBuildings/library.html")

@app.route('/dnhsMapBuildings/quad')
def quad():
    return render_template("/dnhsMapBuildings/quad.html")

@app.route('/dnhsMapBuildings/stadium')
def stadium():
    return render_template("/dnhsMapBuildings/stadium.html")

@app.route('/dnhsMapBuildings/tennis')
def tennis():
    return render_template("/dnhsMapBuildings/tennis.html")

if __name__ == "__main__":
    app.run(debug=True)
#anything after this line will not work