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

@app.route('/oicjob/api/create_account',methods=["POST"])
def test2():
    print(request.headers['Content-Type'])
    if request.headers['Content-Type'] != 'application/json;charset=UTF-8':
        print(request.headers['Content-Type'])
        return "dame"
    try:
        return 'ok'
    except ValueError as e:
        print(e)
        return "dame"

@app.route('/oicjob/api/getsubject',methods=["GET"])
def test3():
    test5 = ["情報スペシャリスト","情報システム","ゲームクリエイター","医療福祉事務","診療情報管理士","ホテル・ブライダル","経営アシスト","公務員","保育"]
    return jsonify(test5)
@app.route('/oicjob/api/getclass',methods=["GET"])
def test4():
    test6 = ["なし","1","2","3","4"]
    return jsonify(test6)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)