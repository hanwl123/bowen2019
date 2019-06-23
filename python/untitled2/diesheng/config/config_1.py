# !/usr/bin/puthon
# # _*_coding:utf_8  _*_
#定义一个读取.txt 文件的函数
def  read_data():
    datas = []
    with  open('C:\\Users\\hanwl\\PycharmProjects\\untitled2\\diesheng.py\\data\\data_1','r') as  f:
        d = f.readlines()
        for  i  in  d:
            datas.append(i.replace('\n','').split(','))
        return datas
print(read_data())



















