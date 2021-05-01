from flask import Flask, request, jsonify
import products_dao
import uom_dao
from sql_connection import get_sql_connection
import json
import orders_dao


app = Flask(__name__)
connection = get_sql_connection()



@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    responses = orders_dao.get_all_orders(connection)
    responses = jsonify(responses)
    responses.headers.add('Access-Control-Allow-Origin', '*')
    return responses


@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = orders_dao.insert_order(connection, request_payload)
    responses = jsonify({
        'order_id': order_id
    })
    responses.headers.add('Access-Control-Allow-Origin', '*')
    return responses



@app.route('/getProducts', methods=['GET'])
def get_products():
    products = products_dao.get_all_products(connection)
    responses = jsonify(products)
    responses.headers.add('Access-Control-Allow-Origin','*')
    return responses



@app.route('/getUOM', methods = ['GET'])
def get_uom():
    responses = uom_dao.get_uoms(connection)
    responses = jsonify(response)
    responses.headers.add('Access-Control-Allow-Origin','*')
    return responses



@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    return_id = products_dao.delete_product(connection, request.form['product_id'])
    responses = jsonify({
        'product_id': return_id
    })
    responses.headers.add('Access-Control-Allow-Origin', '*')
    return responses


@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = products_dao.insert_new_product(connection, request_payload)
    responses = jsonify({
        'product_id': product_id
    })
    responses.headers.add('Access-Control-Allow-Origin', '*')
    return responses


if __name__ == "__main__":
    print("Server Stared.")
    app.run(port=5000)