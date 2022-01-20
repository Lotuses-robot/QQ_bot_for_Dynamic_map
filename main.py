#coding=gbk
import requests
import urllib3
import json
import time
urllib3.disable_warnings()
headers={'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36 Edg/97.0.1072.62'}

s = requests.session()
s.headers = headers
lastt=0

def try_getj():
    while True:
        t=int(time.time()*1000)
        # print(t)
        j=s.get('https://map.oiercraft.ga:20684/up/world/world/'+str(t),verify=False).content
        j=j.decode('unicode_escape')
        
        try:
            j=json.loads(j)
        except:
            time.sleep(2)
            continue
        
        break

    return j

while True:
    mxt=-1
    t=int(time.time()*1000)
    # print(t)
    j=s.get('https://map.oiercraft.ga:20684/up/world/world/'+str(t),verify=False).content
    try:
        j=j.decode('unicode_escape')
    except:
        time.sleep(3)
        continue

    l=j.find('"type": "chat"')
    while l!=-1:
        l2=j.find('"timestamp":',l)
        l2+=len('"timestamp": 1642663591149}')
        try:
            lst=json.loads(j[l-1:l2])
        except:
            pass

        if lst['timestamp']>lastt and lst['source']!='web':
            s.get('http://127.0.0.1:5700/send_group_msg?group_id=865811340&message=【服务器】'+lst['account']+': '+lst['message'])
            print(lst['timestamp'],lastt,'【服务器】'+lst['account']+': '+lst['message']+'\n')
            mxt=max(mxt,lst['timestamp'])
        l=j.find('"type": "chat"',l+1)
    if mxt!=-1:
        lastt=mxt
    time.sleep(3)
    
