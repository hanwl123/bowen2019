# !/usr/bin/puthon
# _*_coding:utf_8  _*_

import xlrd
def  shuju():
    num_1 = []
    f = xlrd.open_workbook(r'C:\Users\hanwl\PycharmProjects\untitled2\bbb.xlsx')
    sheet = f.sheets()[0]
    b = sheet.nrows
    for  i  in  range(b):
        num_1.append(sheet.row_values(i))
    return   num_1
if __name__ == '__main__':
    print(shuju())





















