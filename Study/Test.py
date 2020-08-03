#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/1 18:14
# @Author  : baob
# @Site    : 
# @File    : Test.py
# @Software: PyCharm Community Edition

import xlrd

# xd = xlrd.open_workbook('D:\Study\SAT\Study\Excel\data_info.xls')
# table = xd.sheets()[0]
# rows = table.nrows
# print(table.row_values(1))
# print(table.col_values(1))
# for i in range(rows):
#     print(table.nrow_values(i))

def function(*args, **kwargs):
    print(*args, **kwargs)

a = (2,3)
b = ['s', 'z']
c = {'a':1, 'b': 2}
function(a, c)
function(b, c)
