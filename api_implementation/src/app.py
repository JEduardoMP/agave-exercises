
import json
from flask import Flask, Response, jsonify
from flask_pymongo import PyMongo
from bson import json_util


app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost/flaskmongo'
mongo = PyMongo(app)


@app.route('/api/shopping-statistics', methods=['GET'])
def shopping_reciept():
  # Recieving all data
  data = mongo.db.flaskmongo.find()
  response = json_util.dumps(data)
  return Response(response, mimetype='application/json')


@app.route('/api/shopping-statistics/<category>', methods=['GET'])
def reciept_by_category(category):
  data = mongo.db.flaskmongo.find({'category': category})
  response = json_util.dumps(data)
  return Response(response, mimetype='application/json')
@app.errorhandler(404)
def not_found(error=None):
  response = jsonify({
    'message': 'The category is incorrect', 
    'status': 404
  })
  response.status_code = 404
  return response


def total_spend(price, qty, discount):
  subtotal = price * qty
  percentage = discount / 100
  dis = subtotal * percentage
  total = subtotal - dis
  return total


@app.route('/api/shopping-statistics/category/<category>', methods=['GET'])
def get_by_category(category):
  # Recieving specific data
  data = mongo.db.flaskmongo.find({'category': category})
  response = json_util.dumps(data)
  responseJson = json.loads(response)
  listPrice = []
  for articule in responseJson:
    price = articule['price']
    qty = articule['quantity']
    discount = articule['percentage_discount']
    total = total_spend(int(price), int(qty), int(discount))
    listPrice.append(total)
  count = 0
  for price in listPrice:
    count = count + price
  return {"category": count}
@app.errorhandler(404)
def not_found(error=None):
  response = jsonify({
    'message': 'The category is incorrect', 
    'status': 404
  })
  response.status_code = 404
  return response


if __name__ == '__main__':
    app.run(debug=True)
