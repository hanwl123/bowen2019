#!/usr/bin/puthon
#_*_coding:utf_8  _*_
# import  socket
# sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# sock.connect(('192.168.0.56',3000))
# while True:
#     qq = input('>>>')
#     sock.send(qq.encode('utf-8'))
#     ww = sock.recv(1024)
#     print(ww.decode('utf-8'))

# import requests
# import re
# url = ('https://www.qiushibaike.com/imgrank/')
# res = requests.get(url)
# html = res.content.decode('utf-8')
# hh = re.compile('<img src="//pic.qiushibaike.com/system/(.*?).jpg"')
# ww = hh.findall(html)
# print(len(ww))
# for i in ww:
#     j = ('https://www.qiushibaike.com/imgrank/'+i+'.jpg')
#     print(j)

 #j = 'https://pic.qiushibaike.com/system/pictures/'+i+'.jpg'



import requests
import  re
import json
import xlwt
url = 'https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=653&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&=0&_v=0.80308920&x-zp-page-request-id=5c8f4da4d99d4804a7cfcc6af51cd95b-1557229106436-265543'
head = {
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0'
        }
res = requests.get(url,headers = head)
html = res.content.decode('utf-8')
qqq = json.loads(html)
b = []
for j in range(0,90):
    a = qqq['data']['results'][j]['company']['name'],qqq['data']['results'][j]['jobName'],qqq['data']['results'][j]['salary'],qqq['data']['results'][j]['eduLevel']['name']
    b.append(a)
print(b)
ff = xlwt.Workbook(encoding='utf-8')
sheet = ff.add_sheet('zhilian')
c = ['name','zhiwei','xinzi','wenping']
for i in range(len(c)):
    sheet.write(0,i,c[i])
for k in range(len(b)):
    for t in range(len(b[k])):
        sheet.write(k+1,t,b[k][t])
ff.save('d.xls')






















