# import day1
# day1.asd()
# from day1 import asd,qwe
# from  day1 import *
# import random
# import copy
# try:
#     a = 123 + 'qw'
#     print(a)
# except Exception as e:               #默认可以预防所有类型的错误
#      print(e)
# except TypeError as e:
#     print(e)
# except  TabError as e:
#     print(e)



#
# try:
#     a = 123 + '12'
#     print(a)
# except Exception as e:               #默认可以预防所有类型的错误
#      print(e)
# else:
#     print(12332)
# finally:
#     print(12)

# import  xlwt
#所有的导入语句写入开头
# f = xlwt.Workbook(encoding='utf-8')
# sheet = f.add_sheet('sheet')
# #写入数据，固定的写入单元格 x ，y
# for i in range(100):
#  sheet.write(i,0,i+1)
# f.save('aa.xls')

# import  xlwt
# f = xlwt.Workbook(encoding='utf-8')
# sheet = f.add_sheet('python_test')
# for i in range(1,10):
#     for j in range(1,i+1):
#       sum =  '{}*{}={}'
#       num = (sum.format(i,j,i*j))
#       if i == j:
#           print('')
#       sheet.write(i-1,j-1,num)
# f.save('aa.xls')


#把a.txt到入excel表格中
# a = open('C:\\Users\\hanwl\\Desktop\\a.txt','r',encoding='utf-8')
# b = a.readlines()
# import xlwt
# f = xlwt.Workbook(encoding='utf-8')
# sheet = f.add_sheet('python')
# a = open('C:\\Users\\hanwl\\Desktop\\a.txt','r',encoding='utf-8')
# b = a.readlines()
# c = []
# for i in range(4):
#     w = b[i]
#     q = w.split(',')
#     c.append(q)
#     print(c)
# a.close()
# for j in range(len(c)):
#     for k in range(len(q)):
#      sheet.write(j,k,c[j][k])
# f.save('bb.xls')







# a = xlrd.open_workbook('‪C:\\Users\\hanwl\\Desktop\\a.xls')
# print(a)
# # sheet = f.sheets()[0]
# # b = f.nsheets
# # b = f.sheet_names()
# # print(b)

#读取行
# sheet = f.sheet_by_name('python_test')
# b = sheet.nrows
# # #b = f.sheet.row_values(1)
# for i in range(b):
#     if i > 14 and i < 20:
#      c = sheet.row_values(i)
#      print(c)

#读取列
# b = sheet.col_values(1)
# print(b)
#读取多少列
# c = sheet.col_values(0)
# print(c)
#读取某个单元格的内容
# d = sheet.cell(2,2).value
# print(d)

#追加

#from xlutils.copy  import copy
# #打开想要打开的文件
# import xlrd
# f = xlrd.open_workbook('bb.xls')
# #显示标签页
# sheet1 = f.sheets()[0]
# #显示有多少行
# b = sheet1.nrows
# c = sheet1.ncols
# print(b)
# #复制以下原来的文件具有可写的权限
#new_f = copy(f)
# #获取到的标签页
#sheet = new_f.get_sheet(0)
# #写入内容
# for i in range(10)
#sheet.write(b+i,c,'qwe')
# #保存
# new_f.save('bb.xls')





#单独的具有某种功能的.py文件叫做模块
#xlutils 是一个包
#包是一个目录，存放同一类型的模块
#任何一个包必须含有__init__.py这个文件

#时间模块   python自带的模块
# import time
#1.时间戳 从1970年早上八点到现在经过的秒数
# a = time.time()
# print(a)
#2.以元组的格式显示当前时间
#传入参数时，就显示以元组的格式显示参数的时间
#参数只能是时间戳
# a = time.localtime()
# print(a)
#本地化,默认显示当前时间
#传入参数时，占位符填充的是参数的时间
#参数只能元组类型的时间
#3.将元组类型的时间转化为本地化格式的时间
# b = time.localtime(100)
# a = time.strftime('%Y-%m-%d',b)
#4.将本地化时间转化为元组类型的时间
#第一个参数是本地化时间
#第二个参数时占位符时间
# a = time.strptime('2011-12-22','%Y- %m-%d')
# print(a)
#5.休息
#time.sleep(1)
#6.将元组时间转换成时间戳
# b = (2014,11,11,11,11,11,23,23,23,)
# a = time.mktime(b)
# print(a)

