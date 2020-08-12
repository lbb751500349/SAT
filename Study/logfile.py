#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/8/12 21:10
# @Author  : baob
# @Site    : 
# @File    : logfile.py
# @Software: PyCharm Community Edition

import os
import datetime
import logging

class UserLogInfo(object):
    def __init__(self):
        current_path = os.path.dirname(os.path.abspath(__file__))
        log_file_name = datetime.datetime.now().strftime("%Y%m%d") + ".log"
        # os.path.join()方法中字符串是使用“+”号拼接的，不是“,”
        log_path = os.path.join(current_path + r"/LogInfo/" + log_file_name)
        print(log_path)
        self.log = logging.getLogger()
        self.log.setLevel(logging.INFO)
        # 这里的%(asctime)s格式输错了，写入文件会提示输入的字符错误
        fomatter = logging.Formatter(
            "%(asctime)s - %(filename)s - %(funcName)s:%(lineno)d行 - %(levelname)s --->%(message)s")
        self.handle = logging.FileHandler(log_path, mode='a', encoding="utf-8")
        self.handle.setLevel(logging.INFO)
        self.handle.setFormatter(fomatter)
        self.log.addHandler(self.handle)


    def log_info(self):
        return self.log

    def close_log(self):
        self.handle.close()
        self.log.removeHandler(self.handle)


if __name__ == "__main__":
    log = UserLogInfo()
    logger = log.log_info()
    logger.info("dfsfds")
    log.close_log()