#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/26 21:24
# @Author  : baob
# @Site    : 
# @File    : d1.py
# @Software: PyCharm Community Edition


from flask import Flask
from flask import render_template
from flask import redirect
from flask import send_file

# 实例化flask
app = Flask(__name__)

# 视图函数修饰器
@app.route('/index')
# 方法名称需与路由一致index
def index():
    return "hello world"

# 访问xxhtml文件
@app.route('/home')
def home():
    # 默认存放路径是templates,所以home.html的路径会被自动加载
    return render_template('home.html')

# 重定向至home页面，访问/re会显示302重定向
@app.route('/re')
def re():
    return redirect('home')

# 快速导入模块：输入木块后鼠标选中，alt +　回车键
# os

# 获取文件中内容
@app.route('/get_file')
def get_file():
    return send_file("d1.py")


if __name__ == "__main__":
    app.run(debug=True)