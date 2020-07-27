# coding=utf-8


import unittest
import os

class Run_Unittest(unittest.TestCase):

    def test_case(self):
        # 凉了
        current_path = os.path.join(os.getcwd(), '')
        suite = unittest.defaultTestLoader.discover(current_path, pattern='test0*.py')
        unittest.TextTestRunner().run(suite)

if __name__ == '__main__':
    unittest.main()
    # print(os.path.join(os.getcwd()))