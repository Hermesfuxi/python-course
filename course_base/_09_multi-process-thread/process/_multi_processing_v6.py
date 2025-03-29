from multiprocessing import Process, Manager, current_process

# 使用 Multiprocessing 列表实现栈式进程间数据共享
def send_data(stack):
    for i in range(0, 100):
        stack.append(i)
        print(f'{current_process().name}-{current_process().pid}: sending {i}')

def recv_data(stack):
    while True:
        if stack:
            i = stack.pop()
            print(f'recv {i}')
            print(f'{current_process().name}-{current_process().pid}: receiving {i}')
        else:
            break


if __name__ == '__main__':
    with Manager() as manager:
        stack = manager.list()
        send_p = Process(target=send_data, args=(stack,))
        recv_p = Process(target=recv_data, args=(stack,))
        send_p.start()
        recv_p.start()
        send_p.join()
        recv_p.join()


    print('Child process end.')