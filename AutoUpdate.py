import os
import time
from tkinter.messagebox import RETRY
import requests
import socket
s=requests.session()
socket.setdefaulttimeout(1000000)
headers={'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36 Edg/97.0.1072.62'}
mirror='https://raw.githubusercontents.com/Lotuses-robot/QQ_bot_for_Dynamic_map/main/'

def start(txt):
    os.system('start cmd /k '+txt)

def GetFile(txt):
    return s.get(mirror+txt).content

# time.sleep(60)
with open('Version','r+') as file:
    v=file.read()

while True:

    flag=True
    nv=str(GetFile('Version'))

    if nv!=v:
        with open('Version','w+') as file:
            file.write(nv)
        
        with open('bot.py','w+') as file:
            file.write(GetFile('bot.py'))
        
        with open('bot_plugins/bot.py','w+') as file:
            file.write(GetFile('bot_plugins/bot.py'))

        with open('fl.py','w+') as file:
            file.write(GetFile('fl.py'))

        with open('main.py','w+') as file:
            file.write(GetFile('main.py'))

        imf=str(GetFile(nv))

        s.get('http://127.0.0.1:5700/send_group_msg?group_id=865811340&message='+imf)

        start('AutoUpdate.py')
        exit()

    print('no new update.')
    time.sleep(60*60*5)
    