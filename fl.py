#coding=utf-8

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

l = [['[CQ:face,id=14]', '【微笑】'], ['[CQ:face,id=1]', '【撇嘴】'], ['[CQ:face,id=2]', '【色】'], ['[CQ:face,id=3]', '【发呆】'], ['[CQ:face,id=4]', '【得意】'], ['[CQ:face,id=5]', '【流泪】'], ['[CQ:face,id=6]', '【害羞】'], ['[CQ:face,id=7]', '【闭嘴】'], ['[CQ:face,id=8]', '【睡】'], ['[CQ:face,id=9]', '【大哭】'], ['[CQ:face,id=10]', '【尴尬】'], ['[CQ:face,id=11]', '【发怒】'], ['[CQ:face,id=12]', '【调皮】'], ['[CQ:face,id=13]', '【呲牙】'], ['[CQ:face,id=0]', '【惊讶】'], ['[CQ:face,id=15]', '【难过】'], ['[CQ:face,id=16]', '【酷】'], ['[CQ:face,id=96]', '【冷汗】'], ['[CQ:face,id=18]', '【抓狂】'], ['[CQ:face,id=19]', '【吐】'], ['[CQ:face,id=20]', '【偷笑】'], ['[CQ:face,id=21]', '【可爱】'], ['[CQ:face,id=22]', '【白眼】'], ['[CQ:face,id=23]', '【傲慢】'], ['[CQ:face,id=24]', '【饥饿】'], ['[CQ:face,id=25]', '【困】'], ['[CQ:face,id=26]', '【惊恐】'], ['[CQ:face,id=27]', '【流汗】'], ['[CQ:face,id=28]', '【憨笑】'], ['[CQ:face,id=29]', '【悠闲】'], ['[CQ:face,id=30]', '【奋斗】'], ['[CQ:face,id=31]', '【咒骂】'], ['[CQ:face,id=32]', '【疑问】'], ['[CQ:face,id=33]', '【嘘】'], ['[CQ:face,id=34]', '【晕】'], ['[CQ:face,id=35]', '【折磨】'], ['[CQ:face,id=36]', '【衰】'], ['[CQ:face,id=37]', '【骷髅】'], ['[CQ:face,id=38]', '【敲打】'], ['[CQ:face,id=39]', '【再见】'], ['[CQ:face,id=97]', '【擦汗】'], ['[CQ:face,id=98]', '【抠鼻】'], ['[CQ:face,id=99]', '【鼓掌】'], ['[CQ:face,id=100]', '【糗大了】'], ['[CQ:face,id=101]', '【坏笑】'], ['[CQ:face,id=102]', '【左哼哼】'], ['[CQ:face,id=103]', '【右哼哼】'], ['[CQ:face,id=104]', '【哈欠】'], ['[CQ:face,id=105]', '【鄙视】'], ['[CQ:face,id=106]', '【委屈】'], ['[CQ:face,id=107]', '【快哭了】'], ['[CQ:face,id=108]', '【阴险】'], ['[CQ:face,id=305]', '【右亲亲】'], ['[CQ:face,id=109]', '【左亲亲】'], ['[CQ:face,id=110]', '【吓】'], ['[CQ:face,id=111]', '【可怜】'], ['[CQ:face,id=172]', '【眨眼睛】'], ['[CQ:face,id=182]', '【笑哭】'], ['[CQ:face,id=179]', '【doge】'], ['[CQ:face,id=173]', '【泪奔】'], ['[CQ:face,id=174]', '【无奈】'], ['[CQ:face,id=212]', '【托腮】'], ['[CQ:face,id=175]', '【卖萌】'], ['[CQ:face,id=178]', '【斜眼笑】'], ['[CQ:face,id=177]', '【喷血】'], ['[CQ:face,id=180]', '【惊喜】'], ['[CQ:face,id=181]', '【骚扰】'], ['[CQ:face,id=176]', '【小纠结】'], ['[CQ:face,id=183]', '【我最美】'], ['[CQ:face,id=245]', '【加油必胜】'], ['[CQ:face,id=246]', '【加油抱抱】'], ['[CQ:face,id=247]', '【口罩护体】'], ['[CQ:face,id=78]', '【握手】'], ['[CQ:face,id=79]', '【胜利】'], ['[CQ:face,id=118]', '【抱拳】'], ['[CQ:face,id=119]', '【勾引】'], ['[CQ:face,id=120]', '【拳头】'], ['[CQ:face,id=121]', '【差劲】'], ['[CQ:face,id=122]', '【爱你】'], ['[CQ:face,id=123]', '【NO】'], ['[CQ:face,id=124]', '【OK】'], ['[CQ:face,id=42]', '【爱情】'], ['[CQ:face,id=85]', '【飞吻】'], ['[CQ:face,id=43]', '【跳跳】'], ['[CQ:face,id=41]', '【发抖】'], ['[CQ:face,id=86]', '【恼火】'], ['[CQ:face,id=125]', '【转圈】'], ['[CQ:face,id=126]', '【磕头】'], ['[CQ:face,id=127]', '【回头】'], ['[CQ:face,id=128]', '【跳绳】'], ['[CQ:face,id=129]', '【挥手】'], ['[CQ:face,id=130]', '【激动】'], ['[CQ:face,id=131]', '【街舞】'], ['[CQ:face,id=132]', '【献吻】'], ['[CQ:face,id=133]', '【左太极】'], ['[CQ:face,id=134]', '【右太极】'], ['[CQ:face,id=136]', '【双喜】'], ['[CQ:face,id=137]', '【hpny】'], ['[CQ:face,id=138]', '【灯笼】'], ['[CQ:face,id=140]', '【K歌】'], ['[CQ:face,id=144]', '【喝彩】'], ['[CQ:face,id=146]', '【爆筋】'], ['[CQ:face,id=147]', '【棒棒糖】'], ['[CQ:face,id=148]', '【喝奶】'], ['[CQ:face,id=151]', '【飞机】'], ['[CQ:face,id=158]', '【钞票】'], ['[CQ:face,id=168]', '【药】'], ['[CQ:face,id=169]', '【手枪】'], ['[CQ:face,id=188]', '【蛋】'], ['[CQ:face,id=192]', '【红包】'], ['[CQ:face,id=184]', '【河蟹】'], ['[CQ:face,id=185]', '【羊驼】'], ['[CQ:face,id=190]', '【菊花】'], ['[CQ:face,id=187]', '【幽灵】'], ['[CQ:face,id=193]', '【大笑】'], ['[CQ:face,id=194]', '【不开心】'], ['[CQ:face,id=197]', '【冷漠】'], ['[CQ:face,id=198]', '【呃】'], ['[CQ:face,id=199]', '【好棒】'], ['[CQ:face,id=200]', '【拜托】'], ['[CQ:face,id=201]', '【点赞】'], ['[CQ:face,id=202]', '【无聊】'], ['[CQ:face,id=203]', '【托脸】'], ['[CQ:face,id=204]', '【吃】'], ['[CQ:face,id=205]', '【送花】'], ['[CQ:face,id=206]', '【害怕】'], ['[CQ:face,id=207]', '【花痴】'], ['[CQ:face,id=208]', '【小样】'], ['[CQ:face,id=210]', '【飙泪】'], ['[CQ:face,id=211]', '【我不看】'], ['[CQ:face,id=278]', '【汗】'], ['[CQ:face,id=279]', '【打脸】'], ['[CQ:face,id=280]', '【击掌】'], ['[CQ:face,id=242]', '【头撞击】'], ['[CQ:face,id=243]', '【甩头】'], ['[CQ:face,id=244]', '【扔狗】'], ['[CQ:face,id=215]', '【糊脸】'], ['[CQ:face,id=237]', '【偷看】'], ['[CQ:face,id=226]', '【拍桌】'], ['[CQ:face,id=214]', '【啵啵】'], ['[CQ:face,id=217]', '【扯一扯】'], ['[CQ:face,id=240]', '【喷脸】'], ['[CQ:face,id=216]', '【拍头】'], ['[CQ:face,id=218]', '【舔一舔】'], ['[CQ:face,id=229]', '【干杯】'], ['[CQ:face,id=238]', '【扇脸】'], ['[CQ:face,id=219]', '【蹭一蹭】'], ['[CQ:face,id=225]', '【撩一撩】'], ['[CQ:face,id=231]', '【哼】'], ['[CQ:face,id=233]', '【掐一掐】'], ['[CQ:face,id=221]', '【顶呱呱】'], ['[CQ:face,id=222]', '【抱抱】'], ['[CQ:face,id=239]', '【原谅】'], ['[CQ:face,id=232]', '【佛系】'], ['[CQ:face,id=220]', '【拽炸天】'], ['[CQ:face,id=235]', '【颤抖】'], ['[CQ:face,id=241]', '【生日快乐】'], ['[CQ:face,id=230]', '【嘲讽】'], ['[CQ:face,id=224]', '【开枪】'], ['[CQ:face,id=236]', '【啃头】'], ['[CQ:face,id=228]', '【恭喜】'], ['[CQ:face,id=234]', '【惊呆】'], ['[CQ:face,id=223]', '【暴击】'], ['[CQ:face,id=227]', '【拍手】']]
s = requests.session()
s.headers = headers

