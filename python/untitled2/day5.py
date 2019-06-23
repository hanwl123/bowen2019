# !/usr/bin/puthon
# # _*_coding:utf_8  _*_
# web  自动化     selenium
# Python  代码，控制浏览器打开网页
# 驱动，不同浏览器对应不同的驱动
#需要先下载模块selenium  然后在下载  对应网站的 驱动版本
#进行粘贴复制 到  C:\Users\hanwl\AppData\Local\Programs\Python\Python37目录下



# from  selenium  import  webdriver
# from  time  import  sleep
# #打开浏览器网页
# dr = webdriver.Firefox()
# #请求要打开的网页
# dr.get('https://www.baidu.com/')
# sleep(2)
#打印打开的网页标题
# if dr.title == '百度一下，你就知道':
#     print('yes')
#dr.title
#打印当前网页的网址
#print(dr.current_url)
#设置浏览的窗口大小
#dr.set_window_size(400,400)
#设置浏览器的位置
#dr.set_window_position(400,400)
#最大化浏览器
#dr.maximize_window()
#最小化浏览器窗口
#dr.minimize_window()
#dr.get('https://www.jd.com')
#sleep(2)
#回退 到原先的网址
#dr.back()
#前进 到下面一个网址
# sleep(2)
#dr.forward()

#！！！定位
#1.ID属性定位       动作：    send_keys  (输入内容)    click   点击
#dr.find_element_by_id('kw').send_keys('python')
#sleep(2)
#dr.find_element_by_id('su').click()
#2.通过name属性进行定位
# dr.find_element_by_name('wd').send_keys('开封大学')
# sleep(2)
# dr.find_element_by_id('su').click()
#3.通过class属性定位
#不论哪一种定位方法，
#一定要保证定位的唯一性
# dr.find_element_by_class_name('s_ipt').send_keys('python')
# sleep(2)
# dr.find_element_by_class_name('mnav').click()
#4.通过 link_text  文本进行定位
#5.partial_link_text('hao')进行模糊查找
#dr.find_elements_by_partial_link_text('hao').click()
#6.通过tag_name   根据标签的名称定位
#print(dr.find_elements_by_tag_name(').text)
#7.通过  xpath  路径定位
#xpath 路径标记语言
#/html/body/div[1]/div[1]/div/div[3]/a[1]  绝对路径
#dr.find_elements_by_xpath('/html/body/div[1]/div[1]/div/div[3]/a[1]').click()
#8.通过  css_selector'hao
#dr.find_elements_by_css_selector('a.mnav:nth-child(1)').click()



#自动登录qq空间
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
# sleep(2)
# dr.find_element_by_id('p').send_keys('hwl1997521.')
# sleep(2)
# dr.find_element_by_id('login_button').click()
# sleep(1)
# # dr.find_element_by_xpath('//*[@id="$1_substitutor_content"]').send_keys('  你不能一直做一些烂事，然后自己后悔，好像后悔有用一样，你需要变好。 ')
# # sleep(1)
# # dr.find_element_by_xpath('//*[@id="QM_Mood_Poster_Inner"]/div/div[4]/div[4]/a[2]/span').click()
# dr.find_element_by_xpath('//*[@id="menuContainer"]/div/ul/li[5]/a').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="menuContainer"]/div/ul/li[6]/a').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="edit_base_info"]').click()
# sleep(2)
# dr.find_element_by_xpath('//*[@id="blood_select"]').send_keys('学生')




#自动登录QQ邮箱
# from  selenium  import  webdriver
# from  time  import  sleep
# dr = webdriver.Firefox()
# dr.get('https://mail.qq.com/')
# sleep(2)
# dr.switch_to.frame('login_frame')
# sleep(2)
# dr.find_element_by_id('switcher_plogin').click()
# sleep(2)
# dr.find_element_by_id('u').send_keys('1417926350')
# sleep(2)
# dr.find_element_by_id('p').send_keys('hwl1997521.')
# sleep(2)
# dr.find_element_by_id('login_button').click()

































