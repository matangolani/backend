from flask import Flask, request
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
CORS(app, support_credentials = True)

@app.route('/enter', methods = ['POST'])
@cross_origin(supports_credentials = True)

def enter():
    hoursSlept   = request.form['hoursSlept']
    sleepQuality = request.form['sleepQuality']
    caffeineIn   = request.form['caffeineIn']

    dataFile = open("data.txt", "w")

    dataFile.write(f"{hoursSlept} {sleepQuality} {caffeineIn}")
    dataFile.close()

    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}

@app.route('/get', methods=['GET'])
def get_data():
    with open('data.txt', 'r') as file:
        data = file.read()
    return data

if __name__ == '__main__':
    app.run(debug = True)
