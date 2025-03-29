import socket

hostname = socket.gethostname()
port = 9090

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as service:
    # 1, 创建套接字对象
    # ————对象初始化————
    # 2、绑定IP和端口
    service.bind((hostname, port))
    # 3、设置接收最大数
    service.listen(5)

    while True:
        conn, addr = service.accept()
        msg1 = '欢迎来到AI人工智能进阶班！' + "\r\n"
        conn.send(bytes(msg1, 'utf-8'))

        print(conn, addr)
        recv_msg = conn.recv(1024).decode('utf-8')
        print(recv_msg)

