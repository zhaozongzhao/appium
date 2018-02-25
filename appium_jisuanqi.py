from appium import  webdriver
#android environment
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['paltformVersion'] = '4.4.2'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.ibox.calculators'
desired_caps['appActivity']= '.CalculatorActivity'
#连接qppium
driver  = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)

driver.find_element_by_id('com.ibox.calculators:id/digit8').click()
driver.find_element_by_id('com.ibox.calculators:id/plus').click()
driver.find_element_by_id('com.ibox.calculators:id/digit5').click()
driver.find_element_by_id('com.ibox.calculators:id/equal').click()


