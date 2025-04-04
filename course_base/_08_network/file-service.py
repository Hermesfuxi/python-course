import socket
import sys

# 创建 socket 对象
serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

port = 9999

# 绑定端口
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(5)

while True:
    # 建立客户端连接
    clientsocket, addr = serversocket.accept()

    print("连接地址: %s" % str(addr))

    msg1 = '欢迎访问文件系统' + "\r\n"
    clientsocket.send(msg1.encode('utf-8'))

    while True:
        msg = clientsocket.recv(1024)
        if not msg:
            break
        with open('./data-test.txt', 'wb+') as f:
            f.write(msg)


clientsocket.close()