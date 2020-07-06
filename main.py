#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/6 5:30 PM
# @Author  : Jinlin From Meixin
# @File    : main.py
# @Project : ble-telemetry-https

from flask import Flask, request
import  json

app = Flask(__name__)


@app.route('/auth', methods=['POST'])
def f_data():
    if request.method == 'POST':
        payload = {'access_token':'123456','api_url':'http://192.168.1.100:6666/data'}
        return json.dumps(payload)
    else:
        abort(405)


@app.route('/data', methods=['POST'])
def save_data():
    f = open('data.txt','a')
    f.write(json.dumps(request.json) + '\n')

    f.close()
    status = {'meta':{'version':1},'status':{'code':200,'description':'OK'}}
    return json.dumps(status)

@app.route('/')
def index():
    return 'Customer is first,Customer is last!'


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=6666,debug=True)

