#coding:utf8

from apis_test.common_methods.mysql import *


result = mysql_self('mysql',"select * from s_user where username='17717392244'")


print result
