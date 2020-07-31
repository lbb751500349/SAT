#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/31 7:45
# @Author  : baob
# @Site    : 
# @File    : Screenshop.py
# @Software: PyCharm Community Edition

import os
import HTMLTestRunner
import  unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Baidu_Search_Text1(object):
    def __init__(self, driver):
        self.driver = driver

    def asearch_text1(self):
        SU = (By.ID,'su')
        KW = (By.ID,'kw')
        self.driver.find_element(KW).send_keys('a')
        self.driver.find_element(SU).click()

    def bsearch_text2(self):
        SU = (By.ID, 'su')
        KW = (By.ID, 'kw')
        self.driver.find_element(KW).send_keys('b')
        self.driver.find_element(SU).click()


class Test_Feature(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(r'D:\Study\google\chromedriver.exe')
        self.driver.get(r'https://www.baidu.com/')

    def tearDown(self):
        # 自动截图
        # for method_name,error in self._outcome.errors:
        #     if error:
        #         filename = self._testMethodName
        #         current_path = os.path.join(os.getcwd(), "")
        #         self.driver.save_screenshot(os.path.join(current_path + '\\Report\\' + filename+ ".png"))
        self.driver.close()

    def test01(self):
        Baidu_Search_Text1(self.driver).asearch_text1()

    def test02(self):
        Baidu_Search_Text1(self.driver).bsearch_text2()

if __name__ == '__main__':
    # suite = unittest.TestCase(Baidu_Search_Text('search_text1'))
    # current_path = os.path.join(os.getcwd(), "")
    # f_p = os.path.join(current_path + '\\Report\\' + "report1.html")
    # with open(f_p, 'wb') as fp:
    #     hr = HTMLTestRunner.HTMLTestRunner(stream=fp, title="测试2", description="啥几把万一")
    #     hr.run(suite)

    suite = unittest.TestSuite()
    suite.addTest(Test_Feature('test02'))
    unittest.TextTestRunner.run(suite)
    # current_path = os.path.join(os.getcwd(), "")
    # f_p = os.path.join(current_path + '\\Report\\' + "report1.html")
    # with open(f_p, 'wb') as fp:
    #     hr = HTMLTestRunner.HTMLTestRunner(stream=fp, title="测试2", description="啥几把万一")
    #     hr.run(suite)