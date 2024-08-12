from flask import Flask, jsonify
import json
from urllib.parse import quote as url_quote


app = Flask(__name__)

data_storage = {}

mock_data = [
    {"name": "Kangaroo", "type": "Mammal"},
    {"name": "Camel", "type": "Mammal"},
    {"name": "Lion", "type": "Mammal"},
    {"name": "Giraffe", "type": "Mammal"}
]

def process_data(data):
    return [{key: value.upper() if isinstance(value, str) else value for key, value in item.items()} for item in data]

@app.route('/fetch-data', methods=['GET'])
def fetch_data():
    global data_storage
    processed_data = process_data(mock_data)
    data_storage['data'] = processed_data
    return jsonify({"message": "Data fetched and processed", "data": processed_data})

@app.route('/get-processed-data', methods=['GET'])
def get_processed_data():
    if 'data' in data_storage:
        return jsonify(data_storage['data'])
    else:
        return jsonify({"message": "No data available"}), 404

if __name__ == '__main__':
    app.run(debug=True)