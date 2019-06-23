#!/usr/bin/puthon
#_*_coding:utf_8  _*_
#print('hello',123,0)
# a = input('请输入密码：')
# print(a)

#a=3
#b=4
#c=5
#print(a,b,c)
#
#rint(a+2)
#="a"
#print(type(a))
#a="jhopjhm"
#print(a[1::4])

#改大小写\
# a='wqe'
# e=a.upper()
# print(e)

#替换
#a='qwrqwre'
#b=a.replace('q','g')
#print(b)

#分割
#a='qwreqwrfg'
#b=a.split('wr')
#print(b)

#空格替换
#a='swrrwe wqe we'
#b=a.replace(' ','')
#print(b)
#a=' adfqfqw'
#b=a.lstrip()
#print(b)

#连接
#a='awersfa'
#b=a.split('er')
#print(b)
#c='__'.join(b)
#print(c)

#连接
#a= ['wqe','qwsad','qwe']
#b='=='.join(a)
#3print(b)
#c=b.split('q')
#print(c)

#格式化
#a = 1
#b = 'user{}'.format(b)

#格式化
#a='affdw{name}adff{age}dff{sex}'
#b=a.format(age=90,name='da',sex='xiao')
#print(b)
#c=b.split('ff')
#rint(c)
#d='--'.join(c)
#print(d)


#a = 'hello%s,今年%d岁了,你个大%s'
#b = a%('美女',18,'傻嗨')
#print(b)

#获取某个字符串的下标位置
#a = 'ahgewohg'
#b = a.index('w')
#print(b)
#c = a.count('h')
#print(c)

#len  获取字符串的总共个数
#a = 'dfeergwer'
#print(len(a))
#大小写
# a=' eepgfweghw '
# b =a.  upper()
# print(b)
# c = b.split('WE')
# print(c)
# d = b.replace('GF','kk')
# print(d)
# e = d.strip()
# print(e)
# f ='_'.join(a)
# print(f)
# g = f.count('p')
# print(g)
# h = a.index('e')
# print(h)
# print(len(a))



#分割
# a = 'egergwerfwe'
# b = a.split('er')
# print(b)

#替换
# a = 'egergwerfwe'
# # b = a.replace('er','km')
# # print(b)

#删除
# a = 'egergwerfwe'
# b = a.replace('er','')
# print(b)
#除左右空格
# a = '  egergwerfwe  '
# b = a.strip()
# print(b)
#替换中间空格
# a = 'wegwe fwqe qfd '
# b = a.replace(' ','' )
# print(b)
#判断以什么开头
# a = 'egergwerfwe'
# b = a.endswith('we',)
# print(b)
#连接格式化
# a = 'jga%sgeg%dgweg%s'
# b = a%('w',2,2)
# print(b)


#index
# a = 'egergwerfwe'
# print(len(a))
# #count

# a = 'egergwerfwegw'
# b = a.replace('gw','kk',1)
# print(b)

# a = 'e'
# b = a.upper()
# print(b)
# bowen = [123,'大','小']
# print(type(bowen))
# bowen = list('123')
# print(type(bowen))


#添加一个值默认在最后一位
# bowen = [1,1,2,3,'大','小','中']
# bowen.append(1)
# print(bowen)



#删除指定值默认第一个
# bowen = [0,1,2,3,'大','小','中']
# bowen.remove(1)
# print(bowen)


#指定位置删除（索引）
# bowen = [1,1,2,3,'大','小','中']
# bowen.pop(100)
# print(bowen)

#排序
# abc = [1,4,5,7,3,2]
# abc.sort()
# abc.reverse()
# print(abc)


#倒序：先升序再倒序
# abc = [1,4,5,7,3,2]
# abc.sort()
# abc.reverse()
# print(abc)

# bowen = [1,'大','小','中']
# f=bowen.count('大')
# print(f)

# hanwl = [1,7,3,54,'sda']
# # print(hanwl[::2])
# #
# #print(hanwl[2::])
# #
# print(hanwl[2])
# #
# print(hanwl[:2])
# #
# print(hanwl[4:])
#
# print(hanwl[4::])
#
# print(hanwl[::2])
# a = [2,3,5,3,6,9,5]
# a.insert(2,0)
# print(a)

# a = [2,3,5,3,6,9,5]
# a.remove(2)
# print(a)

# a = [2,3,5,3,6,9,5]
# a.pop(2)
# print(a)# a = [2,3,5,3,6,9,5]

#更改  重新赋值
# a = [2,3,6,9,5]
# a[1]=20
# print(a)
#将两个列表合并到一起
# a = [2,3,5,3,6,9,5]
# b = [9,7,5,7,]
# a.extend(b)
# print(a)


#浅复制
# a = [6,9,5]
# b = [2,3,45,a]
# f=b.copy()
# a.append(100)
# b.append(20000)
# print(b)
# print(f)


