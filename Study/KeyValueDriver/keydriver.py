#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/5 21:56
# @Author  : baob
# @Site    : 
# @File    : keydriver.py
# @Software: PyCharm Community Edition

import time
from Study.KeyValueDriver import action_method
from Study import get_excle_data

class SaoCaoZao(object):

    ac = action_method.Action_Method()

    def run_main(self):
        ged = get_excle_data.Get_Excel_Data()
        for line in range(1, ged.excel_line()):
            excel_method = ged.excel_cell_value(line, 2)
            print(excel_method)
            # print(excel_method== "text:'选择'")
            excel_method_element = ged.excel_cell_value(line, 3)
            excel_method_value = ged.excel_cell_value(line, 4)
            self.run_method(excel_method, excel_method_element, excel_method_value)

    def run_method(self, user_method, locator_element, input_value):
        if user_method == "选择":
            act = getattr(self.ac, "open_browser")
            return act(locator_element)
        elif user_method == "打开":
            act = getattr(self.ac, "open_url")
            return act(locator_element)
        elif user_method == "等待":
            act = getattr(self.ac, "element_wait")
            return act(input_value)
        elif user_method == "关闭":
            act = getattr(self.ac, "element_close")
            return act()
        else:
            print("暂不支持其它操作")

if __name__ == "__main__":
    scz = SaoCaoZao()
    scz.run_main()
# Operation = ['选择浏览器','打开页面','输入值','点击','等待','关闭浏览器']
# am = action_method.Action_Method()
# if Operation[0] == '选择浏览器':
#     am.open_browser('Chrome')
#     am.open_url()
#     am.element_wait(2)
# if Operation[-1] == '关闭浏览器':
#     am.close_browser()
# else:
#     print("没有这些操作")
# a = ['open_browser', '2']
# am.open_browser('Chrome')
# am.open_url()
# am.element_find_element('su')
# time.sleep(2)
# getattr(object, name,default)返回一个对象属性值
# for i in a:
#     gam = getattr(am,i,'3')
#     if gam == '3':
#         print('没有此方法')
#     else:
#         print(gam)
# gam = getattr(am, 'open_browser')
# gam('Chrome')
# gam = getattr(am, 'open_url')
# gam('https://www.baidu.com/')
# gam = getattr(am, 'element_find_element')
# gam('kw')
# gam=getattr(am,'element_send_keys')
# gam('kw', '123')
# gam = getattr(am, 'element_click')
# gam('su')
# gam = getattr(am, 'close_browser')
# gam()


