#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/13 21:10
# @Author  : baob
# @Site    : 
# @File    : userlog.py
# @Software: PyCharm Community Edition

import os
import datetime
import logging

class User_log(object):
    def __init__(self):
        base_path = os.path.dirname(os.path.abspath(__file__))
        user_log_name = datetime.datetime.now().strftime("%Y%m%d") + 'user2.log'
        user_log_path = os.path.join(base_path + r"/Loginfo/" + user_log_name)
        print(user_log_path)
        self.open_user_log = open(user_log_path, mode="a", encoding="utf-8")
        format_string = "%(asctime)s - %(filename)s - %(module)s - " \
                        "%(funcName)s:%(levelname)s - %(lineno)d --->" \
                        "%(message)s"
        logging.basicConfig(
            format=format_string,
            level=logging.INFO,
            stream=self.open_user_log
        )

    def user_log_info(self, message):
        return logging.info(message)
        self.open_user_log.close()

if __name__ == "__main__":
    ul = User_log()
    ul.user_log_info('能不能行')

