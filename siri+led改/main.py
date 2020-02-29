import socket
from machine import Pin
from re import search
from web import do_connect

html = """
<html>
  <head>
    <META HTTP-EQUIV="Content-Type" CONTENT="text/html">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LED控制</title>
  </head>
  <body>
    <p>Hello World!!!</p>
  </body>
</html>
"""

wlan = do_connect()
ip = wlan.ifconfig()[0]
port = 80
led = Pin(2, Pin.OUT)
webserver = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建套接字
webserver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 设置给定套接字选项的值
webserver.bind((ip, port))  # 绑定IP地址和端口号
webserver.listen(5)  # 监听套接字
print("服务器地址:{}:{}".format(ip, port))

while True:
    conn, addr = webserver.accept()
    request = conn.recv(1024)
    if len(request) > 0:
        request = request.decode()
        result = search("(.*?) (.*?) HTTP/1.1", request)
        if result:
            method = result.group(1)
            url = result.group(2)
            print(url)
            conn.send("HTTP/1.1 200 OK\r\n")
            conn.send("Server: Esp8266\r\n")
            conn.send("Content-Type: text/html;charset=UTF-8\r\n")
            conn.send("Connection: close\r\n")
            conn.send("\r\n")
            if url == "/led1":
                led.value(1)
                conn.send("灯灭")
            elif url == "/led2":
                led.value(0)
                conn.send("灯亮")
            else:
                conn.sendall(html)
            conn.send("\r\n")  # 发送结束
        else:
            print("not found url")
    else:
        print("no request")
    conn.close()
