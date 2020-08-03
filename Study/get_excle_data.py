#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/1 16:45
# @Author  : baob
# @Site    : 
# @File    : get_excle_data.py
# @Software: PyCharm Community Edition

import xlrd
import os


class Get_Excel_Data(object):

    def __init__(self,excel_path=None, excel_index=None):
        if excel_path == None:
            excel_path = os.path.join('D:\Study\SAT\Study\Excel\data_info.xls')
            print(excel_path)
        if excel_index == None:
            excel_index = 0
        # 打开excle
        self.data = xlrd.open_workbook(excel_path)
        # 打开指定sheet
        self.table = self.data.sheets()[excel_index]
        # 获取sheet中有数据的行数
        self.rows = self.table.nrows

    def excel_data(self):
        excel_data_lst = []
        # 根据行数进行循环遍历
        print(self.rows)
        if self.rows > 0:
            for i in range(1, self.rows):
                # 获取指定行数据，返回的数据类型：list
                # 错误的把self.table.row_values(i)写成了self.table.row_values[i]
                row_values = self.table.row_values(i)
                # 把返回的行数据追加至excel_data_lst中
                excel_data_lst.append(row_values)
            return excel_data_lst
        return None


if __name__ == '__main__':
    ged = Get_Excel_Data()
    print(ged.excel_data())
