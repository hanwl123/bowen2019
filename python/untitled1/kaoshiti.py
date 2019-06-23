#!/usr/bin/puthon
#_*_coding:utf_8  _*_
#1
# for i in range(1,10):
#      for j in range(1,i+1):
#       sum='{}*{}={}'
#       print(sum.format(i,j,i*j),end='\t')
#       if i == j:
#           print('')

#2
# a = input('>>>')
# b = a[::-1]
# num = 0
# for i in range(len(a)):
#   for j in range(0, 10):
#    if b[i] == str(j):
#     num += j * (10 ** i)
# print(num)
#3
# import os
# import xlwt
# os.mkdir('aaa')
# f = open('C:\\Users\\hanwl\\PycharmProjects\\untitled1\\aaa\\a.txt','w',encoding='utf-8')
# for i in range(1,10):
#      for j in range(1,i+1):
#       f.write('{}*{}={}\t'.format(i,j,i*j))
#      f.write('\n')
# f.close()

#4

# import  pymysql
# import  xlrd
# conn = pymysql.connect(host='192.168.0.200',
#                        port=3306,
#                        user='root',
#                        passwd='123456')
# m = conn.cursor()
# m.execute('use test')
# a = open('C:\\Users\\hanwl\\Desktop\\c.txt','r',encoding='utf-8')
# b = a.readlines()
# for i in range(4):
#  c = b[i]
#  s = c.split(',')
#  if i == 0:
#         #continue
#         m.execute('create table a({} char(20),{} int,{} char(20),{} char(20));'.format(s[0],s[1],s[2],s[3]))
#  else:
#         m.execute('insert into a values("{}","{}","{}","{}");'.format(s[0],s[1],s[2],s[3]))
#         m.execute('select * from a;')
# print(m.fetchall())
# a.close()

# import socket
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('192.168.0.56',3000))
# s.listen(5)
# while True:
#     client,addr = s.accept()
#     while True:
#         reg = (client.recv(1024))
#         print(reg.decode('utf-8'))
#         msg = input('>>>')
#         client.send(msg.encode('utf-8'))

# import smtplib
# import email.mime.multipart as mul
# import email.mime.text as text
# message = mul.MIMEMultipart()
# message['subject'] = 'python'
# message['from'] = 'lijp_1998@163.com'
# message['to'] = '825069672@qq.com'
# txt = """
# 河南是个好地方
# 广东人爱吃福建人
# 我姓xun
# 薰衣草的xun么
# 不是
# 是孙悟空的xun
# """
# tet = text.MIMEText(txt)
# att1 = text.MIMEText(open('kaoshiti2.py', 'rb').read(), 'base64', 'utf-8')
# att1["Content-Type"] = 'application/octet-stream'
# att1["Content-Disposition"] = 'attachment; filename="kaoshiti2.py"'
# message.attach(att1)
# message.attach(tet)
# smtp123 = smtplib.SMTP_SSL('smtp.163.com',465)
# smtp123.login('lijp_1998@163.com','li123456')
# smtp123.sendmail('lijp_1998@163.com','825069672@qq.com',message.as_string())
# smtp123.close()




# import requests
# import  re
# import json
# import xlwt
# url = 'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=653&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&=0&_v=0.80308920&x-zp-page-request-id=5c8f4da4d99d4804a7cfcc6af51cd95b-1557229106436-265543'
# head = {
#          'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
#         }
# res = requests.get(url,headers = head)
# html = res.content.decode('utf-8')
# qqq = json.loads(html)
# b = []
# for j in range(0,90):
#     a = qqq['data']['results'][j]['company']['name'],qqq['data']['results'][j]['jobName'],qqq['data']['results'][j]['salary'],qqq['data']['results'][j]['eduLevel']['name']
#     b.append(a)
# print(b)
# ff = xlwt.Workbook(encoding='utf-8')
# sheet = ff.add_sheet('zhilian')
# c = ['name','zhiwei','xinzi','wenping']
# for i in range(len(c)):
#     sheet.write(0,i,c[i])
# for k in range(len(b)):
#     for t in range(len(b[k])):
#         sheet.write(k+1,t,b[k][t])
# ff.save('d.xls')



# import  pymysql
# import  xlrd
# conn = pymysql.connect(host='192.168.0.200',
#                        port=3306,
#                        user='root',
#                        passwd='123456')
# m = conn.cursor()
# m.execute('use test')
# a = open('C:\\Users\\hanwl\\Desktop\\c.txt','r',encoding='utf-8')
# b = a.readlines()
# for i in range(4):
#  c = b[i]
#  s = c.split(',')
#  if i == 0:
#         #continue
#         m.execute('create table a({} char(20),{} int,{} char(20),{} char(20));'.format(s[0],s[1],s[2],s[3]))
#  else:
#         m.execute('insert into a values("{}","{}","{}","{}");'.format(s[0],s[1],s[2],s[3]))
#         m.execute('select * from a;')
# print(m.fetchall())



import  pymysql
import  xlrd
conn = pymysql.connect(host='192.168.0.200',
                       port=3306,
                       user='root',
                       passwd='123456')
f = xlrd.open_workbook('d.xls')
m=conn.cursor()
m.execute('use test')
sheet = f.sheets()[0]
# a = sheet.nrows
for i in range(sheet.nrows):
    b = sheet.row_values(i)
    if i == 0:
        #continue
        m.execute('create table b({} char(20),{} char(20),{} char(20),{} char(20));'.format(b[0],b[1],b[2],b[3]))
    else:
        m.execute('insert into b values("{}","{}","{}","{}");'.format(b[0],b[1],b[2],b[3]))
        m.execute('select * from b;')
print(m.fetchall())
































