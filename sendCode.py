#!/usr/bin/python
# -*- coding:utf-8 -*-
__author = 'Dobby'


import sys
sys.path.append("..")
# from wxpy import *
from login.login import AutoCheckout
import settings
import time

'''
struct perform timer
'''
m_t_after = settings.MORNINg_time[1]
m_t_before = settings.MORNINg_time[0]
e_t_after = settings.EVENINg_time[1]
e_t_before = settings.EVENINg_time[0]
'''
struct lambda func
'''
get_current_time = lambda: str(time.strftime('%H%M', time.localtime(time.time())))
get_full_current_time = lambda: str(time.strftime('20%y年%m月%d日%H时%M分', time.localtime(time.time())))
is_weekend = lambda : True if (str(time.strftime("%w", time.localtime())) == '7' or str(time.strftime("%w", time.localtime())) =='6') else False


if __name__ == '__main__':
    #initial brower
    fireFox = AutoCheckout(settings.USER_NAME, settings.PASS_WORD)
    while 1:
        #filter weekend
        fireFox.logEven('is today weekend? // {}'.format('yes' if is_weekend() else 'not'))
        if not is_weekend():
            c_time = get_current_time()
            init_string = 'currentTime:{full_time},structTime:{struct_time}'.format(full_time=get_full_current_time(),struct_time=c_time)
            fireFox.logEven(init_string)

            if  c_time < e_t_after and c_time > e_t_before:
                for i in xrange(5):
                    is_succeed = fireFox.startCheckOut()
                    log_even = '-> the {count} : resultIs({result})'.format(count=i,result='succeed' if is_succeed else 'faild')
                    fireFox.logEven(log_even)
                    if is_succeed == True:
                        break

            if c_time < m_t_before and c_time > m_t_after:
                for i in xrange(5):
                    is_succeed = fireFox.startCheckIn()
                    log_morning ='-> the {count} : resultIs({result})'.format(count=i, result='succeed' if is_succeed else 'faild')
                    fireFox.logEven(log_morning)
                    if is_succeed == True:
                        break
        time.sleep(29*60)


#discard wxpy
# code_photo_path = settings.CODE_PHOTO_PATH
#
# bot = Bot(cache_path=True,console_qr=True)
# my_friend_Dobby = bot.friends().search(settings.CONTACT_ONE)[0]

#
# def page(number,path):
#     if number:
#         my_friend_Dobby.send('check out Done')
#     else:
#         my_friend_Dobby.send('check out fail')
#     my_friend_Dobby.send_image(path)
#     bot.start()
#
#
# @bot.register()
# def forward_boss_message(msg):
#
#     '''
#     dealWithMessage been receive
#     :param msg:
#     '''
#     fireFox.logEven(msg.text)
#     lower_recive = msg.text.lower()
#
#     my_friend_Dobby.send('received: {} ({})'.format(msg.text, msg.type))
#
#     if 'checkin' in lower_recive:
#         number = fireFox.startCheckIn()
#         page(number,code_photo_path)
#
#     elif 'checkout' in lower_recive:
#         number = fireFox.startCheckOut()
#         page(number, code_photo_path)
#
#     elif 'code' in lower_recive:
#         '''
#         Example:
#         cicodexxxx
#         xxxx ->verification code
#         '''
#         # if lower_recive[:2] == 'ci':
#         #     number = fireFox.codePerform(lower_recive[-4:])
#         #     page(number, code_photo_path)
#         #
#         # elif lower_recive[:2] == 'co':
#         number = fireFox.codePerform(lower_recive[-4:])
#         page(number, code_photo_path)
#         # else:
#         #     my_friend_Dobby.send('valid command')
#
#     elif 'help' in lower_recive:
#         my_friend_Dobby.send(settings.HELP_COMMAND)
#
# embed()


