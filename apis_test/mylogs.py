#coding:utf-8

"""
目前有BUG，会打印两边
1    filename 包日志保存到哪个文件
2    filemode记录日志的模式，a代表在文件中追加日志，w是删除原有文件，创建新文件。
3    format 设置日志IDE输出格式，
        %(name)s 	            Logger的名字
        %(levelno)s 	        数字形式的日志级别
        %(levelname)s 	        文本形式的日志级别
        %(pathname)s 	        调用日志输出函数的模块的完整路径名，可能没有
        %(filename)s 	        调用日志输出函数的模块的文件名
        %(module)s 	            用日志输出函数的模块名
        %(funcName)s 	        调用日志输出函数的函数名
        %(lineno)d 	            调用日志输出函数的语句所在的代码行
        %(created)f 	        当前时间，用UNIX标准的表示时间的浮 点数表示
        %(relativeCreated)d 	输出日志信息时的，自Logger创建以 来的毫秒数
        %(asctime)s 	        字符串形式的当前时间。默认格式是 “2003-07-08 16:49:45,896”。逗号后面的是毫秒
        %(thread)d 	            线程ID。可能没有
        %(threadName)s 	        线程名。可能没有
        %(process)d 	        进程ID。可能没有
        %(message)s 	        用户输出的消息
4    level 日志的严重程度，
5    datefmt 日期格式
6    stream 日志输出到那里，如果有filename参数，忽略改参数
"""

import time
import os.path
import logging
import sys


def loginfo(name=sys.argv[0].split('/')[-1]):
    logger = logging.getLogger('')
    #获得当前系统时间的字符串
    localtime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    print('\033[32;1mlocaltime=\033[0m'+localtime)
    #系统当前时间年份
    year=time.strftime('%Y',time.localtime(time.time()))
    #月份
    month=time.strftime('%m',time.localtime(time.time()))
    #日期
    day=time.strftime('%d',time.localtime(time.time()))
    #具体时间 小时分钟毫秒
    mdhms=time.strftime('%m%d%H%M%S',time.localtime(time.time()))

    #获取当前文件路径os.getcwd()
    fileYear=os.getcwd()+'/logs/'+year
    fileMonth=fileYear+'/'+month
    fileDay=fileMonth+'/'+day

    if not os.path.exists(fileYear):
        os.mkdir(fileYear)
        os.mkdir(fileMonth)
        os.mkdir(fileDay)
    else:
        if not os.path.exists(fileMonth):
            os.mkdir(fileMonth)
            os.mkdir(fileDay)
        else:
            if not os.path.exists(fileDay):
                os.mkdir(fileDay)

    #创建一个文件，以‘timeFile_’+具体时间为文件名称
    log_file = os.path.join(fileDay, '{}_{}.log'.format(name, mdhms))
    if not os.path.exists(log_file):
        try:
            fp = open(log_file, 'w')
            fp.close()
        except Exception as ex:
            print '{}'.format(ex)

    #获取logs文件夹中的的client.log文件
    logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
            datefmt='%a, %d %b %Y %H:%M:%S',
            filename=log_file,
            filemode='w')
    formatter = logging.Formatter(fmt='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt='%a, %d %b %Y %H:%M:%S')
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    console.setFormatter(formatter)
    logger.addHandler(console)
    return logger

logger = loginfo()

