#-*- coding:utf-8 -*-

from appium import webdriver
from time import sleep


def get_desired_caps():

    desired_caps = {
        'platformName' : 'Android',
        'platformVersion' : '5.1',
        'deviceName' : '81CEBMJ236WJ',
        'udid' : '81CEBMJ236WJ',
        'appPackage' : 'com.tencent.mm', # app package name
        'appActivity' : '.ui.LauncherUI', # app 默认的 Activity

        # 开启unicode键盘
        'unicodeKeyboard' : 'True',
        'resetKeyboard' : 'True',

        'newCommandTimeout' : 1800,

        # 驱动H5自动化关键之一
        'chromeOptions' : {'androidProcess': 'com.tencent.mm:tools'}
    }

    # desired_caps['platformName'] = 'Android'
    # desired_caps['platformVersion'] = '5.1'
    # desired_caps['deviceName'] = 'MEIZU_M571C'
    # desired_caps['appPackage'] = 'com.tencent.mm'
    # desired_caps['appActivity'] = '.ui.LauncherUI'
    # desired_caps["unicodeKeyboard"] = "True" # 开启unicode键盘
    # desired_caps["resetKeyboard"] = "True"
    # desired_caps["newCommandTimeout"] = 1800

    # 驱动H5自动化关键之一
    # desired_caps['chromeOptions'] = {'androidProcess': 'com.tencent.mm:tools'}

    return desired_caps


def get_app_driver():
    app_driver = webdriver.Remote('http://192.168.1.31:4723/wd/hub',get_desired_caps()) #启动Remote RPC
    app_driver.implicitly_wait(10)
    return app_driver

def close_app_driver():
    sleep(3)
    get_app_driver().quit()