#深复制
# import copy
# a=[2,3,4]
# b=[5,6,9,a]
# ff=copy.deepcopy(b)
# b.append(1000)
# print(b)
# print(ff)

#元组
# a = (2,4,3,'ad','af')
# print(type(a))

#统计某元组的某个字符个数
# a=(4,12,4)
# b=a.count(4)
# print(b)

#获取某元组的下标位置
# a=(2,4,67)
# b=a.index(4)
# print(b)


#统计某元组的个数
# a=(2,34,5,4,6,7)
# print(len(a))


#字典

#添加键值对
# a={'name':'小明','age':'18',}
# b={'p':123,'w':456}
# a['sex']='男'
# print(a)

#删除  pop 删除某个键值对

# a.pop('age')
# print(a)

#默认删除最后一个键值对
# a.popitem()
# print(a)

#获取所有的键
# b = a.keys()
# print(b)
#获取所有的值
# b = a.values()
# print(b)

#获取所有的键值对
# b = a.items()
# print(b)

#将b中的所有键值对更新到a中
# a.update(b)
# print(a)

#集合
#a= {12,3,'name',565,6,6,'fsa'}

# #添加
# a={12,3,43,4,'we'}
# a.add(('qwe',123))
# print(a)
#删除

# a.remove(12)
# print(a)

#随机删除一个
# a.pop()
# print(a)

#更新
#b={1,23,3}
# a.update(b)
# print(a)

#并集
#print(a|b)
#交集
#print(a&b)
#补集
#print(a-b)

# b = 123
# b = str(b)
# print(type(b))
# a = '{}*{}={}'
# b = a.format(12,21,21*12)
# print(b)

# a = '%d*%d=%d'
# b =  a%(12,21,12*21)
# print(b)
#占位符


# 运算符
# +，- ，* ，/(完全除)，//整除，%（求余数）
# a = 9 / 4
# print(a)
# 比较运算符
# >,<,>=,<=,==,!=
# 赋值运算符
# +=，-=，*= ，/=(完全除)，//=整除，%=（求余数）
# 成员运算符
#  in  ，not in
# 逻辑运算符
# and  or   not

# 单分支
# a = input('>>>')  # 手动添加为字符串  需要更改相对应的数据类型
# a = int(a)
# if a > 3:
#     print('hello')
#
# 双分支
# a = 8
# if a > 3:
#     print('hello')
# else:         #不能跟条件
#     print('hi')
#
# 多分支判段语句
# a = input('>>>')
# a = int(a)
# if a >= 90:
#     print('优秀')
# elif 80 < a and a < 90:
#     print('良')
# elif 70 < a and a < 80:
#     print('及格')
#
# 嵌套判断
# a = 6
# if a%2==0:   # 满足第一个条件后进行下一个条件
#      if a%3==0:  #
#       print('hello')


# 1.既能除以2又能除以3  打印hello
# 2.能除以2但不能除以3   打印 world
# 3.不能除以2但能除以3  打印  hi
# 4.都不能  打印123
# a = input('>>>')
# a =int(a)
# if a%2==0:
#     if a%3==0:
#      print('hello world')
#     else:
#      print('hello')
# elif a%3==0:
#     print('world')
# else:
#     print(123)
#
# 循环语句
# num=0
# for i in range(1,101,1):
#   num=num+i
# print(num)
# 1-2+3-4+5....+100
# num=0
# for i in range(1,100,1):
#  if i%2==0:
#   num=num-i
#  else:
#     num=num+i
# print(num)
#
#
# 循环嵌套语句
# import  random
# a = random.randrange(1,10)
# for i  in range(1,4):
#     q= input('>>>')
#     q= int(q)
#     if q==a:
#         print('恭喜')
#         break
#     elif q > a :
#        a='小了小了，还有{}次机会'
#     print(a.format(3-i))
#     a= '还有{}次机会'
#     print(a.format(2- i))
# else:
#   print('菜')
# for   elae   语句
# a = [12,35,6,]
# for i in enumerate(a):
#     print(i)
#
# 九九乘法表
# for i in range(1,10):
#      for j in range(1,i+1):
#       sum='{}*{}={}'
#       print(sum.format(i,j,i*j),end='\t')
#       if i == j:
   #        print('')

#一百之内的质数之和
# sum=0
# for i in range(2,101):
#     for  j  in  range(2,i+1):
#       if i%j==0:
#        break
#       elif i==j:
#        sum=sum+i
# print(sum)

#100-1000之内的水仙花数
# for i in range(100,1000):
#      a=i//100
#      b=i//10%10
#      c=i%10
#      d=a**3+b**3+c**3
#      if i == d:
#       print(i)

