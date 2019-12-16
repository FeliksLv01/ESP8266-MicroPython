import requests
import re

url = 'http://i.tianqi.com/index.php?c=code&a=getcode&id=55&py=hongshan'

r = requests.get(url)  # 发起HTTP的GET请求
content = r.text

print('农历')
nongli = re.search(r'<li class="t3">(.*?)</li>', content)
nongli = nongli.group(1)
print(nongli)

print('天气')
tianqi = re.search(r'height: 18px;overflow: hidden;">(.*?)</span>', content)
tianqi = tianqi.group(1)
print(tianqi)

print('温度')

wendu = re.search(
    r'<h5><span class="f1">(.*?)</span>~<span class="f2">(.*?)</span></h5>',
    content)
wendua = wendu.group(1)
wendub = wendu.group(2)
print(wendua, wendub)

print('指数')
zhushui = re.search(r'height:36px"><h4>(.*?)</h4><p>(.*?)</p></a></div>',
                    content)
zhushuia = zhushui.group(1)
zhushuib = zhushui.group(2)
print(zhushuia, zhushuib)
