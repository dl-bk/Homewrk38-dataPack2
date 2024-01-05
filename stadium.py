# До вже реалізованого класу «Стадіон» додайте можливість
# стиснення та розпакування даних з використанням json та
# pickle.

from datetime import datetime
import json
import pickle
import gzip

FILE_JSON = "stadium.json"
FILE_PKL = "stadium.pkl.gz"

class Stadium:
    def __init__(self, name, op_date, country, city, capacity) -> None:
        self.name = name
        self.op_date = op_date
        self.country = country
        self.city = city
        self.capacity = capacity
    



def save_data_pickle(lst):
    dict_obj = []
    for el in lst:
        dct_el = obj_to_dict(el)
        dict_obj.append(dct_el)
    with gzip.open(FILE_PKL, 'wb') as wfile:
        pickle.dump(dict_obj, wfile)
        print("data saved")

def load_data_pickle():
    try:
        with gzip.open(FILE_PKL, 'rb') as rfile:
            data = pickle.load(rfile)
    except FileNotFoundError:
        return None
    return data

def save_data_json(lst):
    dict_obj = []
    for el in lst:
        dct_el = obj_to_dict(el)
        dict_obj.append(dct_el)

    with open(FILE_JSON, 'w') as wfile:
        json.dump(dict_obj, wfile, indent=4)
        print("data saved")

def load_data_json():
    try:
        with open(FILE_JSON, 'r') as rfile:
            data = json.load(rfile)
    except FileNotFoundError:
        return None
    return data

def obj_to_dict(obj) -> dict:
    return obj.__dict__


stadiums = [Stadium("Name", "01.01.2000", "someCountry", "someCity", 5000),
            Stadium("Name2", "01.01.1999", "someCountry2", "someCity2", 8000)]

save_data_json(stadiums)
data = load_data_json()
print(data)

save_data_pickle(stadiums)
data_pkl = load_data_pickle()
print(data_pkl)