#一千之内的因数和等于本身的数
# def a(b):
#  for i in range(1,b):
#     sum=0
#     for j in range(1,b+1):
#      if j<i:
#        if i%j==0:
#         sum=sum+j
#         if sum==i:
#          print(sum)
# a(1000)
# #阶乘之和
# a = 1
# b = 0
# c=input('>>>')
# c=int(c)
# for i in range(1,c+1):
#     a=a*i
#     b=b+a
# print(b)


#任意一个数判断是否是回文数
# a =input('字符串')
# if a == a[::-1]:
#     print('是回文数')
# else:
#     print('不是回文数')

#11.	打印列表中所有第一大和第二大的数
# a = input('数组')
# b = a.split(',')
# c =[]
# d = b.count(b[-1])
# for i in range(1,d+1):
#     c.append(b[-1])
#     b.remove(b[-1])
# g = b.count(b[-1])
# for j in range(1,g+1):
#     c.append(b[-1])
#     b.remove(b[-1])
# print(c)
# print(b)


#21.用100买鸡
# for x in range(1,100//2+1):
#     for y in range(1,100//1+1):
#         z = 100 -x-y
#         if (2*x+1*y+z/2==100) and z%0.5==0:
#                 print(x,y,z)

# #17.
# a = input('>>>')
# b = a.split(',')
# b = [int(i) for i in b]
# d = max(b)
# b.remove(d)
# b.append(d)
# c = min(b)
# b.remove(c)
# b.insert(0,c)
# print(b)

# a.remove(a[-1])
# e = min(a)












#18.	一个有顺序的列表，随机加入一个数，加入的数在正确的位置
# a = input('>>>')
# a = a.split(',')
# a= [int(b) for b in a]
# import  random
# b = random.randrange(1,10)
# a.append(b)
# for  i  in  range(len(a)):
#    for j in  range(len(a)-1):
#        if  a[i] <= a[j]:
#            t=a[i]
#            a[i]=a[j]
#            a[j]=t
# print(a)






# a = input('>>>')
# a = a.split(',')
# a = [int(b) for  b  in a]
# for  i  in  range(len(a)):
#    for j in  range(len(a)-1):
#        if  a[i] <= a[j]:
#            t=a[i]
#            a[i]=a[j]
#            a[j]=t
#        print(a)

#十进制转十六进制
# 31/16=1...15
# 1/16=0....1
# a = input('数字')
# ff = [str(i) for i in  range(10)] + ['a','b','c','d','e','f']
# c = ''
# while  True:
#     b = a % 16
#     c = c + ff[b]
#     a = a // 16
#     if a ==0:
#         break
# print(c[::-1])








 # a = [int(b) for  b  in a]
# for  i  in  range(len(a)):
#    for j in  range(len(a)-1):
#        if  a[i] <= a[j]:
#            t=a[i]
#            a[i]=a[j]
#            a[j]=t
#        print(a)
#whlie
# a = 4
# while  a > 2:
#     print('hello')
#     a = a - 1


#whlie 1+100的和
# a = 0
# i = 0
# while a < 100:
#   a = a + 1
#   i = a + i
# print(i)


#22.while True:
    # a = input('请输入一个数组')
    # a = a.split(',')
    # for i,j in enumerate(a):
    #     a[i]=int(j)
    # b=sum(a)//len(a)
    # if a[0] < 0:
    #     break
    # print('平均数为{}'.format(b))
    # for k in a:
    #     if k  <  b:
    #         print('低于平均数的有{}'.format(k))


# 列表推导式

    # a = input('请输入一个数组')
    # a = a.split(',')
    # a= [int(i) for i in a ]
    # b= sum(a) / len(a)
    # if a[0]< 0:
    #    break
    # print('平均数为{}'.format(b))
    # p=[ k for k in a  if k < b ]
    # print(p)
# 去重
# a=[12,1,21,23,13,12]
# for i in a:
#      b = a.count(i)
#      print(b)
#      if b > 1:
#          for  j  in  range(b-1):
#           a.remove(i)
# print(a)

#第二种
# a = [12,23,12,2,34,2]
# b= []
# for i in a:
#     if i not in  b :
#       b.append(i)
# print(b)

#18.	一个有顺序的列表，随机加入一个数，加入的数在正确的位置

# 对文件进行操作   增删改查
#当前路径下
#f = open('a.txt','w',encoding=utf-8)
#要不是加路径
#f = open('C:\\Users\\hanwl\\Desktop\\b.txt','w',encoding='utf-8')
#  \t  不想当制表符 只是一个字符串
#a= 'qrf\\topwq'
#print(a)
#加文件路径用两个反斜杠
#或者路径前面加小写r
#f = open(r'a.txt','w',encoding='utf-8')
#权限   w 写入 r 读取  a 追加
#  只要使用的写的权限  对文件进行操作时
#如果没有这个文件，先创建在写入
#有文件时直接进行操作
#write(字符串)   给文件写入数据
# f = open('C:\\Users\\hanwl\\Desktop\\b.txt','w',encoding='utf-8')
# for  i  in  range(10):
#      f.write('setgwerg\n')
# #不换行
# #关闭文件
# f.close()


