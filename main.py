# import "packages" from flask
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

def color_data(path="static/", color_dict=None):  # path of blueprint run is default
    # prefill with label and file
    if color_dict is None:
        color_dict = [
            {'source': "Peter Carolin", 'label': "Lassen Volcano", 'file': "lassen-volcano-256.jpg"},
            {'source': "iconsdb.com", 'label': "Black square", 'file': "black-square-16.png"},
            {'source': "iconsdb.com", 'label': "Red square", 'file': "red-square-16.png"},
            {'source': "iconsdb.com", 'label': "Green square", 'file': "green-square-16.png"},
            {'source': "iconsdb.com", 'label': "Blue square", 'file': "blue-square-16.png"},
            {'source': "iconsdb.com", 'label': "White square", 'file': "white-square-16.png"},
            {'source': "iconsdb.com", 'label': "Blue square", 'file': "blue-square-16.jpg"}
        ]
    # calculate attributes of image
    for color in color_dict:
        file = path + color['file']
        image_reference = Image.open(file)
        image_data = image_reference.getdata()
        color['format'] = image_reference.format
        color['mode'] = image_reference.mode
        color['size'] = image_reference.size
        color['data'] = numpy.array(image_data)
        color['hex_array'] = []
        color['binary_array'] = []
        for code in color['data']:
            hex_value = hex(code[0])[-2:] + hex(code[1])[-2:] + hex(code[2])[-2:]
            hex_value = hex_value.replace("x", "0")
            color['hex_array'].append("#" + hex_value)
            bin_value = bin(int('1' + hex_value, 16))[3:]
            color['binary_array'].append("0b" + bin_value)
    return color_dict


if __name__ == "__main__":
    local_path = "static/"
    color_test = [
        {'source': "Peter Carolin", 'label': "Lassen Volcano", 'file': "lassen-volcano-256.jpg"},
        {'source': "Peter Carolin", 'label': "Lassen Volcano", 'file': "lassen-volcano-original.jpg"},
    ]
    colors = color_data(local_path, color_test)  # path of local run
    for row in colors:
        # summarize some details about the image
        print(row['label'])
        print(row['format'])
        print(row['mode'])
        print(row['size'])
        print(row['data'])
        print(row['hex_array'])
        print(row['binary_array'])
        filename = local_path + row['file']
        image_ref = Image.open(filename)
        draw = ImageDraw.Draw(image_ref)
        draw.text((0, 0), "Size is {0} X {1}".format(*row['size']))
        image_ref.show()
print()

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
