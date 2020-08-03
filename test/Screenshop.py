#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/31 7:45
# @Author  : baob
# @Site    : 
# @File    : Screenshop.py
# @Software: PyCharm Community Edition
import os
import sys
sys.path.append(os.path.dirname(__file__))

import time
import ddt
import HTMLTestRunner
import  unittest
from selenium import webdriver

from Study.get_excle_data import Get_Excel_Data

class Baidu_Search_Text1(object):
    def __init__(self, driver):
        self.driver = driver

    def bsearch_text1(self,text,text1):
        self.driver.find_element_by_id(text).send_keys(text1)
        # self.driver.find_element_by_id('kw').send_keys(text1)
        self.driver.find_element_by_id('su').click()

    def bsearch_text2(self, text):
        self.driver.find_element_by_id('kw').send_keys(text)
        self.driver.find_element_by_id('su1').click()

@ddt.ddt
class Test_Feature(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(r'D:\Study\google\chromedriver.exe')
        self.driver.get(r'https://www.baidu.com/')
        self.driver.implicitly_wait(5)

    def tearDown(self):
        # 自动截图
        for method_name,error in self._outcome.errors:
            if error:
                filename = self._testMethodName
                current_path = os.getcwd()
                self.driver.save_screenshot(os.path.join(current_path + '\\Report\\' + filename+ ".png"))
        self.driver.close()

    # @ddt.data(Get_Excel_Data().excel_data())
    # @ddt.unpack
    data = Get_Excel_Data().excel_data()
    @ddt.data(*data)
    def test01(self, data):
        text, text1 = data
        Baidu_Search_Text1(self.driver).bsearch_text1(text, text1)
        time.sleep(2)


    @unittest.skip("跳过")
    @ddt.data((1,))
    def test02(self,text):
        Baidu_Search_Text1(self.driver).bsearch_text2(text)


if __name__ == '__main__':
    suitet = unittest.TestSuite()
    suitet.addTest(Test_Feature('test01'))
    current_path = os.getcwd()
    print(current_path)
    f_p = os.path.join(current_path + '\\Report\\' + "report1.html")
    print(1)
    with open(f_p, 'wb') as fp:
        hr = HTMLTestRunner.HTMLTestRunner(stream=fp, title="测试2", description="啥几把万一")
        hr.run(suitet)