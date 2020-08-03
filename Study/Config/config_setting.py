#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/1 16:54
# @Author  : baob
# @Site    : 
# @File    : config_setting.py
# @Software: PyCharm Community Edition

# 文件路径，其它文件调用，只会是当前目录的，?伤~
import os

Study_path = os.path.abspath(os.path.dirname(__file__))
# print(os.getcwd())   # 获取当前目录
# print(os.path.abspath(os.path.join(os.getcwd(), "..")))   # 获取上级目录
# print(os.path.abspath(os.path.join(os.getcwd(), "../..")))    # 获取上上级目录
# print(os.path.abspath(os.path.join(os.getcwd(), "../../..")))  # 获取上上上级目录

EXCEL_PATH = os.path.join(Study_path + "\Excel\\" + "data_info.xls")
# r'D:\\Study\\SAT\\Excel\\data_info.xls'
print(EXCEL_PATH)