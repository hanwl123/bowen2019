# !/usr/bin/puthon
# # _*_coding:utf_8  _*_
# def  a(x,y):
#     for i in  range(len(x)):
#         for j in range(len(x)):
#             if x[i] != x[j]:
#                 c = x[i] + x[j]
#                 if  c  == y:
#                    if x[i]<x[j]:
#                     print(x[i],x[j])
# a([12,13,14,15],27)

# import  xlrd
# f = xlrd.open_workbook(r'bb.xls')
# a = f.nsheets
# print(a)
# sheet = f.sheets()[0]
# b = sheet.row_values(0)
# print(b)




#客户端：
# import  socket
# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.connect(('192.168.0.60',3000))
# while True:
#     qq = input('>>>')
#     sock.send(qq.encode('utf-8'))
#     ww = sock.recv(1024)
#     print(ww.decode('utf-8'))


# def  asd(x,y,z):
#     if  y + z < len(z):
#         for  i in range (z):
#          x.remove(x[y])
#     elif y + z >= len(x):
#         for j in range (len(x)-y):
#          x.remove(x[y])
#     print(x)

import requests
import  re
url = 'https://movie.douban.com/top250'
res = requests.get(url)
html = res.content.decode('utf-8')
#过滤
a = []
patt = re.compile(' <img width="100" alt="(.*?)"')
itesms = patt.findall(html)
print(itesms)
a.extend(itesms)
p = re.compile('https://img(.).doubanio.com/view/photo/s_ratio_poster/public/(.*?)class=""')
s = p.findall(html)
print(s)
b = 0
for  i in s:
     bb ='https://img{}.doubanio.com/view/photo/s_ratio_poster/public/{}'.format(i[0],i[1])
     #aa = bb.findall(i)
     print(bb)
     msg = requests.post(bb)
     hh = msg.content
     with open('{}.jpg'.format(a[b]),'wb') as  f:
         f.write(hh)
     b = b+1

































































































