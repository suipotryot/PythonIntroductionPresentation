from DataHandler import DataHandler
from flask import Flask, jsonify, request
app = Flask(__name__)

data_handler = DataHandler()
data_handler.fetch_data()

@app.route('/')
def home():
    return "The Shire"

@app.route('/consumption/')
def consumption():
    name_list = [row[0] for row in data_handler.data if len(row) > 0]
    return jsonify(name_list)

@app.route('/consumption/<tool_name>/')
def consumption_of(tool_name):
    name_list = [row[0] for row in data_handler.data if len(row) > 0]
    if not tool_name in name_list:
        return "It's a 404 boy", 404
    found_row = data_handler.data[name_list.index(tool_name)]
    min_con, max_con = found_row[1:3]
    return jsonify({"min": min_con, "max": max_con})

@app.route('/calculate/<tool_name>/')
def calculate_consumption_of(tool_name):
    name_list = [row[0] for row in data_handler.data if len(row) > 0]
    if not tool_name in name_list:
        return "It's a 404 boy", 404
    found_row = data_handler.data[name_list.index(tool_name)]
    min_con, max_con = found_row[1:3]
    average = (int(min_con) + int(max_con)) / 2
    return jsonify(average * int(request.args.get('qtity')) * int(request.args.get('time')))
