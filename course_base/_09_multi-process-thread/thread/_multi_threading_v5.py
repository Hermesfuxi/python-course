from threading import Thread, current_thread
from queue import Queue, Empty

# 使用 队列 实现线程间通信：一个线程写，一个线程读
def write(queue):
    queue.put('hello world')
    for i in range(10):
        s = f'{chr(i+ord('a')+10)}'
        print(s)
        queue.put(s)

def read(queue):
    while True:
        try:
            # 设置超时时间为 1 秒
            item = queue.get(timeout=1)
            if item is None:
                break
            else:
                print(f'thread {current_thread().name} - {current_thread().native_id}: 读取结果为 - {item}')
        except Empty:
            # 超时后可以进行其他操作，这里简单打印提示信息
            print("在指定时间内未获取到元素，稍后重试")
            break

if __name__ == '__main__':
    print(f'thread {current_thread().name} - {current_thread().native_id}: main thread start')
    q = Queue()
    write_t = Thread(target=write, args=(q,))
    read_t = Thread(target=read, args=(q,))

    write_t.start()
    read_t.start()

    write_t.join()
    read_t.join()