# f = open('C:\\Users\\hanwl\\Desktop\\b.txt','w',encoding='utf-8')
# for i in range(1,10):
#      for j in range(1,i+1):
#       f.write('{}*{}={}\t'.format(i,j,i*j))
#      f.write('\n')
# f.close()





# f = open('C:\\Users\\hanwl\\Desktop\\a.txt','r',encoding='utf-8')
# a=f.readlines()
# for i in range(len(a)-1):
#     if  a[i]=='\n':
#         a.remove(a[i])
# for j in range(len(a)):
#         b =a[j].startswith('#')
#         if b == True:
#          a.remove(a[j])
# print(len(a))
# f.close()



# f = open('C:\\Users\\hanwl\\Desktop\\a.txt','r',encoding='utf-8')
# a=f.readlines()
# c = len(a)
# print(c)
# for i in range(c-1):
#     b =  a[i].startswith('#')
#     if  a[i]=='\n':
#      c=c-1
#     elif  b == True:
#      c =c-1
# print(c)
# f.close()



#读取
# f = open('C:\\Users\\hanwl\\Desktop\\b.txt','r',encoding='utf-8')
# #读取文件中的 所有内容，结果是个列表
# #文件中的每一行，是文件中的每一个元素
# b=f.readlines()
# #读取文件中的 所有内容，结果是个字符串
# # b = f.read()
# #读取文件中的每一行 随着每一次的读取而读取下面的一行
# #b = readline()
# print(b)
# f.close()

 #将a.txt的文档中的以abc开头的打印出来
# f = open('C:\\Users\\hanwl\\Desktop\\a.txt','r',encoding='utf-8')
# b = f.readlines()
# for i in b:
#      if i[:3]=='abc':
#        print(i)
#
# for  i  in  range(21):
#     b= f.readline()
#     if  i >= 15:
#       print(b)

#判断是否为三角形
# a = input('>>>')
# a = int(a)
# b = input('>>>')
# b = int(b)
# c = input('>>>')
# c = int(c)
# if  a+b+c==180:
#    print('是一个三角形')
# else:
#    print('不是一个三角形')

#冒泡法排序
# a = input('>>>')
# a = a.split(',')
# a = [int(b) for  b  in a]
# for  i  in  a
#    for j in  range(len(a)-1):
#        if  a[j] > a[j+1]:
#            t=a[j]
#            a[j]=a[j+1]
#            a[j+1]=t
# print(a)


#选择法排序
# a = input('>>>')
# a = a.split(',')
# a = [int(b) for  b  in a]
# for  i  in  range(len(a)):
#    for j in  range(len(a)-1):
#        if  a[i] <= a[j]:
#            t=a[i]
#            a[i]=a[j]
#            a[j]=t
#        print(a)


#打印列表中所有第一大和第二大的数
# a = input('>>>')
# a = a.split(',')
# for  i  in  range(len(a)):
#    for j in  range(len(a)-1):
#        if  a[i] >= a[j]:
#            t=a[i]
#            a[i]=a[j]
#            a[j]=t
# print(a[0:2])

#一个有顺序的列表，随机加入一个数，加入的数在正确的位置
# a = input('>>>')
# 不用int将字符串变成整数
# a = input('>>>')
# num = 0
# for  i,j  in enumerate(a):
#    for b in  range(0,10):
#         if  j==str(b):
#          num += j * (10 ** i)
# print(num)


#不用int将字符串改为整数
# a = input('>>>')  # ‘123’
# b = a[::-1]    #先表示出百位 1*10**2   十位 2*10**1  个位  3*10**0
# num = 0        反转之后  b[0]=3  b[1]=2  b[2]=1
# for i in a:
#   for j in range(0, 10):
#    if b[i] == str(j):
#     num += j * (10 ** i)
# print(num)
#


#任意四个数字，组成三个不同的三位数
# r = []
# for i in range(1,5):
#
#     for j in range(1,5):
#
#         for k in range(1,5):
#
#             r.append(i*100+j*10+k)
# print(set(r))


#将列表中的元素向左移动一位
# a = [i for i in range(10)]
# b = a.pop(0)
# a.append(b)
# print(a)







