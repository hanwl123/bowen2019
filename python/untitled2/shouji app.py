
from appium import  webdriver
from time import sleep
#面向对象
from appium import webdriver
from time import sleep


# 面向对象
class Tim(object):

    # 初始化属性
    def __init__(self):
        # 建立与appium服务器需要的参数，以字典的形式
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
        sleep(5)

    def dian_zan(self):
        # 第一步，点击办公
        self.dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')[
            -1].click()
        # 第二步，点击好友动态
        t = self.dr.find_element_by_id('com.tencent.tim:id/lebasv').find_elements_by_class_name(
            'android.widget.RelativeLayout')
        t[-1].click()
        sleep(0.5)
        # 第三步 点赞
        x = self.dr.find_elements_by_class_name('android.widget.ImageView')
        print(x)
        x[1].click()
        sleep(2)
        x[2].click()


# 调用类
if __name__ == '__main__':
    yasuo = Tim()
    yasuo.dian_zan()



# des = {
#   "platformName": "Android",
#   "platformVersion": "5.1.1",
#   "deviceName": "emulator-5554",
#   "appPackage": "com.ss.android.ugc.aweme",
#   "appActivity": ".main.MainActivity",
#   "noReset": "true"
# }
# #'http://127.0.0.1:4723/wd/hub'  固定的  写死localhost=127.0.0.1
# #测试脚本与appium服务器建立一个session连接
# dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=des)
# items=dr.find_element_by_id('com.ss.android.ugc.aweme:id/ca9').find_elements_by_class_name('android.widget.FrameLayout')
# print(items)
# # 第三步：点赞
# dr.quit()
#
#
#
#
#
# dr.find_element_by_class_name('')[2].click()






















