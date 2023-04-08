from flask import Flask
from flask_restful import Api, Resource
from parsel import Selector

import json

import requests

app = Flask(__name__)
api= Api(app)

def find_json_objects(text: str, decoder=json.JSONDecoder()):
    """Find JSON objects in text, and generate decoded JSON data"""
    pos = 0
    while True:
        match = text.find("{", pos)
        if match == -1:
            break
        try:
            result, index = decoder.raw_decode(text[match:])
            yield result
            pos = match + index
        except ValueError:
            pos = match + 1

def getProductData(productId: str):
    headers = {'Accept-Encoding': 'identity'}
    response = requests.get("https://www.sodimac.com.br/sodimac-br/product/" + productId, headers=headers)
    # print(response.text)

    selector = Selector(response.text)
    
    script_text = selector.css("#__NEXT_DATA__::text").get()

    return list(find_json_objects(text=script_text))


class GetProduct(Resource):
    def get(self, id):
        return {"data": getProductData(id)}


api.add_resource(GetProduct, "/product/<string:id>")

if __name__ == '__main__':
    app.run(port=5000)