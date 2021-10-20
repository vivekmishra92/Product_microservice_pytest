import requests
import json
from  data import Data
class Helper():

    def __init__(self):
        self._product_url = "http://localhost:3001/product"

    def post_product(self, data):

        headers = {'content-type': 'application/json'}
        try:
            response = requests.post(self._product_url, json=data, headers=headers)

            return response.status_code, response.json()
        except Exception as e:
            print(e)

    def get_all_product(self):
        try:
            response = requests.get(self._product_url)

            return response.status_code, response.json()
        except Exception as e:
            print(e)

    def get_product_by_id(self, product_id):

        url = f"{self._product_url}/{product_id}"
        try:
            response = requests.get(url)

            return response.status_code, response.json()
        except Exception as e:
            print(e)

    def update_product(self, product_id, updated_data):

        url = f"{self._product_url}/{product_id}"
        try:
            response = requests.put(url, json=updated_data)

            return response.status_code, response.json()
        except Exception as e:
            print(e)

    def delete_product(self, product_id):

        url = f"{self._product_url}/{product_id}"
        try:
            response = requests.delete(url)

            return response.status_code, response.json()
        except Exception as e:
            print(e)

if __name__ == "__main__":

    ob1 = Helper()
    print("--------------------")
    ob1.post_product(Data.add_valid_product)