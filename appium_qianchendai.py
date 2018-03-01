from appium import  webdriver
import time
from appium.webdriver.common.touch_action import TouchAction
#android environment

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['paltformVersion'] = '4.4.2'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.xxzb.fenwoo'
desired_caps['appActivity']= '.activity.addition.SplashActivity'
#连接qppium
driver  = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

def getSize():
    x = driver.get_window_size()['width'] #获取界面的宽
    y = driver.get_window_size()['height'] #获取界面的高
    return (x,y)

def swipeleft():
    '''从向左滑动'''
    x = getSize()[0]
    y = getSize()[1]
    driver.swipe(x*0.9,y*0.2,x*0.1,y*0.2,500)

#向左滑动三次
for i in range(3):
    swipeleft()
time.sleep(3)
#点击立即体验按钮
driver.find_element_by_id('com.xxzb.fenwoo:id/btn_start').click()
driver.find_element_by_id('com.xxzb.fenwoo:id/btn_login').click()
driver.find_element_by_id('com.xxzb.fenwoo:id/et_phone').send_keys('13760246701')
driver.find_element_by_id('com.xxzb.fenwoo:id/btn_next_step').click()
driver.find_element_by_id('com.xxzb.fenwoo:id/et_pwd').send_keys('python_test')
driver.find_element_by_id('com.xxzb.fenwoo:id/btn_next_step').click()



driver.find_element_by_id('com.xxzb.fenwoo:id/btn_confirm').click()
driver.find_element_by_id('com.xxzb.fenwoo:id/btn_gesturepwd_guide').click()
driver.find_element_by_id('com.xxzb.fenwoo:id/right_btn').click()
picture = driver.find_element_by_id('com.xxzb.fenwoo:id/gesturepwd_create_lockview')
scope =picture.size
ss=picture.location
print(scope)
x4 = ss['x']+scope ['width']/6
y4 = ss['y']+scope ['height']/2
x_step = scope ['width']/6
y_step = scope ['height']/6
print(x_step,y_step)
action = TouchAction(driver)
action.press(x=x4, y=y4).wait(100).move_to(x=x_step*4, y=0).wait(200).move_to(x=0,y=-y_step*2).release().wait(100).perform()
print(x_step*5)
#driver.find_element_by_id('com.xxzb.fenwoo:id/right_btn').click()
