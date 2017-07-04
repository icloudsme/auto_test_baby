#coding:utf-8
"""
=================================
     打印总行数，并显示每行数据
=================================
1、host=数据库hosts
2、dbname=数据库名称
3、port=数据库端口
4、username=用户名
5、userpwd=用户密码

"""
import cx_Oracle

from apis_test.common_methods.config import *
from apis_test.mylogs import logger


def myoracle_self(type,sql):
    if type=='oracle':
        host=datas['sit-oracle']['数据库hosts']
        dbname=datas['sit-oracle']['数据库名称']
        port=datas['sit-oracle']['数据库端口']
        username=datas['sit-oracle']['用户名']
        userpwd=datas['sit-oracle']['用户密码']
        dsn=cx_Oracle.makedsn(host, port, dbname)

        #连接数据库
        conn = cx_Oracle.connect(username, userpwd, dsn)
        cur = conn.cursor()
        #执行sql语句
        r=cur.execute(sql)
        #查看语句执行结果
        info = cur.fetchall()

        for n in info:
            logger.info(n)
        cur.close()
        conn.commit()
        conn.close()
        return info

