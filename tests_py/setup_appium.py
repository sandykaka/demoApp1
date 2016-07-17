import os
import config
from appium import webdriver
import subprocess32

def setup_appium(App, platform):
    if platform == 'iOS':
        desired_caps = dict()
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '9.2.1'
        desired_caps['deviceName'] = 'iPhone Simulator'
        desired_caps['udid'] = '09d905a109245efebd23ab741c0900e83769b3ae'
        desired_caps['app'] = os.path.realpath(os.path.realpath(__file__) + "/../../") + '/' + App
        config.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        return config.driver


def start_appium():
    config.appium_server = subprocess32.Popen(['appium'])


def stop_appium():
    config.appium_server.terminate()