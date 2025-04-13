from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
# CORS open for all origins, TODO: restrict for security
CORS(app) 

@app.route('/api/message', methods=['POST'])
def get_message():
    data = request.get_json()
    PAT : str = data.get('PAT', '')
    return jsonify({"PAT": f"{PAT}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)