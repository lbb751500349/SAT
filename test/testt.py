# coding=utf-8

import os
import unittest
import HTMLTestRunner


class Run_Unittest(unittest.TestCase):

    def test_case(self):
        # 凉了
        current_path = os.path.join(os.getcwd(), '')
        suite = unittest.defaultTestLoader.discover(current_path, pattern='test0*.py')
        f_p = os.path.join(current_path + '\\Report\\'+"report.html")
        with open(f_p, 'wb') as fp:
            hr = HTMLTestRunner.HTMLTestRunner(stream=fp, title="测试2", description="啥几把万一")
            hr.run(suite)
        # unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    unittest.main()
    # print(os.path.join(os.getcwd()))