#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import telebot
    import os
    import sys
    import random
except ImportError :
    print "[-] You need to install Modules \n\nsudo pip install pytelegrambotapi"
    exit()
reload(sys)
sys.setdefaultencoding("utf-8")
TOKEN = '<<<< Your Token >>>>>'
bot = telebot.TeleBot(TOKEN)

def banner():
    print """

 FORCE TEAM

"""

def clearing():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])

banner(),clearing()

f = "\n \033[01;30m Bot Firstname: {} \033[0m".format(bot.get_me().first_name)
u = "\n \033[01;34m Bot Username: {} \033[0m".format(bot.get_me().username)
i = "\n \033[01;32m Bot ID: {} \033[0m".format(bot.get_me().id)
c = "\n \033[01;31m Bot Is Online Now! \033[0m"
print(f + u + i + c)

@bot.message_handler(content_types=['text', 'audio', 'document', 'photo', 'sticker', 'video', 'voice', 'location'])
def us(m):
    file = open("fuckbot.db","r")
    file = file.read()
    new = file.split(",")
    bot.send_message(m.chat.id, random.choice(new))


bot.polling(True)
-- #Dev_Master <===
