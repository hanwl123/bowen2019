# !/usr/bin/puthon
# _*_coding:utf_8  _*_
from  HTMLTestReportCN  import HTMLTestRunner
import   unittest

def  Bao_gao(*name,report_path):
    suit = unittest.TestSuite()
    for  i in  name[0]:
    #dis = unittest.defaultTestLoader.discover(r'C:\Users\hanwl\PycharmProjects\untitled2\test_1\report',pattern='{}_test.py')
        suit.addTest(i)
    with  open(report_path, 'wb')as f:
        runner = HTMLTestRunner(
        stream=f,
        title="测试报告",
        description="报告的描述",
        verbosity=2,
    )
    runner.run(suit)

# if __name__ == '__mian__':
#     Bao_gao()



#
# from HTMLTestReportCN import HTMLTestRunner
# import unittest
# from test_1.test.biaozhun_test import Biao
# def baogao(*x):
#     suit=unittest.TestSuite()
#     for i in x:
#         suit.addTest(Biao(i))
#     f=open('c.html','wb')
#     runner=HTMLTestRunner(stream=f,tester='sunyuebo',description='结果如下',title='延期取消订单报告',verbosity=2)
#     runner.run(suit)
# baogao('test_1','test_2')
#
#
#










