# coding:utf-8
"""
功能：超级大乐透后端路由
作者：DX3906 993628121@qq.com
"""

from flask_cors import CORS
from flask import Flask

app = Flask(__name__)
cors = CORS(app)


@app.route('/')
def index():
    return "hello"


if __name__ == '__main__':
    app.run(debug=True)
