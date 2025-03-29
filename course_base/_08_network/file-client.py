#!/usr/bin/python3
# 文件名：client.py

# 导入 socket、sys 模块
import socket
import sys

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()
# host = '192.168.13.62'

# 设置端口号
port = 9999

# 连接服务，指定主机和端口
s.connect((host, port))
# s.connect(('192.168.13.62', 8888))

# 接收小于 1024 字节的数据
# msg = s.recv(1024).decode('utf-8')
# print (msg)

# s.send("发个好人卡".encode('utf-8'))
while True:
#     send_msg = input("请输入消息：")
#     s.send(send_msg.encode('utf-8'))
    file_address = input('请输入文件地址：')
    with open(file_address, 'rb') as f:
        while True:
            data = f.read(1024)
            s.send(data)
            if not data:
                break

s.close()

