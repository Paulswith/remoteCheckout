# -*- coding:utf-8 -*-
__author = 'Dobby'


import sys
sys.path.append("..")
from wxpy import *
from login.login import AutoCheckout
import settings


code_photo_path = settings.CODE_PHOTO_PATH

bot = Bot(cache_path=True,console_qr=True)
my_friend_Dobby = bot.friends().search('Dobby')[0]
fireFox = AutoCheckout(settings.USER_NAME, settings.PASS_WORD)

def page(number,path):
    if number:
        my_friend_Dobby.send('check out Done')
    else:
        my_friend_Dobby.send('check out fail')
    my_friend_Dobby.send_image(path)
    bot.start()


@bot.register()
def forward_boss_message(msg):

    '''
    dealWithMessage been receive
    :param msg: 
    '''
    fireFox.logEven(msg.text)
    lower_recive = msg.text.lower()

    if 'checkin' in lower_recive:
        number = fireFox.startCheckIn()
        page(number,code_photo_path)

    elif 'checkout' in lower_recive:
        number = fireFox.startCheckOut()
        page(number, code_photo_path)

    elif 'code' in lower_recive:
        '''
        Example:  
        cicodexxxx 
        ci -> checkIn
        co -> checkout
        xxxx ->verification code
        '''
        if lower_recive[:2] == 'ci':
            number = fireFox.codePerform(lower_recive[-4:])
            page(number, code_photo_path)

        elif lower_recive[:2] == 'co':
            number = fireFox.codePerform(lower_recive[-4:])
            page(number, code_photo_path)
        else:
            my_friend_Dobby.send('valid command')
    else:
        my_friend_Dobby.send(settings.HELP_COMMAND)

embed()