#追加a
#w,r,a
#r+  w+  a+ 既能读又写
#wb  rb  ab   以二进制的方式读取和写入
# f = open('a.txt','a',encoding='utf-8')
# f.write('asd123')  #write 的写入不换行
# f.close()
# f = open('C:\\Users\\hanwl\\Desktop\\a.txt','rb',)
# print(f.read())
# f.close()
# f = open('C:\\Users\\hanwl\\Desktop\\kaida\\image\\123.jpg','rb')
# b= f.read()
# # print(b)
# ff = open('C:\\Users\\hanwl\\Desktop\\kaida\\image\\1234.jpg','wb')
# ff.write(b)
# print(ff)
# ff.close()
#文件路径 权限 编码方式   with
#with   语句   上下文管理器
#自动释放占用的资源
#自动关闭文件


#格式     with  要操作的对象  as 变量名：    执行语句  # 注意缩进
#_enter_进入   —exit—退出
# with open('C:\\Users\\hanwl\\Desktop\\a.txt','r+',encoding='utf-8')  as  f:
#     b= f.read()
#     f.write('qwl1234214')
# print(b)

#报错内容
#第一行： 报错的位置
#第二行： 报错的语句
#第三行： 报错的类型和描述


#函数：可重复使用的，具有某种功能的代码块
#内置函数
#自定义函数：自己写的函数
#格式 def  函数名()：语句块
#函数的名字是： a   函数的功能是： 1-100的和
#函数名的命名规则：
#1.只能是字母，数字，下划线组成
#2.不能以数字开头
#3.不能命名为语言内部命令
#  默认  4.函数命名跟功能相近的英文
# def  a():
#      b = 0
#      for i in range(101):
#          b=b+i
#      print(b)
# a()
#2.变量的作用域
# 分类：局部变量    全局变量
#局部变量只作用于函数内部
#
# b = 1         #作用于整个文件
# def  a():
#     global b  # 将局部变量变成全局变量
#     b = 0     # 局部变量在函数内部
#     print(b)
# a()
# print(b)
#

#3.传参
# 定义函数： def 函数名（）：
# 执行语句块
#参数的个数是任意的
#必须参数：使用函数时必须传入数据的参数
# def a(x):
#     a = sum(range(x+1))
#     print(a)
# for i in range(10,41,10):
#     a(i)
#默认参数：
# def 函数名（参数名==值）：
# 执行语句
# def bas(b = 100):
# #     a = 0
# #     for i in range(b+1):
# #         a = a+i
# #     print(a)
# # bas()

#必须参数
#通过传参计算任意范围的指数之和
# def wd(a,b):
#  sum = 0
#  for i in range(a,b+1):
#     for  j  in  range(2,b):
#          if i%j==0:
#              break
#     if i==j:
#           sum=sum+i
#  print(sum)
# wd(3,100)




#默认参数
# def wd(a,b）:
#  sum = 0
#  for i in range(a,b+1):
#     for  j  in  range(2,b):
#          if i%j==0:
#              break
#     if i==j:
#           sum=sum+i
#  print(sum)
# wd()

#可变长参数参数2.使用函数时可以传入多个参数
# def asd(*a):# 将这些数据放在一个元组中
#     print(a)
# asd(123,'321','qwr')

#
# def asd(**a):# 将这些数据放在一个字典  键值对的形式  **默认的  kwargs
#     print(a)
# asd(name=123,sex='nan',)


#优先级：  必须参数》默认参数》可变长参数
# def asd(*a):# 将这些数据放在一个元组中
#     print(a)
# asd(123)

# return:1.结束函数
#        2.赋值
# 1.结束函数
# def asd():
#     print('a')
#     return
#     print('b')
# asd()

# 2.赋值
# 第一步：1-任意数的和
# 第二部：1-任意数的和+2，要求不允许改变函数的
# def bas(b):
#     a = 0
#     for i in range(1,b+1):
#        a = a+i
#     return a
# for  i in range(10,41,10):
#     c = bas(i) + 2
#     print(c)

# def bas(b):
#     a = 0
#     for i in range(1,b+1):
#        a = a+i
#     print(a)
#     return a
# asd(100)调用函数=none
# asd(100) = return  数据  =  数据
# c = bas(10)
# print(c)


#函数计算器：两个数字的加减乘除+，-，*，|
# def  jia(a,b):
#     jia = a+b
#     print(jia)
# def jian(a,b):
#     jian = a-b
#     print(jian)
# def cheng(a,b):
#     cheng = a*b
#     print(cheng)
# def chu(a,b):
#     chu = a//b
#     print(chu)
# chu(21,3)


# 5.lamdba  匿名函数  是一个简单的表达式，只能做一些逻辑结构简单的代码块

# a = lambda  x,y : x+y
# print(a(12,12))


#函数计算器：两个数字的加减乘除+，-，*，|
# a = lambda  x,y : x+y
# b = lambda  x,y : x-y
# c = lambda  x,y : x*y
# e = lambda  x,y : x/y
# # while true:
# s =  input('>>>')
# if '-' in s:
#     d = s.split('-')
#     print(b(int(d[0]),int(d[1])))
# elif '+' in s:
#     d = s.split('+')
#     print(a(int(d[0]),int(d[1])))
# elif '*' in s:
#     d = s.split('*')
#     print(c(int(d[0]),int(d[1])))
# elif '/' in s:
#     d = s.split('/')
#     print(e(int(d[0]),int(d[1])))


