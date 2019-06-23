# !/usr/bin/puthon
# _*_coding:utf_8  _*_
import   xlrd
def shuju():
    a = xlrd.open_workbook(r'C:\Users\hanwl\PycharmProjects\untitled2\aaa.xlsx')
    sheet = a.sheets()[0]
    b = []
    c = sheet.nrows
    for  i in  (c):
        b.append(sheet.row_values(i))
    return   b
if  __name__ == '__mian__':
    print(shuju())











