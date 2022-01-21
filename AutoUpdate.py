import os
import time
from tkinter.messagebox import RETRY
import requests
import socket
s=requests.session()
socket.setdefaulttimeout(1000000)
headers={'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36 Edg/97.0.1072.62'}

def start(txt):
    os.system('start cmd /k '+txt)

def check_update(txt):
    new=s.get('https://raw.githubusercontents.com/Lotuses-robot/QQ_bot_for_Dynamic_map/main/'+txt,headers=headers,timeout=100000).content
    new.replace(b'\r\n',b'\n')
    # print(new)
    with open(txt,'rb') as file:
        old=file.read()
    # print(old)
    if old!=new:
        with open(txt,'wb') as file:
            file.write(new)
        return False
    
    return True

# time.sleep(60)
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
        ver=s.get('https://raw.githubusercontents.com/Lotuses-robot/QQ_bot_for_Dynamic_map/main/Version',headers=headers,timeout=100000).text
        ver=ver.replace('\n','')
        imf=s.get('https://raw.githubusercontents.com/Lotuses-robot/QQ_bot_for_Dynamic_map/main/'+ver,headers=headers,timeout=100000).text
        # print('step2:',imf)
        imf=imf.replace('\r\n','\n')
        print(imf)
        s.get('http://127.0.0.1:5700/send_group_msg?group_id=865811340&message='+imf)
        start('AutoUpdate.bat')

    print('no new update.')
    time.sleep(60*60*5)
    