from appium import  webdriver
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



