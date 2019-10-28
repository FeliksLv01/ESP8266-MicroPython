import time
from machine import Pin


MY_SSID = "PandoraBox-2.4G"
MY_PASSWORD = "104104104"

def do_connect(essid,password):
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(essid,password)
        time.sleep(10) # 连接有延时，睡眠10秒         
    print('network config:', wlan.ifconfig())
    return wlan.isconnected()

def dis_connect():
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(False)
    print('network config:', wlan.ifconfig())

do_connect(MY_SSID,MY_PASSWORD)

import urequests

url='http://i.tianqi.com/index.php?c=code&a=getcode&id=55&py=hongshan'

r = urequests.get(url)   # 发起HTTP的GET请求
content = r.text


import ure as re
print('农历')
nongli = re.search(r'<li class="t3">(.*?)</li>', content)
nongli = nongli.group(1)
print (nongli)

print('天气')
# r'<span style="font-size:14px;width: 70px;line-height: 18px;height: 18px;overflow: hidden;">雷阵雨</span>  这是是原文的串
tianqi = re.search(r'height: 18px;overflow: hidden;">(.*?)</span>', content)
tianqi = tianqi.group(1)
print (tianqi)

print('温度')
# r'<h5><span class="f1">27</span>~<span class="f2">34</span></h5>'  这是是原文的串
wendu = re.search(r'<h5><span class="f1">(.*?)</span>~<span class="f2">(.*?)</span></h5>', content)
wendua = wendu.group(1)
wendub = wendu.group(2)
print (wendua,wendub)

print('指数')
zhushui = re.search(r'height:36px"><h4>(.*?)</h4><p>(.*?)</p></a></div>', content)
zhushuia = zhushui.group(1)
zhushuib = zhushui.group(2)
print (zhushuia,zhushuib)




