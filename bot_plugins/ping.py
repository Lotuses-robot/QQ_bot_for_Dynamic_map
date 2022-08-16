#coding=utf-8

from re import L
import plotly.graph_objects as go
import plotly.io as io
import plotly.figure_factory as ff

def MakeGra(dic):
    p = io.renderers['png']
    p.width = 750
    p.height = 750  
    f = go.Figure(data = [go.Table(
        columnorder = [1, 2, 3, 4, 5, 6],  # 列属性的顺序
        columnwidth = [680, 400, 200, 400, 220, 220],  # 列属性中元素所占单元格整体大小
        
        # 表头
        header = dict(
            values = [["Name"], ["X"], ["Y"], ["Z"], ["Hea"], ["Arm"]],  # 两个表头
            # line_color = 'darkslategray',  # 线条和填充色
            # fill_color = 'royalblue',
            # # align = 'center', # 位置
            # font = dict(color = 'white', size = 24), # 表头文本的颜色和字体大小
            font_size = 26,
            height = 38  # 高度
        ),
        
        # 单元格设置
        cells = dict(
            values = dic, # 数据
            # line_color = 'darkslategray',  # 线条颜色
            # fill = dict(color = ['paleturquoise', 'white']),
            # # align = ['center'],  # 两个列属性文本显示位置
            font_size = 22,  # 字体大小
            height = 35
        )
    )], layout = {
        "template" : "simple_white",
        "margin" : go.layout.Margin(l = 20, r = 20, b = 20, t = 20, pad = 0)
    })
    # f.show(renderer = "png", height = 600, width = 700)
    io.write_image(f, 'tmp.png', height = 80 + int(len(dic[0]) * 35), width = 660)
    return f

from nonebot.command import CommandSession
from nonebot.experimental.plugin import on_command
import requests
import time
import json
import os
s=requests.session()
headers={'user-agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Mobile Safari/537.36 Edg/97.0.1072.62'}

lll = [[] * 6]

def makeup(x):
    global lll
    lll[0].append(x['account'])
    lll[1].append(x['x'])
    lll[2].append(x['y'])
    lll[3].append(x['z'])
    lll[4].append(x['health'])
    lll[5].append(x['armor'])

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
    global lll
    lll = []
    for i in range(0, 6):
        lll.append([])
    print(lll)
    sends=''
    args=session.current_arg_text.strip()
    
    j=try_getj()
    
    j=j['players']
    
    if args=='l':
        for x in j:
            makeup(x)
    else:
        for x in j:
            if x['account']==args:
                makeup(x)

    if len(lll[0]) == 0:
        sends='未找到查询用户...'
    else:
        MakeGra(lll)
        sends = '[CQ:image,file=file:///E:/bot/tmp.png]'

    await session.send(sends)


@on_command('update', permission=lambda sender: sender.is_superuser)
async def _(session: CommandSession):
    os.system('start cmd /k cd ..&python AutoUpdate.py')
