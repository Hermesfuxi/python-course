from multiprocessing import Process, Pipe
import os

def send_data(send_con):
    send_con.send('hello world')
    send_con.close()

def recv_data(recv_con):
    recv = recv_con.recv()
    print(recv)
    recv_con.close()

if __name__ == '__main__':
    print(f'main parent process: {os.getppid()}')
    print('main process %s.' % os.getpid())

    recv_con, send_con = Pipe()
    # 使用池简化流程管理
    send_p = Process(target=send_data, args=(send_con,))
    recv_p = Process(target=recv_data, args=(recv_con,))
    send_p.start()
    recv_p.start()
    send_p.join()
    recv_p.join()
    print('Child process end.')