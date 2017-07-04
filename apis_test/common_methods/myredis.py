#encoding:utf-8
"""
1、myhost:数据库hosts
2、myport:数据库端口
"""

import redis

from apis_test.common_methods.config import *

myhost=datas['sit-redis']['数据库hosts']
myport=int(datas['sit-redis']['数据库端口'])

connect = redis.Redis(host=myhost,port=myport)