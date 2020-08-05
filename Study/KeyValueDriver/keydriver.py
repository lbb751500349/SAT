#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/5 21:56
# @Author  : baob
# @Site    : 
# @File    : keydriver.py
# @Software: PyCharm Community Edition

import time
from Study.KeyValueDriver import action_method

am = action_method.Action_Method()
a = ['open_browser', '2']
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
gam = getattr(am, 'open_browser')
gam('Chrome')
gam = getattr(am, 'open_url')
gam('https://www.baidu.com/')
gam = getattr(am, 'element_find_element')
gam('kw')
gam=getattr(am,'element_send_keys')
gam('kw', '123')
gam = getattr(am, 'element_click')
gam('su')
gam = getattr(am, 'close_browser')
gam()


