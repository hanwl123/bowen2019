# !/usr/bin/python
# _*_coding:utf_8  _*_
from  selenium  import  webdriver
from  time  import  sleep
#from selenium.webdriver.common.action_chains import  ActionChains
def  test1():
    dr = webdriver.Firefox()
    dr.get('https://shurufa.baidu.com/')
    sleep(2)
    dr.switch_to.frame('login_frame')
    sleep(2)
    dr.find_element_by_link_text('皮肤').click()
    sleep(3)
    # for i in read():
    dr.find_element_by_id('keyword').send_keys('王者')
    sleep(3)
    dr.find_element_by_class_name('submit').click()

    #sleep(3)
    #     try:
    #         a = self.dr.find_element_by_link_text('最新').text
    #         self.assertEqual(a,'最新',msg="登录失败")
    #     except:
    #         b = self.dr.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[2]')
    #         print(b)
    #
    #         print("pass")
test1()





































