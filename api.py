from flask import Flask, request, render_template
import openweather as opw

app = Flask(__name__)
APP_ID = "a453aba51ddf22fa57d0973144ce1e41"

@app.route('/')
def home():
    return render_template("homepage.html")

@app.route('/data_page', methods = ["GET", "POST"])
def data():
    if request.method == 'POST':
        option = request.form['options']
        global option
        if option == 'name':
            return render_template("data_page.html")
        elif option == 'pin':
            return render_template("data_page_pin.html")
        elif option == 'Coordinates':
            return render_template("data_page_coords.html")

@app.route('/city_results', methods = ['GET', 'POST'])
def result():

    if request.method == 'POST':
        data = request.form['info']

        units = request.form['units']

        if option == 'name':
            
            info = opw.city(data, None, units)
            return str(info)

        elif option == 'pin':

            info = opw.city(data, 'zip', units)
            return str(info)

        else:

            info = opw.city(data, 'coords', units)
            return str(info)


if __name__ == '__main__':
    app.run(debug = True)


