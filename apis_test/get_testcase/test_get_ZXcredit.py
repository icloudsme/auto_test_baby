#coding:utf8
"""
获取预授信结果
"""

import requests

from apis_test.common_methods.config import *
from apis_test.get_testcase.case_test import TestCase
from apis_test.mylogs import logger


class get_credit_ZX(TestCase):
    datas = {
        "sit": {
            "applyId":"26170155"
        },
        "uat": {
            "applyId":"26170155"
        }
    }

    def __init__(self):
        # 配置URL
        self.URL = hosts["uat"] + apis["获取51公积金数据"]["path"]
        # 配置请求头
        # self.headers = {"Content-Type":"application/x-www-form-urlencoded","Access-Token":Token().get_token()}
        self.headers={"Content-Type":"application/x-www-form-urlencoded","Access-Token":"d3ad324c239d4ece86bdb9c523acc5b5e5cc2b96b7ee4800b87cf2437ee19658"}
        print self.headers
        logger.info(self.headers)
        # 配置请求数据
        self.data = self.datas["uat"]
        logger.info(self.data)
    #获取征信预授信
    def get_credit(self):
        self.sendrequests = requests.post(self.URL, json=self.data, headers=self.headers)
        #打印出请求返回信息
        print self.sendrequests.text
        assert self.sendrequests.status_code == 200, "接口返回code,期望值:200"

get_credit_ZX().get_credit()


