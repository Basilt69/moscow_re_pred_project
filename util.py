import json
import pickle
import numpy as np
import sklearn


__locations = None
__data_columns = None
__model = None
__materials = None


def get_estimated_price(material, floor_number, floors_total, area_total, kitchen_area, location):
    try:
        loc_index = __data_columns.index(location.lower())
        material_index = __materials.index(material.lower())
    except:
        loc_index = -1
        material_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = floor_number
    x[1] = floors_total
    x[2] = area_total
    x[3] = kitchen_area

    if loc_index >= 0:
        x[loc_index] = 1

    if material_index >= 0:
        x[material_index] = 1

    return round(__model.predict([x])[0],2)


def get_location_names():
    return __locations


def get_material_names():
    return __materials


def load_saved_artifacts():
    print("loading saved artifacts ... start")
    global __data_columns
    global __locations
    global __materials

    with open("columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[12:]
        __materials = __data_columns[4:11]


    global __model
    with open("moscow_home_prices_lasso_model.pickle",'rb') as f:
        __model = pickle.load(f)
    print("loading saved artifacts ... done")


def get_data_columns():
    return __data_columns


if __name__ == '__main__':
    load_saved_artifacts()