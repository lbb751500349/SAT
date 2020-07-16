# -*- coding: utf-8 -*-

"""
  @desc: 测试类
  @author: Amio_
  @file: test.py
  @date: 2017/12/18 12:06
"""
# import time
#
# from sat.ui.pom.login_page import LoginPage
# from sat.ui.base.browser_engine import BrowserEngine
# from selenium import webdriver
#
#
# class Test(object):
#     driver = webdriver.Chrome(r'D:\Study\google\chromedriver.exe')
#
#     def test_login(self):
#         LoginPage(driver=self.driver).login()  # 实现登录
#         time.sleep(2)
#         self.driver.quit() # 一定要退出
#
# if __name__ == "__main__":
#     tt =Test()
#     tt.test_login()
import time
import unittest
from ddt import ddt,data

from sat.ui.pom.login_page import Search


@ddt()
class Test_Search_txt(unittest.TestCase):
    @data("d", "t")
    def test01(self,txt):
        Search.search_txt(txt)
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()

