#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/5 21:44
# @Author  : baob
# @Site    : 
# @File    : action_method.py
# @Software: PyCharm Community Edition

import time
from selenium import webdriver

from Study import logfile

class Action_Method(object):


    def __init__(self):
        self.lf.log_info("TEST")
        self.lf.close_log()
    # def __init__(self, driver):
    #     if driver == 'Chrome':
    #         self.driver = webdriver.Chrome(r'D:\Study\google\chromedriver.exe')
    #     elif driver == 'Edge':
    #         self.driver = webdriver.Edge('')
    #     elif driver == 'Firefox':
    #         self.driver = webdriver.Firefox('')
    #     else:
    #         print('暂不支持')
    def open_browser(self, browser):
        if browser == 'Chrome':
            self.driver = webdriver.Chrome(r'D:\Study\google\chromedriver.exe')
        elif browser == 'Edge':
            self.driver = webdriver.Edge('')
        elif browser == 'Firefox':
            self.driver = webdriver.Firefox('')
        else:
            print('暂不支持此种浏览器')

    def open_url(self, url = None):
        if url is None:
            self.driver.get(r'https://www.baidu.com/')
        else:
            self.driver.get(url)

    def element_find_element(self, ele):
        return self.driver.find_element_by_id(ele)

    def element_send_keys(self, ele, value):
        self.element_find_element(ele).send_keys(value)

    def element_click(self,ele):
        self.element_find_element(ele).click()

    def element_close(self):
        self.driver.close()

    def element_wait(self, sleep_value):
        time.sleep(sleep_value)

    def close_browser(self):
        self.driver.close()
        self.driver.quit()

