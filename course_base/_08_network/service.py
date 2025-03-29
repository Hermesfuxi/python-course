import socket

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
    client_socket, addr = serversocket.accept()

    print(f"连接地址: {addr}")

    msg1 = '欢迎访问W3Cschool教程！' + "\r\n"
    client_socket.send(msg1.encode('utf-8'))

    msg = client_socket.recv(1024).decode('utf-8')
    print(f'{addr}:{msg}')


    # clientsocket.close()