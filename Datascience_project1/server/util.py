import json
import pickle

import numpy as np

__location=None
__model=None
__data_columns=None

def get_estimated_price(location,sqft,bath,bhk):
    try:
        loc_index=__data_columns.index(location.lower())
    except:
        loc_index=-1

    x=np.zeros(len(__data_columns))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk
    if loc_index >=0:
        x[loc_index]=1
    return round(__model.predict([x])[0],2)

def get_location_names():
    return __location

def load_saved_artifacts():
    print("loading saved artifacts...")
    global __location
    global __data_columns
    global __model

    with open("server\\artifacts\\columns.json", "rb") as f:
        __data_columns = json.load(f)['data_columns']
        __location = __data_columns[3:]

    with open ('server\\artifacts\\banglalore_price_detection model.pickle', 'rb') as f:
        __model= pickle.load(f)

    print("loading artifacts are done...")



if __name__=='__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('devarabeesana halli',1000,2,2))
    print(get_estimated_price('1st phase jp nagar',1000,2,2))
    print(get_estimated_price('indira nagar',1000,2,2))
    print(get_estimated_price('1st phase jp nagar',1000,3,3))