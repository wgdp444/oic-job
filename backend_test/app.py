from flask import Flask, jsonify, request
from flask_cors import CORS

from google.oauth2 import id_token
from google.auth.transport import requests

import os

app = Flask(__name__)
CORS(app)

@app.route('/oicjob/api/oauth/login',methods=["POST"])
def test():
    print(request.headers['Content-Type'])
    if request.headers['Content-Type'] != 'application/json;charset=UTF-8':
        print(request.headers['Content-Type'])
        return "dame"
    try:
        data = request.get_json()
        idinfo = id_token.verify_oauth2_token(data['id_token'], requests.Request(), os.getenv("CLIENT_ID"))

        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('しっぱいしたんだが？？？？？')
        print(idinfo)
        return 'ok'
    except ValueError as e:
        print(e)
        return "dame"
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)