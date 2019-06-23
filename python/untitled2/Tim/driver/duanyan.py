# !/usr/bin/python
# _*_coding:utf_8  _*_
#from HTMLTestReportCN import HTMLTestRunner
from  Tim.config.config_5 import report
from  time  import sleep
import  unittest
from  selenium  import  webdriver
class Duan(unittest.TestCase):
    def Duan_yan(self):
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
        try:
            a = dr.find_element_by_link_text('最新').text
            self.assertEqual(a,'最新',msg="验证失败")
        except:
            b = dr.find_element_by_xpath('/html/body/div[3]/div/div[3]/div[1]/div[2]')
            self.assertEqual(b,'',msg="验证成功")
if __name__ == '__main__':
   report(Duan.Duan_yan,report_path=(r'C:\Users\hanwl\PycharmProjects\untitled2\Tim\report\b.html'))
























