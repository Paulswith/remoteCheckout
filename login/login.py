#!/usr/bin/python
# -*- coding:utf-8 -*-
__author = 'Dobby'

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time,os
import settings



class AutoCheckout(object):

    def __init__(self,name,passwd):
        self.username = name
        self.password = passwd
        self._path = os.path.join(os.getcwd(),'geckodriver')
        self.driver = webdriver.Firefox(executable_path=self._path)
        self.element= {'用户名':'#username',
                       '密码框':'#password_input',
                       '记住密码':'#rememberButton',
                        '登录按钮':'#login_button',
                        '签出按钮':'#checkout_btn',
                        '签入按钮':'#checkin_btn',
                        '签到确定':'//*[@id="tdialog-buttonwrap"]/a[1]',
                       '签出成功知会':'//*[@id="ui-dialog-title-tdialog"]',
                       '完成确定':'//*[@id="tdialog-buttonwrap"]/a/span',
                       '验证码':'#code_input'
                       }

    def logEven(self,str):
        '''
        打印日志
        '''
        print '///= = || %s:%s || = =/\/\/\/'%(time.ctime(),str)

    def tryfind(self,atr,way=By.CSS_SELECTOR,timeOut=5):
        '''
        :param atr:需要查找的元素 
        :param way: 默认 CSS
        :param timeOut: 默认30
        :return: element if 1 else return 0 
        '''

        try:
            btnExit = WebDriverWait(self.driver, timeOut).until(EC.element_to_be_clickable((way, atr)))
            return btnExit
        except:
            return False

    def realTime(self):
        '''
        get realTime
        :return: intTime
        '''
        return int(time.strftime('%H%M', time.localtime(time.time())))

    def loginPage(self):
        '''
        Base do login
        '''

        self.driver.get(settings.DO_WEBSITE)
        self.tryfind(self.element['用户名']).send_keys(self.username)
        time.sleep(5)
        self.tryfind(self.element['密码框']).send_keys(self.password)
        time.sleep(5)
        self.tryfind(self.element['登录按钮']).click()

    def clearCookies(self):
        '''
        Clear cookies
        '''
        self.driver.delete_all_cookies()
        if not self.driver.get_cookies():
            print ' #               *清除缓存成功*                # '
        else:
            print ' #             ~*`清除缓存失败`*~              # '
            self.driver.delete_all_cookies()

    def get_screenshot_as_file(self, path=settings.CODE_PHOTO_PATH):
        '''截屏操作'''
        try:
            self.driver.get_screenshot_as_file(path)
        except:
            pass



    def startCheckIn(self):
        '''
        签入操作
        :param" 失败与成功都截图下 <>
        :return: 1 success  | 0 fail
        '''
        try:
            self.loginPage()
            self.tryfind(self.element['签入按钮']).click()
            if self.tryfind(self.element['验证码']):
                self.get_screenshot_as_file()     #截图到本地 , 不清空,  让存在cookie
                return 0                #存在验证码返回2
            self.tryfind(self.element['签到确定'], way=By.XPATH).click()  # 点击确定
            if self.tryfind(self.element['签出成功知会'], way=By.XPATH,timeOut=30).text == u'签入成功知会':
                print ' # 本次%s成功 at %s    # ' % ('签入', time.ctime())
                self.clearCookies()
        except:
            self.get_screenshot_as_file()
            self.clearCookies()
            self.logEven('签入失败')
            return 0
        else:
            self.get_screenshot_as_file()
            return 1

    def startCheckOut(self):
        '''
        签出操作
        :param" 失败与成功都截图下 <>
        !!! 存在验证码的时候不会清空缓存
        :return: 1 success  | 0 fail
        '''
        try:
            self.loginPage()
            self.tryfind(self.element['签出按钮']).click()
            if self.tryfind(self.element['验证码']):
                self.get_screenshot_as_file()
                return 0
            self.tryfind(self.element['签到确定'], way=By.XPATH).click()
            if self.tryfind(self.element['签出成功知会'], way=By.XPATH,timeOut=30).text == u'签出成功知会':
                print ' # 本次%s成功 at %s    # ' % ('签出', time.ctime())
                self.clearCookies()
        except:
            self.get_screenshot_as_file()
            self.clearCookies()
            self.logEven('签出失败')
            return 0
        else:
            self.get_screenshot_as_file()
            return 1

    def codePerform(self,code):
        """
        延续存在验证码的后续操作, 失败与成功都截图下 <>
        :param code:  验证码<此处不处理消息的验证码>
        :return:  1 success  | 0 fail
        """
        try:
            self.tryfind(self.element['验证码']).click()
            self.tryfind(self.element['验证码']).send_keys(code)
            self.tryfind(self.element['签到确定'], way=By.XPATH).click()  # 点击确定
            bool_check_text = self.tryfind(self.element['签出成功知会'], way=By.XPATH).text
            if bool_check_text == u'签入成功知会' or bool_check_text == u'签出成功知会':
                print ' # 本次%s成功 at %s    # ' % ('签入', time.ctime())
                self.clearCookies()
        except:
            self.get_screenshot_as_file()
            self.clearCookies()
            self.logEven('验证码签到失败')
            return 0
        else:
            self.get_screenshot_as_file()
            return 1