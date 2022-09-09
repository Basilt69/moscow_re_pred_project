from flask import Flask, request, jsonify
from flask_cors import CORS
import util
import gunicorn

app = Flask(__name__)
CORS(app)

@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/get_material_names', methods=['GET'])
def get_material_names():
    response = jsonify({
        'materials':util.get_material_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/get_data_columns', methods=['GET'])
def get_data_columns():
    response = jsonify({
        'data_columns':util.get_data_columns()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict_home_price/', methods=['GET', 'POST'])
def predict_home_price():
    material = request.form['material']
    floor_number = int(request.form['floor_number'])
    floors_total = int(request.form['floors_total'])
    area_total = float(request.form['area_total'])
    kitchen_area = float(request.form['kitchen_area'])
    location = request.form['location']

    response = jsonify({'estimated_price': util.get_estimated_price(material, floor_number, floors_total,
                                                                    area_total, kitchen_area, location)})
    #response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add_header('Access-Control-Allow-Origin','*')
    return response


if __name__ == "__main__":
    print("Starting Python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()