# !/usr/bin/puthon
# # _*_coding:utf_8  _*_

#  web自动化

#selenium：   web 自动化测试工具集
#selenium1.0的组成

#1.   selenium  IDE  是火狐浏览器的一个插件
#  作用：  录制和回放
#2.   selenium Grid  是自动化测试的一个辅助工具
#  作用：  可以实现在不同的环境中同时实现执行测试
#3.   selenium  Rc  selenium1.0 是自动化测试的核心
#  作用：   控制浏览器的行为

#   selenium2.0的组成
#   selenium1.0在内的所有的工具（selenium  ide/  grid  /  rc）  加上   webdriver
#   webdriver 是selenium2.0的核心
#   作用： ，控制浏览器的行为
#   Rc：通过将测试代码转换成JavaScript能够识别的动作，从而间接的控制浏览器
#   webdriver：通过将浏览器的所有的原生接口集成到webdriver驱动中，然后通过驱动直接控制浏览器

#   wbedriver.exe

#为什么选择selenium特点 ？
#1.开源免费
#多浏览器支持
#多平台支持
#多语言支持
#对web页面有良好的支持
#简单（api简单）、灵活（用开发语言驱动）
#支持分布式测试用例的执行
#
#
# from  selenium  import  webdriver
# from  time  import  sleep
# dr = webdriver.Chrome()
# dr.get('https://qzone.qq.com/')
# sleep(2)
# dr.switch_to.frame('login_frame')
# sleep(2)
# dr.find_element_by_id('switcher_plogin').click()
# sleep(2)
# dr.find_element_by_id('u').send_keys('1417926350')
# sleep(3)
# dr.find_element_by_id('p').send_keys('hwl1997521.')
# sleep(2)
# dr.find_element_by_id('login_button').click()
# sleep(2)




#selenium  的安装和环境搭建
#
#定位一组对象
from  selenium  import  webdriver
from time import  sleep
#导入模块   智能等待
import selenium.webdriver.support.ui  as  ui
from selenium.webdriver.common.action_chains import  ActionChains  #动作链
# dr = webdriver.Chrome()
# dr.get('https://www.baidu.com')
# sleep(3)
# ww  = dr.find_elements_by_class_name('option')
# # print(len(ww))
# for   i in  ww:
#   b =   i.get_attribute('text')   #获取某个属性的值
#   print(b)



#层级定位:   先从一个大的区域，在从大的区域中定位
#先定位 父元素，再定位子元素
#定位的父元素必须是唯一的，子元素可以是定位一组，也可以定位一个
# dr = webdriver.Chrome()
# dr.get('https://www.ctrip.com')
# sleep(3)
# dr.find_element_by_class_name('current').click()
# sleep(3)
# ww  = dr.find_element_by_id('J_roomCountList').find_elements_by_class_name('option')
# print(len(ww))
# for  i in  ww:
#      i.click()
#      sleep(2)




#鼠标 模拟点击
# dr = webdriver.Chrome()
# dr.get('https://www.jd.com')
# sleep(3)
# ww = dr.find_element_by_xpath('//*[@id="J_cate"]/ul').find_elements_by_class_name('cate_menu_lk')
# for  i in  ww:
#     ActionChains(dr).move_to_element(i).perform()
#     sleep(3)
#



#鼠标拖拽
# dr = webdriver.Chrome()
# dr.get('https://qzone.qq.com/')
# sleep(2)
#iframe 内嵌框架（窗口）
#切换到某个框架上去
# 三种方式  1.id  2. name  3.xpath路径
#从框架中出来  回退到最初的页面上
#dr.switch_to.default.content()
#回退到上一个框架上
#dr.switch_to.parent_frame()
# dr.find_element_by_id('u').send_keys('65368260')
# sleep(2)
# dr.find_element_by_id('p').send_keys('hwl19971.')
# sleep(2)
# dr.find_element_by_id('login_button').click()
# sleep(1)
#drag_and_drop   两个参数（起始位置，结束位置）
#drag_and_drop_by_offset(起始位置，x轴坐标，y轴坐标)

#切换框架
# dr.switch_to.frame('tcaptcha_iframe')  20
# sleep(3)
#

#进行拖拽
# wd = dr.find_element_by_xpath('//*[@id="tcaptcha_drag_button"]')
# sleep(3)
# ActionChains(dr).drag_and_drop_by_offset(wd,188,0).perform()
# sleep(2)



#任何浏览器管理窗口的管理
#  将每一个窗口用一个特定的字符来标识
#  只需要获取每一个窗口的标识号，通过切换标识号，来达到切换窗口的目的

# dr = webdriver.Chrome()
# dr.get('https://www.douban.com/')
# sleep(2)

# # # 获取当前的窗口标识
# print(dr.current_window_handle)
# sleep(2)
# dr.find_element_by_xpath('//*[@id="anony-nav"]/div[1]/ul/li[1]/a').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="anony-nav"]/div[1]/ul/li[2]/a').click()
# sleep(2)
# print(dr.window_handles)
# aa = dr.window_handles
# #切换窗口
# dr.switch_to.window(aa[2])
# print(dr.current_window_handle)
# print(dr.title
#自动翻页
# for i in range(0,10000,500):
#     #执行JavaScript语句的
#     js="var  q=document.documentElement.scrollTop={}".format(i)
#     dr.execute_script(js)
#     sleep(3)

# dr = webdriver.Chrome()
# dr.get('C:/Users/hanwl/Desktop/abc.html')
# sleep(2)
# #  处理弹出框
# dr.find_element_by_xpath('/html/body/input').click()
# sleep(2)
# #切换到弹出框上去
# ww = dr.switch_to_alert()
# print(ww.text)
# #获取弹出框上面的文本
# #点击确定
# ww.accept()
# #点击取消
# ww.dismiss()
#向弹出框输入数据
#ww.send_keys('asdfghjkl;')


# dr = webdriver.Chrome()
# dr.get('https://www.baidu.com')
# #sleep(3)#强制等待
# #先创建一个智能等待的控制器   10 ：最大等待时间
# unti = ui.WebDriverWait(dr,10)
# #如果定位元素出现了就不必等待了
# unti.until(lambda  dr: dr.find_element_by_link_text('hao123').is_displayed())
#
# #检查hao123是否出现，
# #如果出现了执行下面的代码
# # 如果没出现就一值等待  最大等待 10秒
# dr.find_element_by_link_text('新闻').click()

















