#!/usr/bin/python
#coding:utf-8

"""
@Author: Baob
@Project:SAT
@software: PyCharm
@time: 2020/7/2 19:01
"""

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
# from selenium.webdriver.support.wait import WebDriverWait
#
# from Study import settings
#
# def define_sum(num = None):
#     if num is not None:
#         sum = settings.DEFULT_INPUT_NUM + num
#         print("输入的值和是%s" %sum)
#     else:
#         print("输入的值和是%s" %(settings.DEFULT_INPUT_NUM))
#
#
# # define_sum()
# # define_sum(3)
#
#
# import time
# from  selenium import  webdriver
# from  selenium.webdriver.common.by import By
#
#
# def run_selenium():
#     driver = webdriver.Chrome(r'D:\Study\google\chromedriver.exe')
#     driver.maximize_window()
#     driver.get(r'https://www.baidu.com/')
#     driver.implicitly_wait(time_to_wait=2)
#     # driver.find_element(By.ID, 'kw').send_keys('d')
#     time.sleep(1)
#     driver.find_element(By.ID, 'su').click()
#     print(driver.find_element(By.ID, 'su').get_attribute("value"))
#     time.sleep(2)
#     driver.close()
#     driver.quit()
#
#
# run_selenium()
import os

report_path = os.path.join(os.getcwd() + '\\Report\\' + 'report.html')
print(report_path)
report_file = open(report_path, 'wb')
report_file.close()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(r'D:\Study\google\chromedriver.exe')
driver.get(r'https://www.baidu.com/')

driver.find_element(By.ID,'kw').send_keys('a')
driver.find_element(By.ID,'su').click()

time.sleep(2)
driver.quit()