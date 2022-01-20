#coding=utf-8
#coding=gbk

from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
import requests
import time
import json
s=requests.session()
headers={'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36 Edg/97.0.1072.62'}

def makeup(x):
    sends=''
    sends+=x['account']+':\n'
    sends+=str(x['x'])+'  '+str(x['y'])+'  '+str(x['z'])+'\n'
    sends+='health: '+str(x['health'])+'\n'
    sends+='armor: '+str(x['armor'])
    return sends

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

@on_command('q',only_to_me=False)
async def _(session: CommandSession):
    sends=''
    args=session.current_arg_text.strip()
    
    j=try_getj()
    
    j=j['players']
    
    sends=''
    if args=='l':
        for x in j:
            sends+=makeup(x)+'\n\n'
    else:
        for x in j:
            if x['account']==args:
                sends+=makeup(x)

    if sends=='':
        sends='未找到查询用户！'
    
    await session.send(sends)
