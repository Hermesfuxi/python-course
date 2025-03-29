import socket

hostname = socket.gethostname()
port = 9090

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:

    client_socket.connect((hostname, port))
    while True:
        recv = client_socket.recv(1024).decode('utf-8')
        print(recv)
        if not recv:
            break
