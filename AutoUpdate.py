import os
import time
import requests
s=requests.session()

def start(txt):
    os.system('start cmd /k '+txt)

while True:
    flag=False
    #ping.py
    new=s.get('https://ghproxy.com/https://raw.githubusercontent.com/Lotuses-robot/QQ_bot_for_Dynamic_map/main/bot_plugins/ping.py').text
    with open('./bot_plugins/ping.py','r+',encoding='gb18030', errors='ignore') as file:
        old=file.read()
    
    if old!=new:
        with open('./bot_plugins/ping.py','w+') as file:
            file.write(new)
        flag=True
    
    #bot.py
    new=s.get('https://ghproxy.com/https://raw.githubusercontent.com/Lotuses-robot/QQ_bot_for_Dynamic_map/main/bot.py').text
    with open('bot.py','r+',errors='ignore') as file:
        old=file.read()
    
    if old!=new:
        with open('bot.py','w+') as file:
            file.write(new)
        flag=True
    
    #bot_config.py
    new=s.get('https://ghproxy.com/https://raw.githubusercontent.com/Lotuses-robot/QQ_bot_for_Dynamic_map/main/bot_config.py').text
    with open('bot_config.py','r+', errors='ignore') as file:
        old=file.read()
    
    if old!=new:
        with open('bot_config.py','w+') as file:
            file.write(new)
        flag=True
    

    #fl.py
    new=s.get('https://ghproxy.com/https://raw.githubusercontent.com/Lotuses-robot/QQ_bot_for_Dynamic_map/main/fl.py').text
    with open('fl.py','r+',encoding='gbk', errors='ignore') as file:
        old=file.read()
    
    if old!=new:
        with open('fl.py','w+') as file:
            file.write(new)
        flag=True

    #main.py
    new=s.get('https://ghproxy.com/https://raw.githubusercontent.com/Lotuses-robot/QQ_bot_for_Dynamic_map/main/main.py').text
    with open('main.py','r+',encoding='gbk', errors='ignore') as file:
        old=file.read()
    
    if old!=new:
        with open('main.py','w+') as file:
            file.write(new)
        flag=True

    if flag==True:
        start('AutoUpdate.bat')

    time.sleep(60*60*10)
    
