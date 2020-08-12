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
            self.excel_path = os.path.join('D:\Study\SAT\Study\Excel\data_info.xls')
            # print(self.excel_path)
        if excel_index == None:
            self.excel_index = 0
        # 打开excle
        self.data = xlrd.open_workbook(self.excel_path)
        # 打开指定sheet
        self.table = self.data.sheets()[0]

    # 获取sheet中有数据的行数
    def excel_line(self):
        return self.table.nrows

    # 获取sheet中有数据的列数
    def excel_col(self):
        return self.table.ncols

    # 获取单元格值
    def excel_cell_value(self, row, col):
        if self.excel_line() > 0:
            return self.table.cell(row, col).value
        else:
            print('空数据')

    # 获取行的值
    def excel_line_value(self, line):
        return self.table.row_values(line)

    def excel_data(self):
        excel_data_lst = []
        # 根据行数进行循环遍历
        # print(self.excel_line())
        if self.excel_line() > 0:
            for i in range(1, self.excel_line()):
                # 获取指定行数据，返回的数据类型：list
                # 错误的把self.table.row_values(i)写成了self.table.row_values[i]
                row_values = self.table.row_values(i)
                # 把返回的行数据追加至excel_data_lst中
                excel_data_lst.append(row_values)
            return excel_data_lst


if __name__ == '__main__':
    ged = Get_Excel_Data()
    # ged.excel_line()
    print(ged.excel_cell_value(1,3).value)
    print(ged.excel_data())