#练习题
#手动输入一个日期（年-月-日），输出
#1.年份的那一年是否是闰年
#2,.输出是一年中的第几天
# #3.输出今天是第几天
# import time                   #import time
# a = input('>>>')             #time.strptime()
# b = time.strptime(a,'%Y-%m-%d')
# print(b)
# if  b[0] % 400 == 0:
#     print('是世纪闰年')
# elif b[0] % 4 == 0 :
#     print('是闰年')
# print(b)
# print('这年的第',b[7],'天')
# print('今天周',b[6]+1)

# import time
# # a = input('>>>')
# # b = time.strptime(a,'%Y-%m-%d')
# # print(b)
# # d = time.mktime(b)
# # print(d)
# # c = d - 86400
# # print(c)
# # f = time.localtime(c)
# # print(f)
# # print(f[0],'年',f[1],'月',f[2],'号')

# a = time.strptime('2011-12-22','%Y- %m-%d')
# print(a)
#把excel表格导入a.txt文档
# import xlrd
# f = xlrd.open_workbook('bb.xls')
# sheet = f.sheet_by_name('python')
# b = sheet.nrows
# a = open('C:\\Users\\hanwl\\Desktop\\c.txt','w',encoding='utf-8')
# for i in range(b):
#     c = sheet.row_values(i)
#     print(c)
#     d = ','.join(c)
#     print(d)
#     a.write(d)
# a.close()





#把文档》txt导入excel表格
# import xlwt
# f = xlwt.Workbook(encoding='utf-8')
# sheet = f.add_sheet('python')
# a = open('C:\\Users\\hanwl\\Desktop\\a.txt','r',encoding='utf-8')
# b = a.readlines()
# c = []
# for i in range(4):
#     w = b[i]
#     q = w.split(',')
#     c.append(q)
#     print(c)
# a.close()
# for j in range(len(c)):
#     for k in range(len(q)):
#      sheet.write(j,k,c[j][k])
# f.save('bb.xls')


# import  pymysql
# import  xlrd


#连接数据库
#conn = pymysql.connect(host='192.168.0.88',
#                        port=3306,
#                        user='root',
#                        passwd='123456')
#创建游标
#m = conn.cursor()
#执行sql语句   数据库的个数
#创建数据库
# m.execute('create database python_learn;')
#使用数据库
# m.execute('use python_learn')
# #查看数据库
# m.execute('show databases;')
# print(m.fetchall())
#查看表格内容
#m.execute('show tables;')
#m.execute('create table h(name char(20),age int(20),sex char(20))')
#插入数据20条
# for i  in range(20):
#  m.execute('insert into h values("小红",{},"女"),("小李","19","女");'.format(i))
#  m.execute('select *  from h')
#读取上一个sql语句的结果 结果是个元组
# b = m.fetchall()
# print(b)
#默认一次读取一个参数，
# 传入的参数是数字几就读取几条数据
#b = m.fetchmany(3) #读取三条信息
#每次只读取一条数据
#b = m.fetchone()
#c = m.fetchone()
#print(b,c)
#断开数据库
# conn.close()





#把excel表格加入数据库中
# import  pymysql
# import  xlrd
# conn = pymysql.connect(host='192.168.0.88',
#                        port=3306,
#                        user='root',
#                        passwd='123456')
# f = xlrd.open_workbook('bb.xls')
# m=conn.cursor()
# m.execute('use python_learn')
# sheet = f.sheets()[0]
# # a = sheet.rows
# for i in range(a):
#     b = sheet.row_values(i)
#     if i == 0:
#         # continue
#         m.execute('create table aa({} char(20),{} int,{} char(20),{} char(20));'.format(b[0],b[1],b[2],b[3]))
#     else:
#         m.execute('insert into aa values("{}","{}","{}","{}");'.format(b[0],b[1],b[2],b[3]))
#     m.execute('select * from aa;')
# print(m.fetchall())





#将a.txt文档导入数据库中

# import  pymysql
# import  xlrd
# conn = pymysql.connect(host='192.168.0.88',
#                        port=3306,
#                        user='root',
#                        passwd='123456')
# m = conn.cursor()
# m.execute('use python_learn')
# a = open('C:\\Users\\hanwl\\Desktop\\a.txt','r',encoding='utf-8')
# b = a.readlines()
# for i in range(b):
#     w = b[i]
#     s = w.split(',')
#     if i == 0:
#         #continue
#         m.execute('create table ab({} char(20),{} int,{} char(20),{} char(20));'.format(s[0],s[1],s[2],s[3]))
#     else:
#         m.execute('insert into ab values("{}","{}","{}","{}");'.format(s[0],s[1],s[2],s[3]))
#     m.execute('select * from ab;')
# print(m.fetchall())
# a.close()


