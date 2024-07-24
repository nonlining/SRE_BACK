import sys
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/get_options', methods=['GET'])
def get_options():
    options = ['Option 1', 'Option 2', 'Option 3']
    return jsonify(options=options)

if __name__ == '__main__':
    
    app.run(debug=True)