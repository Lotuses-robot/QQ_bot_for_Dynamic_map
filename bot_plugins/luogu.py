#coding=utf-8

from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
import requests
import time
import json
import os
s=requests.session()
headers={'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36 Edg/97.0.1072.62'}

def Query_User(id):
    res=s.get('https://www.luogu.com.cn/api/user/search?keyword='+id,headers=headers)
    if res.status_code!=200:
        return {'users':[None]}
    txt=json.loads(res.text)
    return txt

def search_MainPage(content,id):

    Location_start = content.find(id)+len(id)+6
    Location_end = content.find('%',Location_start)

    # print(id,content [ Location_start : Location_end ])

    return content [ Location_start : Location_end ]



def Query_User_Imf(id):
    dic=Query_User(id)
    if(dic['users']==[None]):
        return {"status":"Can't Find this user."}
    
    id=dic['users'][0]['uid']
    
    mainPage = s.get('https://www.luogu.com.cn/user/'+str(id),headers=headers).text

    Following = search_MainPage(mainPage, 'followingCount')

    Follower = search_MainPage(mainPage, 'followerCount')

    Passed = search_MainPage(mainPage, 'passedProblemCount')

    Submited = search_MainPage(mainPage, 'submittedProblemCount')

    Ranked = search_MainPage(mainPage, 'ranking')

    return {'Following':int(Following),'Follower':int(Follower),'Submited':int(Submited),'Passed':int(Passed),'Ranked':int(Ranked)}

def Query_User_gugu(id):
    dic=Query_User(id)
    if(dic['users']==[None]):
        return {"status":"Can't Find this user."}
    
    id=dic['users'][0]['uid']

    # print(id)

    txt=s.get('https://luogu-card.vercel.app/guzhi?id='+str(id),headers=headers).text

    # print(txt)

    if txt.find('text-before-edge')!=-1:
        return {"status":"Can't query this user."}
    
    mod='<text x="0" y="15" class="text">'

    mod2='class="text">'

    loc=end=0

    loc = txt.find(mod,end)+len(mod)
    end = txt.find('<',loc)

    name1=txt[loc:end]

    loc = txt.find(mod2,end)+len(mod2)
    end = txt.find('<',loc)

    value1=txt[loc:end-1]



    loc = txt.find(mod,end)+len(mod)
    end = txt.find('<',loc)

    name2=txt[loc:end]

    loc = txt.find(mod2,end)+len(mod2)
    end = txt.find('<',loc)

    value2=txt[loc:end-1]



    loc = txt.find(mod,end)+len(mod)
    end = txt.find('<',loc)

    name3=txt[loc:end]

    loc = txt.find(mod2,end)+len(mod2)
    end = txt.find('<',loc)

    value3=txt[loc:end-1]



    loc = txt.find(mod,end)+len(mod)
    end = txt.find('<',loc)

    name4=txt[loc:end]

    loc = txt.find(mod2,end)+len(mod2)
    end = txt.find('<',loc)

    value4=txt[loc:end-1]



    loc = txt.find(mod,end)+len(mod)
    end = txt.find('<',loc)

    name5=txt[loc:end]

    loc = txt.find(mod2,end)+len(mod2)
    end = txt.find('<',loc)

    value5=txt[loc:end-1]

    return {name1:int(value1),name2:int(value2),name3:int(value3),name4:int(value4),name5:int(value5)}


@on_command('qlg',only_to_me=False)
async def _(session: CommandSession):
    sends=''
    args=session.current_arg_text.strip().split(' ',1)

    if len(args)<2:
        sends="Args not valid."

    else:
        if args[0]=='usr':
            sends=str(Query_User(args[1]))
        if args[1]=='imf':
            sends=str(Query_User_Imf(args[1]))
        if args[1]=='gugu':
            sends=str(Query_User_gugu(args[1]))
    
    await session.send(sends)

