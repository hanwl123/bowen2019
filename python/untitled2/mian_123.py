# !/usr/bin/puthon
# _*_coding:utf_8  _*_
#  driver   中主要是控制跑回归测试时只跑那些模块的用例


from  report import  B_gao

with  open   ('a.txt','r')  as   fb:
    a = fb.readlines()
    if  'all'  in  a :
           B_gao('*')
    else:
           B_gao(a)






























