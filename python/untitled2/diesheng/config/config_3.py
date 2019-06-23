#!/usr/bin/python
#_*_ coding:utf-8 _*_
#python   自带写日志的模块
import  logging
#写日期的模块
import datetime
#系统模块
import  os
#第一步：创建一个日志文件
log_file = os.path.join(r'C:\Users\hanwl\PycharmProjects\untitled2\diesheng\log',str(datetime.datetime.now().date())+ ".out")
#第二步：定义一个日志，输出的格式,设置日志输出的格式：脚本的名字、代码执行的行货
formatter = logging.Formatter(fmt='%(asctime)s,%(msecs)d %(levelname)-4s [%(filename)s:%(lineno)d] %(message)s',
                              datefmt='%d-%m-%Y:%H:%M:%S')
#第三步：将日志以字节流的形式输出
con_handler = logging.StreamHandler()
#第四步：将日志输出到文本中
fil_handler = logging.FileHandler(log_file, encoding='utf-8')
#第五步：输出到控制台的日志添加格式
con_handler.setFormatter(formatter)
#第六步：给输出的日志添加格式
fil_handler.setFormatter(formatter)
#第七步：定义一个日志函数，供别的脚本使用
def get_logger(name):
    """
    :param name: 脚本的名字，例如：在test_1.py使用get_logger,name==test_1
    :return:
    """
    logger = logging.getLogger(name)
    logger.addHandler(con_handler)
    logger.addHandler(fil_handler)
    logger.setLevel(logging.INFO)
    return logger