#将数据库中的数据导入到excel表格中
# import  pymysql
# import  xlwt
# conn = pymysql.connect(host='192.168.0.16',
#                        port=3306,
#                        user='root',
#                        passwd='123456')
# m = conn.cursor()
# m.execute('use hanwl')
# a =m.execute('select * from x;')
# print(a)
# m.execute('desc x')
# b = m.fetchall()
# f = xlwt.Workbook(encoding='utf-8')
# sheet = f.add_sheet('python_excel')
# c = []
# for i in range(len(b)):
#     c.append(b[i][0])
#     sheet.write(0,i,c[i])
# m.execute('select * from x;')
# d = m.fetchall()
# for  e  in range(len(d)):
#     for g in range(len(d)):
#       print(sheet.write(e+1,g,d[e][g]))
# f.save('ac.xls')

#将数据库中的内容导入到txt文档中
# import  pymysql
# import  xlwt
# conn = pymysql.connect(host='192.168.0.16',
#                        port=3306,
#                        user='root',
#                        passwd='123456')
# m = conn.cursor()
# m.execute('use hanwl')
# e =m.execute('select * from x;')
# print(e)
# m.execute('desc x')
# b = m.fetchall()
# a = open('C:\\Users\\hanwl\\Desktop\\d.txt','w',encoding='utf-8')
# c = []
# for i in range(len(b)):
#     c.append(b[i][0])
#     a.write('{} '.format(c[i]))
#     for j in range(len(e)):
#         p = e[j]
#         for k in range(len(p)):
#           a.write('{} '.format(p[k])
# a.close()


#与操作系统交互的模块
#import os
#获取当前所在位置
#print(os.getcwd())

#切换目录
# os.chdir(r'C:\Users\hanwl')
# print(os.getcwd())
#执行cmd命令，有结果的命令
# b = os.popen('ping 192.168.0.1')
# print(b.read())
# c = os.popen(('route print'))
# print(c.read())

# print(os.listdir())
#传入参数
#print(os.listdir(r'C:/Users/hanwl/PycharmProjects/untitled1'))
#创建目录
#os.mkdir(加路径)
#只能删除空目录
#os.rmdir(加路径)
#重命名
#os.remove(加路径)
#创建递归目录
#os.makedirs(r'aaa\bbb\ccc')
#删除递归目录
#os.removedirs(r'aaa\bbb\ccc')
#将路径与文件分隔开
# b = os.path.split(r'‪C:\Users\hanwl\Desktop\迅雷.lnk')
# print(b)
#将后缀名与路径分开
# b = os.path.splitext(r'‪C:\Users\hanwl\Desktop\迅雷.lnk')
# print(b)
#判断文件是否是普通文件
# b = os.path.isfile(r'‪C:\Users\hanwl\Desktop\迅雷.lnk')
# print(b)
#判断是否是目录
# b = os.path.isdir(r'‪C:\Users\hanwl\Desktop\迅雷.lnk')
# print(b)

#练习题
#将本目录下的所有.py的文件打印出来

# b = os.listdir()
# for i in b:
#     c = str(i)
#     d = c.endswith('.py')
#     if d == True:
#         print(i)




#封装了ssh协议，可以实现远程控制#
# import   paramiko
# #创建一个ssh客户端
# with paramiko.SSHClient() as  ssh123:
#     #跳过从known_hosts文件中验证
#     ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#     #连接主机
#     ssh123.connect(hostname='192.168.0.74',
#                    port = 22,
#                    username='root',
#                    password='123456')
#     #执行命令
#while  True:
 #   q = input('>>>')
#     a,b,c = ssh123.exec_command('{}'.format(q))
#
#     #第一个变量：标准输入的命令,,,,必须是有结果的命令
#     #第二个变量：命令的输出
#     #第三个变量是命令的报错
#     print(b.read().decode())
#if q ='exit'
 #   break
#     #操作完之后要断开连接


# import  paramiko
# #创建一个传输通道
# qq = paramiko.Transport(('192.168.0.74',22))
# #连接主机
# qq.connect(username='root',password='123456')
# #使用ssh协议创建一个传输文件的功能
# sftp = (paramiko.SFTPClient.from_transport(qq))
# #下载文件，，，从Linux上传文件到windows
# #sftp.get('在Linux上的路径 /home 文件名',r'前面加路径想要改的文件名字')
# #上传文件，，，，从Windows上传到Linux    文件名
# sftp.put('day1.py','/etc/day1.py')
# qq.close()


