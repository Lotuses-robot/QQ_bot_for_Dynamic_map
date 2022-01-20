import os
import time
import requests
s=requests.session()

def start(txt):
    os.system('start cmd /k '+txt)

def check_update(txt):
    new=s.get('https://ghproxy.com/https://raw.githubusercontent.com/Lotuses-robot/QQ_bot_for_Dynamic_map/main/'+txt).content
    new.replace(b'\r\n',b'\n')
    print(type(new))
    with open(txt,'rb') as file:
        old=file.read()
    if old!=new:
        with open(txt,'wb') as file:
            file.write(new)
        return False
    
    return True

while True:
    flag=True
    #bot_plugins/ping.py
    flag=flag and check_update('bot_plugins/ping.py')
    #bot.p
    flag=flag and check_update('bot.py')
    #bot_config.py
    flag=flag and check_update('bot_config.py')
    #fl.py
    flag=flag and check_update('fl.py')
    #main.py
    flag=flag and check_update('main.py')

    if flag==False:
        start('AutoUpdate.bat')

    print('no new update.')
    time.sleep(60*60*5)
    