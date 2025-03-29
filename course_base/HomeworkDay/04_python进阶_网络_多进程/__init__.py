import multiprocessing


def worker():
    print(f'Hello from {multiprocessing.current_process().name}')


if __name__ == '__main__':
    # 创建并启动一个进程，同时设置名称
    p = multiprocessing.Process(target=worker, name='CustomName')
    p.start()
    p.join()