#发送邮件是smtp，pop3，imap
# import  smtplib  #封装smtp协议
# import email.mime.multipart as mul  # 制作邮件 赋给mul
# import email.mime.text as text  # 对邮件的正文进行处理
# #创建一个空邮件
# message = mul.MIMEMultipart()
# #标题
# message['subject'] = 'python_test'
# #发件人
# message['from'] = 'hanwl_1997@163.com'
# #收件人
# message['To'] = '854917004@qq.com'    #   添加多个收件人    群发   '.'join
# #正文  多行数据
# txt = """
# 河南是个好地方
# 广东人爱吃福建人
# 我姓xun
# 薰衣草的xun么
# 不是
# 是孙悟空的xun
# """
# #对正文进行处理
# tet = text.MIMEText(txt)
# #将处理过后的正文添加到邮件里  attcah  附着，连着
# #发送附件
# att1 = text.MIMEText(open('day1.py', 'rb').read(), 'base64', 'utf-8')
# #附件的字段   固定
# att1["Content-Type"] = 'application/octet-stream'
# # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
# att1["Content-Disposition"] = 'attachment; filename="day1.py"'
# message.attach(att1)
# #message.attach(tet)
# #定义邮件服务器
# smtp123 = smtplib.SMTP_SSL('smtp.163.com',465)
# #登录服务器  用户名 ， 密码：不是邮箱密码  是授权码
# smtp123.login('hanwl_1997@163.com','qwer')
# #发送邮件   发件人   收件人
# smtp123.sendmail('hanwl_1997@163.com','854917004@qq.com',message.as_string())
# #断开连接
# smtp123.close()




# #服务器
# #socket
# #   套接字：提供了通信双方最底层的功能（发送、接收）
# # c/s架构 ， 通过是socket 实现基本的通信
#
# #server服务器端   服务器：可以提供某种服务的产品或软件
# #邮件服务器 smtp   tcp  pop3
# #
#


#TCP
# import socket
# #创建一个套接字（具有发送和接收的能力）
# #  sock_STREAM   指的是tcp
# #AF_INET  是 ipv4
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #绑
# 定IP地址和端口号
# s.bind(('192.168.0.69',3000))
#
# #监听
# s.listen(5)   #  3  当达到我的处理极限时最大的等待个数
# while  True:
#     #接收客户端建立的连接
#     #accep 接收的是建立连接
#     #第一个变量：建立连接的信息
#     #第二个变量：客户端的ip和端口号
#     client,addr = s.accept()
#     while True:
#         # print(client)
#         #接收客户端发送的数据
#         #1024  指的是每次接收的最大字节B
#         reg = client.recv(1024)
#         print(reg.decode('utf-8'))
#         msg = input('>>>')
#         #给客户端发送响应
#         client.send(msg.encode('utf-8'))


#UDP服务器
# import  socket
# #创建一个套接字  # IPV4  SOCK_DGRAM    UDP
# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# #绑定IP地址  接收到的是元组的类型
# s.bind(('192.168.0.69',3000))
# while True:
#     #接收客户端的请求
#     #第一个变量：是客户端的请求数据
#     #第二个变量：是客户端的IP地址和端口号
#     while True:
#         client,addr = s.recvfrom(1024)
#         print(client.decode('utf-8'))
#         #发送响应
#         msg = input('>>>')
#         s.sendto(msg.encode('utf-8'),addr)
#
# import day1
# day1.H().asd()









# import os
# a = os.getcwd()
# aa = os.listdir(a)
# for i in aa:
#     c = str(i)
#     d = c.endswith('.jpg')
#     if d == True:
#         os.remove(i)



























# def asd(x):
#     a = 0
#     for  i in  range(x+1):
#         a = a + i
#     return a
# c =  asd(123) + 2
# print(c)
#
# a = [123,13,[23,43,1],23,32]
# b = a.copy()
# a .append(100)
# print(a)
# print(b)























































# import  pymysql
# import  xlrd
# conn = pymysql.connect(host='192.168.0.88',
#                        port=3306,
#                        user='root',
#                        passwd='123456')
# m = conn.cursor()
# m.execute('use python_learn')
# a = open('C:\\Users\\hanwl\\Desktop\\a.txt','r',encoding='utf-8')
# b = a.readlines()
# for i in range(4):
#     w = b[i]
#     s = w.split(',')
#     if i == 0:
#         #continue
#         m.execute('create table ab({} char(20),{} int,{} char(20),{} char(20));'.format(s[0],s[1],s[2],s[3]))
#     else:
#         m.execute('insert into ab values("{}","{}","{}","{}");'.format(s[0],s[1],s[2],s[3]))
#     m.execute('select * from ab;')
# print(m.fetchall())
# a.close()








