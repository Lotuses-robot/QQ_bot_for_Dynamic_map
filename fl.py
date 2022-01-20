#coding=gbk
from flask import Flask,request
from queue import Queue
from json import loads
import _thread
import requests
import urllib3
import time
q=Queue(10000)
urllib3.disable_warnings()
headers={'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36 Edg/97.0.1072.62'}

s = requests.session()
s.headers = headers

def send_msg():
    while True:
        try:
            txt=q.get()
        except:
            continue

        try:
            r=s.post('https://map.oiercraft.ga:20684/up/sendmessage',json={'name':'','message':'【QQ群】'+txt},timeout=10000,verify=False)
            code=r.status_code
            print(code+'\n')
        except:
            pass
        
        time.sleep(5)

bot_server = Flask(__name__)

@bot_server.route('/',methods=['POST'])
#路径是你在酷Q配置文件里自定义的
def server():
    data = request.get_data().decode('utf-8')
    data = loads(data)
    try:
        if data['message_type']=='group' and data['group_id']==865811340:
            q.put(data['sender']['card']+' | '+data['sender']['nickname']+': '+data['message'])

    except:
        #print('no')
        return ''
    #print(data)
    return ''

if __name__ == '__main__':
    _thread.start_new_thread( send_msg, ( ) )
    bot_server.run(port=5701)
