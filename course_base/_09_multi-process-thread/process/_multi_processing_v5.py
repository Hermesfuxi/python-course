from multiprocessing import Process, Queue, current_process
import os

def send_data(queue):
    for i in range(0, 100):
        queue.put(i)
        print(f'{current_process().name}-{current_process().pid}: sending {i}')

def recv_data(queue):
    while True:
        if queue.empty():
            break
        else:
            # 参数为True时，不阻塞
            # i = queue.get(True)
            i = queue.get()
            print(f'recv {i}')
            print(f'{current_process().name}-{current_process().pid}: receiving {i}')


if __name__ == '__main__':
    queue = Queue()
    # 使用池简化流程管理
    send_p = Process(target=send_data, args=(queue,))
    recv_p = Process(target=recv_data, args=(queue,))
    send_p.start()
    recv_p.start()
    send_p.join()
    recv_p.join()

    print('Child process end.')