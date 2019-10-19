import socket, time, re
from machine import Pin



html="""
    <html>
    <head>
      <META HTTP-EQUIV="Content-Type" CONTENT="text/html">
      <title>LED控制</title>
    </head>
    <body>
    <form>
    	<span id="status" name="status">%s</span>
    	<input type="button" value="转换" onclick="onSubmit()">
    </from>
    </body>
    </html>
    <script>
    function onSubmit(){
    if (window.XMLHttpRequest) {
        // 用于现代浏览器的代码,code for IE7+, Firefox, Chrome, Opera, Safari
         xmlhttp = new XMLHttpRequest();
     } else {
        // 应对老版本 IE 浏览器的代码,// code for IE6, IE5
         xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
     }
    
    xmlhttp.onreadystatechange = function() {
      if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
        document.getElementById("status").innerHTML = xmlhttp.responseText;
        // document.getElementById("status").value = xmlhttp.responseText;
      }
    }
    xmlhttp.open("GET", "led", true);
    xmlhttp.send("ssss");
    }
    </script>
"""

wlan = do_connect()
ip = wlan.ifconfig()[0]
port = 80
led = Pin(14, Pin.OUT)
webserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)    #创建套接字
webserver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  #设置给定套接字选项的值
#webserver.settimeout(2000)
webserver.bind((ip, port))                                       #绑定IP地址和端口号
webserver.listen(5)                                              #监听套接字
print("服务器地址:%s:%d" %(ip,port))

while True:
  conn, addr = webserver.accept()                                #接受一个连接，conn是一个新的socket对象
  #print("in %s" % str(addr))
  request = conn.recv(1024)                              #从套接字接收1024字节的数据
  if len(request)>0:
    request = request.decode()
    result = re.search("(.*?) (.*?) HTTP/1.1", request)
    if result:
      method = result.group(1)
      url = result.group(2)
      print(url)
      if method == "POST":
        postdata = re.search(".*?\r\n\r\n(.*)", request).group(1)
        if postdata:
          lists = postdata.split("&")
          payload = {}
          for list in lists:
            k,v = list.split("=")
            payload[k]=v
          #print(payload)
      #conn.sendall("HTTP/1.1 200 OK\nConnection: close\nServer: Esp8266\nContent-Type: text/html;charset=UTF-8\n\n")
      conn.send("HTTP/1.1 200 OK\r\n")
      conn.send("Server: Esp8266\r\n")
      conn.send("Content-Type: text/html;charset=UTF-8\r\n")
      conn.send("Connection: close\r\n")
      conn.send("\r\n")
      if url =="/":
        conn.sendall(html % ("灯亮" if led.value()==0 else "灯灭"))
      elif url == "/led":
        if method == "POST":
          status = payload.get("status")
          if status=="on":
            led.value(0)
          elif status=="off":
            led.value(1)
        else:
          led.value(not led.value())
        conn.sendall("灯亮" if led.value()==0 else "灯灭")
        #conn.send(str(led.value()))
      conn.send("\r\n")  # 发送结束
    else:
      print("not found url")
  else:
    print("no request")
  conn.close()
  #print("out %s" % str(addr))

