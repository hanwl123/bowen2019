# !/usr/bin/puthon
# # _*_coding:utf_8  _*_
#导入模块
from HTMLTestReportCN  import HTMLTestRunner
import  unittest
from  appium  import  webdriver
from time  import  sleep
import warnings
from diesheng.config import config_1
from diesheng.config import config_2
#导入封装好的日志函数
from diesheng.config.config_3 import get_logger
#创建变量名接收日志的句柄    根笔
log = get_logger('test_1')
#单元测试必须继承unittest.TestCase
class  DS(unittest.TestCase):
    #每个用例执行之前运行一次，  作用：用于清理测试环境残留数据，初始化测试环境
    def setUp(self):#setup  相当于  _init_  类的调用会自动运行
        warnings.simplefilter('ignore',ResourceWarning)
        self.des = {
            "device": "android",
            "platformName": "Android",
            "platformVersion": "9",
            "deviceName": "46HDU19314003325",
            "appPackage": "com.tencent.tim",
            "appActivity": "com.tencent.mobileqq.activity.SplashActivity",
            "noReset": "true",
        }
        # http://127.0.0.1:4723/wd/hub 固定的，写死localhost==127.0.0.1
        # 测试脚本与appium服务器建立一个session连接
        self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=self.des)
        sleep(5.0)
        log.info("手机与appium服务器建立连接完成…………")
    def test_1 (self):
        #使用账号密码登录碟声
        #点击密码，进入手机号、密码登录界面
        log.info("点击密码按键，进入账号密码登录界面")
        self.dr.find_elements_by_id('com.qk.butterfly:id/et_login_pwd').click()
        # 使用脚本与测试相结合
        for i in config_1.read_data():
            #进入登录密码页面之后
            self.dr.find_elements_by_id('com.qk.butterfly:id/et_login_phone').send_keys(i[0])
            log.info(f'输入的手机号是:{i[0]}')
            self.dr.find_elements_by_id('com.qk.butterfly:id/et_login_pwd').send_keys(i[1])
            log.info(f'输入的密码是:{i[1]}')
            self.dr.find_elements_by_id('com.qk.butterfly:id/tv_to_login')
            log.info(f'点击登录按钮')
            #断言登录失败
            sleep(5.0)
            """
            if  else  处理登录成功与失败，也可以用  try   except  语句断言
            """
            try:
                #登录失败，还在登录界面
                log.info('登录成功测处理')
                b = self.dr.find_elements_by_id('').text
                print("登录失败")
                self.assertEqual(b,"登录",msg="登录失败")
            except:
                # 断言
                sleep(5.0)
                # 进入登录之后的页面
                a = self.dr.find_elements_by_id('')[-1].text
                self.assertEqual(a, '我的', msg="断言已经登陆成功")
                print("登录成功")


        #使用账号密码登录碟声
        #点击密码，进入手机号，密码登录页面
        #self.dr.find_elements_by_id('com.qk.butterfly:id/et_login_pwd').click()
        #进入登录手机号密码登录之后的页面之后
        # self.dr.find_elements_by_id('com.qk.butterfly:id/et_login_phone').send_keys('')
        # self.dr.find_elements_by_id('com.qk.butterfly:id/et_login_pwd')
        # self.dr.find_elements_by_id('com.qk.butterfly:id/tv_to_login')


    #断言

    #进入登录之后的页面
        # a = self.dr.find_elements_by_id('')[-1].text
        # self.assertEqual(a,'我的',msg="断言已经登陆成功")

    #每一个测试用例执行完毕后，  运行teardown一次， 作用：测试用例运行完，清理测试环境
    def tearDown(self):
        log.info('手机与appium断开连接…………')
        self.dr.quit()

if __name__ == '__main__':
    #unittest.main()
    config_2.report(test_name=DS('test_1'),report_path=('C:\Users\hanwl\PycharmProjects\untitled2\diesheng\report\a.html'))

