# !/usr/bin/puthon
# _*_coding:utf_8  _*_
a =input('账户余额')
a = int(a)
product_good= [
    ['电脑',1999],
    ['鼠标',10],
    ['游艇',20],
    ['美女',998],
  ]
shopping_car=[]
for  i,j in enumerate(product_good):
     print(i,j)
while True:
    for  i,j in enumerate(product_good):
         b = input('请输入商品序号')
         c = int(b)
         if  c >= 0  and  c <= len(product_good):
            print(product_good[c])
            shopping_car.append(b)
            print('添加成功')
            if  c >=4:
                break
         
            # print('总共添加的商品{}'.format(shopping_car[c]))
            # #v= int(shopping_car)
            # for i in shopping_car:
            #     m = shopping_car.pop(i)
            #     print('y或n')
            q = j[c]
            w = int(q)
            if  w < a:
                print('已购买')
                d = a - w
                print('剩余金额:%d' %d)
                if  d < w :
                 print('余额不足请充值')
                g =int(input('充值金额'))
                if g > 0:
                 d +=g
                 print('充值成功剩余金额:%d' %d)
                 
















































































