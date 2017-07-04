# encoding:utf-8 
"""
 获取网销access_token授权 ，且设置供后续文件调用
"""

import requests

from apis_test.common_methods.config import *
from apis_test.get_testcase.case_test import TestCase
from apis_test.mylogs import logger


class Token(TestCase):
    datas = {
        "sit": {
            "appId": "net_sale_wap", "secret": "f08191872fd54af4904d01bd0fd28778"
        },
        "uat": {
            "appId": "net_sale_wap", "secret": "f08191872fd54af4904d01bd0fd28778"
        }
    }

    def __init__(self):
        super(Token,self).__init__()
        # 配置URL
        self.URL = hosts["uat"] + apis["51fund授权码接口Access-Token"]["path"]
        # 配置请求头
        self.headers = {"Content-Type": "application/json"}
        # 配置请求数据
        self.data = self.datas["uat"]

    def get_token(self):
        self.sendrequests = requests.post(self.URL, json=self.data, headers=self.headers)
        # print self.sendrequests.text    #打印出请求返回内容
        assert self.sendrequests.json()['responseStatus']['code']== '000000'
        #获取token
        token = self.sendrequests.json()["body"]["accessToken"]
        #日志打印token
        logger.info(token)
        #返回token，供后续调用
        return token

    def test01(self):
        self.get_token()
Token().test01()