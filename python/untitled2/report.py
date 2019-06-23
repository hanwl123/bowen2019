# !/usr/bin/puthon
# _*_coding:utf_8  _*_
from  HTMLTestReportCN import  HTMLTestRunner
import unittest

#出现这样的提示语的原因是pycharm

def  B_gao(name):
    #创建一个测试套件
    suit = unittest.TestSuite()
    for  i in  name:
        #将测试用例添加到测试套件中
        #将某一个类中所有的测试用例添加到测试套件中

        #自动去发现写的通配符语句中的文件的以test开头的函数，提取出来放在dis（列表）中
        #第一个参数：存放测试脚本的路径
        #第二个参数：匹配测试文件的通配符语句
        dis = unittest.defaultTestLoader.discover(r'C:\Users\hanwl\PycharmProjects\untitled2',pattern='{}_test.py'.format(i.strip()))
        for i  in   dis:
            suit.addTest(i)
        f = open  ('abc.html','wb')
        runner = HTMLTestRunner(
                stream=f,
                title="别克测试报告",
                description="报告的描述",
                verbosity=2,
            )
        runner.run(suit)
        f.close()
if __name__ == '__mian__':
    B_gao()


