# 自定义一个函数，给这个函数三个参数
#第一个参数是字符串
#第二个和第三个参数是数字
#删除这个字符串从第二个数字为下标位置删除第三个数字
# def  bas(x,y,z):
#     b = x.split(',')
#     x = list(x)
#     print(b)
#     for i  in  range(y,y+z):
#         c =x .pop(y)
#         print(c)
#     d = '-'.join(x)
#     print(d)
# bas('abcdefg',2,2)
#
#
# def  bas(x,y,z):
#     x = list(x)
#     d = y + z
#     if d>len(x):
#         d=len(x)
#     for i  in  range(y,d):
#         x .pop(y)
#     x = str(x)
#     d = '-'.join(x)
#     print(d)
# bas('abcdefg',2,2)
#


#
# def  asd():
#     print('hello')
# asd()
#
# def  qwe():
#     print(123)
# qwe()
# #判断正在执行的文件，是否是本文件
# if __name__ == '__main__':
#     for  i in range(10):
#         print(i)




#tcp客户端

import  socket
#创建一个套接字
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#连接服务器
sock.connect(('192.168.0.56',3000))
#将qq当做请求发送给服务器
while True:
    qq = input('>>>')
    sock.send(qq.encode('utf-8'))
    #接收响应
    ww = sock.recv(1024)
    print(ww.decode('utf-8'))



#udp客户端
# import socket
# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# host = ('192.168.0.69',3000)
# while True:
#     msg = input('>>>')
#     s.sendto(msg.encode('utf-8'),host)
#     #接收响应
#     reg = s.recv(1024)
#     print(reg.decode('utf-8'))



#正则表达式
#匹配文件中的字符串
#自己写的正则表达式对于python来说，
#python不认识
#需要将正则表达式转换成python能够识别的正则表达式
#正则表达式的模块

#贪婪模式：尽可能多的去匹配符合条件的内容
# a = 'awrqqwe12sfgs34das12efrwe34'
# b = re.compile('12(.*)34'
#打印出来的是尽可能匹配多的 12 开始   34 结尾的所有的中间数

#非贪婪模式：尽可能匹配少的符合条件的内容(?)
# a = 'awrqqwe12sfgs34das12efrwe34'
# b = re.compile('12(.*?)34'
#打印出来只要符合条件的先拿出来  然后在去匹配下一个符合条件的


# import  re
# #将字符串转换成正则表达式
# a = 'awrqqwe12hoi34ho12qwe34erfwe34'
# #将正则表达式编译成python能够识别的正则语言
#  . :匹配任意一个字符，除了换行符之外的
#  加上匹配换行符在内的权限  re.S
# b = re.compile('12(.*?)34')       #过滤出来以什么开头结尾的中间的东西
# #拿着编译之后的正则到字符串中去查找
# #查找所有符合条件的字符，结果手机一个列表
# c = b.findall(a)
# print(c)


# import  re
# a = 'wqade\nqwe'
# #  . :匹配任意一个字符，除了换行符之外的
# #  加上匹配换行符在内的权限  “re.S”   给  .  加上匹配成有换行符的功能的  re.I 不区分大小写
# b = re.compile('wq(.*?)we',re.S)
# c = b.findall(a)
# print(c)


# import  re
# a = 'wqadeqwe'
# #findall  除了查找，本身就具有编译的功能
# c = re.findall('w(.*)w',a)
# print(c)

#替换   sub
# import  re
# a = ['wqa123d','1231e4123q2','we134']
# #替换
# #第一个参数：通过正则过滤出来的被替换的字符
# #第二个参数：替换成的字符
# #第三个参数：要被替换的文件中的东西
# for  i  in a:
#     #把所有的数字替换成‘qwe’
#  c = re.sub('[0-9]+','qwe',i)
#  print(c)



#python的函数

# print(hex(123))     #十进制转换成16进制
# print(oct(123))     #十进制转换成8进制
# print(bin(123))     #十进制转换成2进制
# print(int(0x12))    #任何数转换成10进制


#chr  将数字转化为accssi 表对应的字符
# a = [chr(i) for i in range(97,103)]
# print(a)

#ord将asill中的字符转化为 对应的数字
#print(ord('.'))

#最大值  最小值  求和
# a = [123,123,44,12]
# print(max(a))
# print(min(a))
# print(sum(a))


#整除求余   divmod
#第一个参数：是整数
#第二个参数：是余数
# a,b = divmod(100,16)
# print(a,b)


#面向对象 ：将函数进行分类和封装，使开发更高效

