# !/usr/bin/puthon
# _*_coding:utf_8  _*_
def read():
    with open(r'C:\Users\hanwl\PycharmProjects\untitled2\Tim\data\data2') as f:
        a = []
        b = f.readlines()
        for i in b:
            a.append(i.replace('\n', '').split(','))
    return a
print(read())