def decode_cq(txt):
    for s in l:
        txt = txt.replace(s[0], s[1])
    return txt

def send_msg():
    while True:
        try:
            txt = decode_cq(q.get())
        except:
            continue

        try:
            r = s.post('https://map.oiercraft.ga:20684/up/sendmessage',json = {'name' : '', 'message' : txt}, timeout = 10000, verify = False)
            code = r.status_code
            print(code+'\n')
        except:
            pass
        
        time.sleep(3)

bot_server = Flask(__name__)

@bot_server.route('/',methods=['POST'])

def server():
    global l
    data = request.get_data().decode('utf-8')
    data = loads(data)
    # print(data)
    if data['message_type']=='group' and data['group_id']==865811340:
        # q.put(data['sender']['nickname']+': '+data['message'])
        s.post('http://localhost:8123/up/sendmessage',json = {'name' : 'bot', 'message' : decode_cq(data['sender']['nickname']+': '+data['message'])}, timeout = 1, verify = False)
        # else:
        #     if data['message_type']=='private' and data['sender']['user_id']==2814386153:
        #         args=data['message'].split()
        #         if len(args)!=2:
        #             print('A')
        #             print(str(l))
        #         else:
        #             print('B')
        #             l.append([args[0],args[1]])


if __name__ == '__main__':
    _thread.start_new_thread( send_msg, ( ) )
    bot_server.run(port=5701)