#1.定义一个类    class  类名：
#   属性，方法（函数）
#默认首字母大写
#调用   在本文件中调用类名().函数名()  H().asd()
#调用   不在本文件中  加上 文件名 day1().类名().函数名()
#2.类的实例（对象）
#将类名()赋值给一个变量
#H  此时的H是    类的实际例子（对象） 是方便在类的外部调用其他函数
#  self  不是函数的参数，
#  self是类的实例，它的存在方便类的“内部”调用其他函数
#3.继承
#括号中是要写继承的类
# 新的类会继承旧的类中的所有函数   继承上一个函数
# class  H():
#     def  asd(self):
#         print('hello')
#     def  qwe(self):
#         print(123)
#         self.asd()
# class jkl(H):
#     pass
# q = jkl()
# q.asd()
#多继承：一个类可以继承多个类  用逗号隔开
# 有相同的函数名是  从左往右开始算起 匹配到符合就打印第一个 新的类会继承旧的类中的所有函数
#4.多态 （方法重写）
#继承的类中某一个函数不满足需要
#在本类中自定义一个跟继承的类中函数名相同的函数
#5.私有方法（函数）
#   不可被继承的，不能在类的外部调用的
#   只能在内部调用
#在函数名的左边加两个“下划线”
#class  W():
   # def  __zxc(self):
       # print('qwe')
#6.类的专有方法
#函数名左右两边都有两个下划线的
# 专有方法是python内部固定的
#只要是个类，具有所有的专有方法
#不需要调用直接使用
#属性：一个类中的所有函数都具有的特点
#   基础值
# class asd():
#     def  __inti__(self):   #初始化属性
#         self.a = 4
#         self.b = 5
# q = asd()
# class  asd():
#     def __init__(self,name,xueliang):
#         self.name = name
#         self.xueliang = xueliang
#     def daguai(self):
#         self.xueliang += 20
#         print('{},还剩下{}血量'.format(self.name,self.xueliang))
#     def jiaxue(self):
#         self.xueliang += 200
#         print('{},还剩下{}血量'.format(self.name,self.xueliang))
# q = asd('李白',100)
# q.daguai()
# q.jiaxue()




# class  H():
#     def  asd(self):
#         print('hello')
#     def  qwe(self):
#         print(123)
#         self.asd()
# class  W():
#     def  __zxc(self):
#         print('qwe')
#         self.__zxc()
#     def  dfg(self):
#         print(456)
#
#括号中是要写继承的类
# 新的类会继承旧的类中的所有函数
# class jkl(H):
#     def  op(self):
#      print('open')
# q = jkl()
# q.op()
# #将类名()赋值给一个变量
# H = H()
# #H  此时的H是    类的实际例子（对象）
# H.asd()
# H.qwe()

#面向对象的优点：可扩展，易维护，可重复使用
#面向过程的优点：性能好，运行程序快
#面向过程：通过代码和逻辑一步一步实现要达到的目的






#爬虫：模仿浏览器，根据自己制定的规则批量下载指定的资源
#爬虫的分类：聚焦爬虫和搜索爬虫
#聚焦爬虫：只针对某个网站进行爬取
#搜素爬虫：针对全网络进行爬取（搜索引擎）
#模仿浏览器：requests， 自带的模块urllib，urllib3   发送请求   scrapy
#过滤网页资源：re 正则表达式  Beautifulsoup ，xpath
#爬虫第一步：分析网址
#爬虫第二步：找到想要的资源并过滤
#爬虫第三步：保存


#对服务器进行请求  将得到的响应数据过滤出来并保存

#反爬虫：防止爬虫程序，批量下载资源
#常见的反爬机制：
#1.通过请求headrs判断
#2.ip地址被封     频繁转换公网ip地址  （西刺代理）
#3.验证码
#4.数据混淆
#5.行为分析
 #

#爬虫第一步：分析网址
# import requests
# import  re
# class  FreeBuf():
#     def  sent_请求(self):
#           url = 'https://www.freebuf.com/page/1'
#            head = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko\r\n'
#            }
# #发送请求
#           res = requests.get(url,headers=head)
# #读取结果    1.text  以文本的方式接收,结果是一个字符串
# #         较好2.content  以字节方式接收  结果是字节的形式
#           hh = res.content.decode('utf-8')
#           return hh
#     def guolv(self,x):
#         #二次过滤
#         title = []
#         patt = re.compile('<div class="news-info">(.*?)<dd>',re.S)
#         itesms = patt.findall(x)
#         #print(len(itesms))
#         for  i in  itesms:
#             bb =  re.compile('title="(.*?)"')
#             aa = bb.findall(i)
#             title.extend(aa[0])
#         return  title
# #爬虫第三部保存到文件中
#     def  save(self,y):
#         with open('C:\\Users\\hanwl\\Desktop\\c.txt','a',encoding='utf-8') as f:
#             for  i  in  y:
#                 f.write(i+'\n')
# fr = FreeBuf()
# hh = fr.sent_请求()
# #爬虫第二步：找到想要的资源并过滤
# yy = fr.guolv(hh)
# fr.save(yy)




