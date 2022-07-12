# coding:utf-8
"""
功能：  超级大乐透后端路由
作者：  DX3906 993628121@qq.com
"""

from flask_cors import CORS
from flask import Flask, render_template
# import json
from gevent import pywsgi

from source import number_res, log_get
# from source import htmls

app = Flask(__name__)
cors = CORS(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/lottery')
def lottery():
    res1, res2 = number_res.number_res_get()
    # res = ""
    head = "<header><h1 align='center'><font style='font-size: 55px'>大乐透预测（简易版）</font></h1>"
    number1 = res1['号码']
    front_area = " ".join(number1[0]['前区'])
    back_area = " ".join(number1[0]['后区'])
    p1 = "<p>前区：{}</p><p>后区：{}</p><p>原则：{}</p><p>期数：{}</p>".format(
        front_area, back_area, "最小中奖次数原则", res1['基于的期数'])
    number2 = res2['号码']
    front_area = " ".join(number2['前区'])
    back_area = " ".join(number2['后区'])
    p2 = "<p>前区：{}</p><p>后区：{}</p><p>原则：{}</p><p>期数：{}</p><p>总金额：{}</p>".format(
        front_area, back_area, "最小中奖次数原则", res2['基于的期数'], res2["此号码中将总金额"])

    # res = json.dumps({'res1': res1, 'res2': res2})
    # res1 = json.dumps(res1)
    # res2 = json.dumps(res2)
    res = head + "<body>" + p1 + "<p>---------------</p>" + p2 + "</body>"

    return res


@app.route('/log')
def log():
    data = log_get.log_get()
    res = ''
    for item in data:
        res += '<p>' + item + '</p>'

    return res


if __name__ == '__main__':
    server = pywsgi.WSGIServer(('0.0.0.0', 23333), app)
    server.serve_forever()
