from flask import Flask, jsonify, request
from flask_cors import CORS

from google.oauth2 import id_token
from google.auth.transport import requests

import os

app = Flask(__name__)
CORS(app)

def google_aouth(token):
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), os.getenv("CLIENT_ID"))
        print(idinfo)
        if idinfo['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
            raise ValueError('しっぱいしたんだが？？？？？')
        return idinfo
    except ValueError as e:
        print(e)
        return None


@app.route('/oicjob/api/login',methods=["POST"])
def login():
    # print(request.headers)
    print(request.headers['Authorization'].split()[1])
    if request.headers['Content-Type'].lower() != 'application/json;charset=utf-8':
        return "dame"
    idinfo = google_aouth(request.headers['Authorization'].split()[1])
    if idinfo  is None:
        return "dame"
    return "ok"

@app.route('/oicjob/api/userinfo',methods=["GET"])
def get_user():
    idinfo = google_aouth(request.headers['Authorization'].split()[1])
    if idinfo  is None:
        return "dame"

    
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)