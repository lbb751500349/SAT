#!/usr/bin/python
#coding:utf-8

"""
@Author: Baob
@Project:SAT
@software: PyCharm
@time: 2020/7/2 19:01
"""


from Study import settings

def define_sum(num = None):
    if num is not None:
        sum = settings.DEFULT_INPUT_NUM + num
        print("输入的值和是%s" %sum)
    else:
        print("输入的值和是%s" %(settings.DEFULT_INPUT_NUM))


# define_sum()
# define_sum(3)


import time
from  selenium import  webdriver
from  selenium.webdriver.common.by import By


def run_selenium():
    driver = webdriver.Chrome(r'D:\Study\google\chromedriver.exe')
    driver.maximize_window()
    driver.get(r'https://www.baidu.com/')
    driver.implicitly_wait(time_to_wait=2)
    driver.find_element(By.ID, 'kw').send_keys('d')
    time.sleep(2)
    driver.find_element(By.ID, 'su').click()
    time.sleep(2)
    driver.close()
    driver.quit()


run_selenium()
