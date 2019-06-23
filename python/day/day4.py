# !/usr/bin/puthon
# # _*_coding:utf_8  _*_
#上传文件
# import  paramiko
# qq = paramiko.Transport(('192.168.0.69'))
# qq.connect(username='root',password='123456')
# sftp = paramiko.SFTPClient.from_transport(qq)
# #从Linux上传到windows
# sftp.put()
# #从windows上传到Linux
# sftp.get()


#发送邮件
# import  smtplib
# import  email.mime.multipart as mul
# import  email.mime.text as text
# message = mul.MIMEMultipart()
# ff = ('854917004@qq.com')
# ww = ('lijp_1998@163.com','songzf_1996@163.com')
# message['subject'] = '13_text'
# message['from'] = ff
# #群发消息
# message['To'] = '.'.join(ww)
# txt = """
# 河南是个好地方
# 广东人爱吃福建人
# 我姓xun
# 薰衣草的xun么
# 不是
# 是孙悟空的sun
# """
#tet = text.MIMEText(txt)
# # att1 = text.MIMEText(open('day1.py', 'rb').read(), 'base64', 'utf-8')
# # att1 ["Content-Type"]='application/octet-stream'
# # att1 ["Content-pisposition"]='attachment';filename='da.py'
# # message.attach(att1)
# smtp123 = smtplib.SMTP_SSL('smtp.qq.com',995)
# smtp123.login('ff','upzlsevjtwmzbdbi')
# smtp123.sendmail('ff','ww',message.as_string())
# smtp123.close()






# import  smtplib
# import email.mime.multipart as mul
# import email.mime.text as  text

# message =  mul.MIMEMultipart()
# message['subject'] = ('python_test')
# message['from'] = ('854917004@qq.com')
# message['to'] = ('1346863457@163.com')
# txt = """
#
#
#
#
# """
# smtp123 = smtplib.SMTP_SSL('smtp.163.com',465)
# smtp123.login('854917004@qq.com','#shouqunama')
# smtp123.sendmail('dajhianren','shoujianren ',message.as_string())
# smtp123.close()



# import socket
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# s.bind(('192.168.0.60',3000))
# s.listen(3)
# while True:
#     client,addr = s.accept()
#     while True:
#         reg = client.recv(1024)
#         print(reg.decode('utf-8'))
#         msg = input('>>>')
#         client.send(msg.encode('utf-8'))

# import  smtplib
# import  email.mime.multipart as mul
# import  email.mime.text as text
# message = mul.MIMEMultipart()
# ff = ('lijp_1998@163.com')
# ww = ('854917004@qq.com','hanwl_1997@163.com','songzf_1996@163.com')
# message['subject'] = ('123')
# message['from'] = ('ff')
# message['to'] = '.'.join('ww')
# txt = """
# 我是一个小青龙啊小青龙
# 你是一个猪儿虫啊猪儿虫
# """
# smtp123 = smtplib.SMTP_SSL('smtp.163.com',465)
# smtp123.login('lijp_1998@163.com','li123456')
# smtp123.sendmail('ff','ww',message.as_string())
# smtp123.close()




# import  re
# a = 'vasv3qjbj5b23j1233bkj2b675'
# b = re.compile('[0-9]+[0-9]+')
# c = b.findall(a)
# print(c)
# print(len(c))


#
# class  asd():
#     def h(self):
#         print(1)
#     def w(self):
#         print(2)
# class  qwe():
#     def l(self):
#         print(3)
#         self.__d()
#     def q(self):
#         print(4)
#     def __d(self):
#         print(5)
# class   zxc(asd,qwe):
#     pass
# q = zxc()
# q.q()
# w = qwe()
# w.l()

# import  smtplib
# import email.mime.multipart as  mul
# import email.mime.text as text
# message = mul.MIMEMultipart()
# messagesubject = ['python']
# messagefrom = ['123856@qq.com']
# messageto = ['123456@qq.com']
# txt = """
#
#
# """
# tet = text.MIMEText(txt)
# smtp123 = smtplib.SMTP_SSL('smtp.163.com',465)
# smtp123.login('123446@qq.com',1347)
# smtp123.sendmail('12313@qq.com','456734@qq.com',message.as_string())
# smtp123.close()

#将execl表格写入txt中
# import xlrd
# p = xlrd.open_workbook('bb.xls')
# sheet = p.sheet_by_name('python')
# s =sheet.nrows
# d = open(r'C:\Users\hanwl\Desktop\d.txt','w',encoding='utf-8')
# for i in range(s):
#     a = sheet.row_values(i)
#     b = ','.join(a)
#     d.write(b)
#     d.write('\n')
# d.close()

#将txt文档写入execl表格中
# import  xlwt
# a = xlwt.Workbook('utf-8')
# sheet =a.add_sheet('python_text')
# with  open('C:\\Users\\hanwl\\Desktop\\a.txt','r',encoding='utf-8') as  f:
#  b = f.readlines()
# print(b)
# c = []
# for i in b:
#     s = b[i]
#     print(s)
#     q = s.split(',')
#     c.append(q)
#     print(c)
# for j in range(len(c)):
#     for k in range(len(c)):
#      sheet.write(j,k,c[j][k])
#a.save('a.txt')



# import   smtplib
# import email.mine.multipart.email as mul
# import email.mine.test as  test
# message = mul.MIMEMultipart()
# message['subject'] = ('python')
# message['from'] = ('发件人邮箱')
# message['to'] = ('收件人邮箱')
# txt = """
# 大家好
# 我是DJ喜羊羊
# 青青草原我最狂
# 嘟嘟嘟
# 嘟一嘟嘟
# 啊 嘟一嘟嘟
#
# """
# tet = txt.multipart(text)
# smtp123 = smtplib.SMTP_SSL(smtp,'163.com','465')
# smtp123.login('发件人的邮箱','1234234')
# smtp123.sendmail('发件人的邮箱','收件人的邮箱',message.as_string)


# import   socket
# s = socket.socket(socket.AF_INET.socket.SOCK_STRAM)
# s.bild(('57467463'))
# s.listen(3)
# while  True:
#     client,addr = s.accept()
#     while True:
#         reg = client.recv('1024')
#         print(reg.decode('utf-8'))
#         msg = input('>>>')
#         client.encode('utf-8')

# import socket
# sock = socket.socket(socket.AF_INET.socket.SOCK_STRAM)
# sock.connect(('565767'))
# while True:
#     qq = input('>>>')
#     sock.send(qq.encode('utf-8'))
#     msg = sock.recv('1024')
#     print(msg.decode('utf-8'))





# def  zhishu(a,b):
#  sum = 0
#  for  i  in  range(a,b+1):
#     num = 0
#     for j  in  range(a,i+1):
#         if  i % j ==0:
#          num = num +1
#     if num == 2:
#          sum = sum + i
#          print(sum)
# zhishu(1,100)
































































































