from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('admin')
def admin():
    return render_template("admin.html")

@app.route('basketball')
def basketball():
    return render_template("basketball.html")

@app.route('buildingA')
def buildingA():
    return render_template("buildingA.html")

@app.route('buildingBGym')
def buildingBGym():
    return render_template("buildingBGym.html")

@app.route('buildingD')
def buildingD():
    return render_template("buildingD.html")

@app.route('buildingE')
def buildingE():
    return render_template("buildingE.html")

@app.route('buildingG')
def buildingG():
    return render_template("buildingG.html")

@app.route('buildingJ')
def buildingJ():
    return render_template("buildingJ.html")

@app.route('buildingK')
def buildingK():
    return render_template("buildingK.html")

@app.route('buildingL')
def buildingL():
    return render_template("buildingL.html")

@app.route('buildingM')
def buildingM():
    return render_template("buildingM.html")

@app.route('buildingN')
def buildingN():
    return render_template("buildingN.html")

@app.route('buildingP')
def buildingP():
    return render_template("buildingP.html")

@app.route('buildingR')
def buildingR():
    return render_template("buildingR.html")

@app.route('foodService')
def foodService():
    return render_template("foodService.html")

@app.route('library')
def library():
    return render_template("library.html")

@app.route('quad')
def quad():
    return render_template("quad.html")

@app.route('/stadium/')
def stadium():
    return render_template("stadium.html")

@app.route('tennis')
def tennis():
    return render_template("tennis.html")
