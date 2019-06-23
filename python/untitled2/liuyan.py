# !/usr/bin/python
# _*_coding:utf_8  _*_
from selenium import  webdriver
from time import sleep
dr = webdriver.Chrome()
dr.get('https://qzone.qq.com/')
sleep(2)
dr.switch_to.frame('login_frame')
sleep(2)
dr.find_element_by_id('switcher_plogin').click()
sleep(2)
dr.find_element_by_id('u').send_keys('1417926350')
sleep(3)
dr.find_element_by_id('p').send_keys('hwl1997521.')
sleep(2)
dr.find_element_by_id('login_button').click()
sleep(2)


dr.get('https://user.qzone.qq.com/854917004')
sleep(5)
dr.find_element_by_xpath('//*[@id="menuContainer"]/div/ul/li[4]/a').click()
sleep(3)
dr.find_element_by_xpath('/html/body').send_keys('......')
sleep(3)
dr.find_element_by_xpath('//*[@id="btnPostMsg"]').click()















































