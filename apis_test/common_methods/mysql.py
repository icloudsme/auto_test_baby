#encoding:utf-8

import MySQLdb

from apis_test.common_methods.config import *
from apis_test.mylogs import logger


def mysql_self(type,sql):
    if type == 'mysql':
        conn=MySQLdb.connect(
                              host=datas['sit-mysql']['数据库hosts'],
                              port=int(datas['sit-mysql']['数据库端口']),
                              user=datas['sit-mysql']['用户名'],
                              passwd=datas['sit-mysql']['用户密码'],
                              db=datas['sit-mysql']['数据库名称'],
                              charset='utf8'
                             )
        cur = conn.cursor()
        #语句
        # sql = "select * from s_user where username='17717392244'"
        r = cur.execute(sql)
        info = cur.fetchmany(r)
        for i in info:
            logger.info(i)
        cur.close()
        conn.commit()
        conn.close()
        return info

mysql_self('mysql',"select * from s_user where username='17195864861'")
