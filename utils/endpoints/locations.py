import requests
import json
from resource.test_data import *
from utils.config import *
from resource.test_data import *


class Locations:
    @staticmethod
    def get_list(iso=None):
        r = requests.get(LOCATIONS_LIST_URL, headers=HEADERS)
        return r

    @staticmethod
    def get_all():
        r = requests.get(LOCATIONS_URL, headers=HEADERS)
        return r


    @staticmethod
    def post(data):
        return requests.post(LOCATIONS_URL, headers=HEADERS, data=json.dumps(data))

    @staticmethod
    def put(data, location_id):
        pass

    @staticmethod
    def delete(location_id):
        del_test = requests.delete(LOCATIONS_URL + location_id, headers=HEADERS)
        return del_test


if __name__ == "__main__":
    pass
<<<<<<< HEAD
=======

>>>>>>> Adding del method
