#coding:utf8

import os
import subprocess
import sys

path = sys.path[0]
print path

caselist=os.listdir(path,'case.txt')
print caselist
# for a in caselist:
#      s=a.split('.')[1]
#
#      if s=='py':
#
# #由于路径中有空格，所以先用cd命令查找到该目录
#           os.system('cd D:\\Program Files\\python\\test_case')
#           os.system('python .\\%s 1>>log.txt 2>&1'%a)