# import requests
# import  re
# class  FreeBuf():
#     def  sent_请求(self,page):
#           url = 'https://www.freebuf.com/page/{}'.format(page)
# #发送请求
#           head = {
#           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko\r\n'
#           }
#           res = requests.get(url,headers=head)
# #读取结果    1.text  以文本的方式接收,结果是一个字符串
# #         较好2.content  以字节方式接收  结果是字节的形式
#           hh = res.content.decode('utf-8')
#           return hh
#     def guolv(self,x):
#         #二次过滤
#         title = []
#         patt = re.compile('<div class="news-info">(.*?)<dd>',re.S)
#         itesms = patt.findall(x)
#         #print(len(itesms))
#         for  i in  itesms:
#             bb =  re.compile('title="(.*?)"')
#             aa = bb.findall(i)
#             title.extend(aa[0])
#         return  title
# #爬虫第三部保存到文件中
#     def  save(self,y):
#         with open('C:\\Users\\hanwl\\Desktop\\c.txt','a',encoding='utf-8') as f:
#             for  i  in  y:
#                 f.write(i)
# fr = FreeBuf()
# for  j  in range(2,5):
#     hh = fr.sent_请求(j)
#     #爬虫第二步：找到想要的资源并过滤
#     yy = fr.guolv(hh)
#     fr.save(yy)



#保存图片
# import  requests
# import re
# url = 'https://www.qiushibaike.com/imgrank/'
# # head = {
# #           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko\r\n'
# #           }
# res = requests.get(url)
# html = res.content.decode('utf-8')
# #过滤
# patt =re.compile(r'<img src="//pic.qiushibaike.com/system/pictures/(.*?).jpg"')
# itesms = patt.findall(html)
# print(len(itesms))
# a = 0
# for  i in  itesms:
#      j = 'https://pic.qiushibaike.com/system/pictures/'+i+'.jpg'
#      print(j)
# #保存图片   先对图片的链接进行请求 以字节的方式读取，一字节的方式保存
#      msg = requests.get(j)
#      hh = msg.content
#      with open('{}.jpg'.format(a),'wb') as  f:
#          f.write(hh)
#          a = a+1


#zip()将多个列表一一对应
# a = [12,32,3,2]
# b = ['a','b','c']
#加上数据类型
# aa = list(zip(a,b))
# print(aa)




#进行网页分析
# import requests
# import  re
# url = 'https://movie.douban.com/top250'
# res = requests.get(url)
# html = res.content.decode('utf-8')
# #过滤
# a = []
# patt = re.compile(' <img width="100" alt="(.*?)"')
# itesms = patt.findall(html)
# print(itesms)
# a.extend(itesms)
# p = re.compile('https://img(.).doubanio.com/view/photo/s_ratio_poster/public/(.*?)class=""')
# s = p.findall(html)
# print(s)
# b = 0
# for  i in s:
#      bb ='https://img{}.doubanio.com/view/photo/s_ratio_poster/public/{}'.format(i[0],i[1])
#      #aa = bb.findall(i)
#      print(bb)
#      msg = requests.post(bb)
#      hh = msg.content
#      with open('{}.jpg'.format(a[b]),'wb') as  f:
#          f.write(hh)
#      b = b+1



# import re
# import requests
# url = 'https://www.qiushibaike.com/pic/'
# res = requests.get(url)
# hh = res.content.decode('utf-8')
# #过滤：
# patt = re.compile('<img src="//pic.qiushibaike.com/system/(.*?).jpg"')
# itesms = patt.findall(hh)
# print(len(itesms))
# print(itesms)
# #保存：
# a = 0
# for i in itesms:
#      j = 'https://pic.qiushibaike.com/system/'+i+'.jpg'
#      print(j)
#      msg = requests.get(j)
#      b = msg.content
#      #进行二进制转化保存文件
#      with  open ('{}.jpg'.format(a),'wb')  as  f:
#       f.write(b)
      #a = a+1



#网页
# 静态网页：所有的资源都在html文件上
#动态网页：资源不在html文件上
#  ajax（XHR报文）     Javascript
#       json：是一种轻量级的数据传输格式
#将字符串转换为字典：
#变量名  =  json.loads(变量名)
#将字典转换为字符串
#变量名  =  json.dumps(变量名)
# import   requests


# import  json
# url = ''
# res =requests.get(url)
# hhh =res.content.decode('utf-8')
# qqq =json.loads(hhh)
# print(qqq[''])


































































































































































































































































































































