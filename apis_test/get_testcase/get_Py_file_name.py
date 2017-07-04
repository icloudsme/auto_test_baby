#coding:utf8
"""
核心:获取到可执行文件
1、startswith以什么开头
2、endswith以什么结尾
"""
import os
import sys
from apis_test.mylogs import logger

#获取需要执行的脚本文件路径
path = sys.path[0]

# 获取test开头的PY文件
def del_files(path):
    for root , dirs, files in os.walk(path):
        for name in files:
            if name.startswith("test"):
                Executable_files=os.path.join(root, name)
                logger.info("Executable files: " + Executable_files)
                print Executable_files
                f = open("case.txt", 'a')
                f.writelines(Executable_files+'\n')
                f.close()

# 输入一个py文件名称，获取文件内部函数
def Query_file():
    filename = raw_input('Input the one filename show above[q to quit]:')
    if filename == 'q':
        sys.exit()

    file = open(filename, 'r').readlines()
    print '\n\n'
    for i in file:
        if i.startswith('class') or i.startswith('def') or i.startswith('    def'):
            print i,

# test
if __name__ == "__main__":
    del_files(path)