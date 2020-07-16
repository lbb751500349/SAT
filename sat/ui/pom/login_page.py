# -*- coding: utf-8 -*-

"""
  @desc: 登录页PO
  @author: Amio_
  @file: login_page.py
  @date: 2017/12/18 12:01
"""
# from selenium.webdriver.common.by import By
#
# from sat.ui.base.base_page import BasePage
#
#
# class LoginPage(BasePage):
#     URL = 'http://mdm-test.test.com/login/'
#     USERNAME = (By.ID, 'username')
#     PASSWORD = (By.ID, 'password')
#     SUBMIT_BTN = (By.XPATH, '//button[@type="submit"]')
#
#     def __init__(self, driver):
#         super().__init__(driver=driver, url=self.URL)
#
#     def login(self):
#         self.open('TrialOS药试圈，医药数字化协作平台，让好药触手可及')
#         self.send_keys(webElement=self.find_element(*self.USERNAME), keys='rng')
#         self.send_keys(webElement=self.find_element(*self.PASSWORD), keys='123')
#         self.find_element(*self.SUBMIT_BTN).click()


from selenium.webdriver.common.by import By

from sat.ui.base.base_page import Base


class Search(Base):
    KW = (By.ID, 'kw')
    SU = (By.ID, 'su')

    def get_elemnt_kw(self):
        return self.find_element(*self.KW)

    def get_elemnt_su(self):
        return self.find_element(*self.SU)

    def search_txt(self,txt):
        self.get_elemnt_kw().send_keys(txt)
        self.get_elemnt_su().click()

# tt = Search()
# tt.search(txt='abc')
