# -*- coding: utf-8 -*-

"""
  @desc: 测试类
  @author: Amio_
  @file: testt.py
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




import unittest



# @ddt()
class Search_txt(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(u"test类第一次运行")

    @classmethod
    def tearDownClass(cls):
        print(u"test类第2次运行")


    def setUp(self):
        pass
        # self.driver = webdriver.Chrome(r'D:\Study\google\chromedriver.exe')
        # # driver.get(r'https://www.baidu.com/')
        # self.url = r'https://www.baidu.com/'


    # @data("d", "t")
    # def test01(self,txt):
    #     Search(self.driver,self.url).search_txt(txt)
    #     time.sleep(3)

    def test_first(self):
        print(u"test第一条case111")

    # @unittest.skip("跳过第二条")
    def test_second(self):
        print(u"test第2条case")

    def test_thrid(self):
        print(u"test第3条case")


    def tearDown(self):
        pass
        # self.driver.close()
        # self.driver.quit()

if __name__ == '__main__':
    # 批量执行case并生成测试报告
    # suite = unittest.defaultTestLoader.discover(os.getcwd(),pattern="test*.py")
    # unittest.TextTestRunner().run(suite)
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(Search_txt("test_first"))
    # 第一次未把TextTestRunner实例化TextTestRunner()
    # 第二次忘记了TextTestRunner方法了
    unittest.TextTestRunner().run(suite)