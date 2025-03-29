from multiprocessing import current_process, Pool
import os, time, random

def num_sqrt(num):
    print(f'Running task {num}({os.getpid()})...')
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print(f'subprocess {current_process().name} - {current_process().pid}: result 为 {num * num}, 用时: {end-start}')

if __name__ == '__main__':
    print(f'main parent process: {os.getppid()}')
    print('main process %s.' % os.getpid())
    # 使用池简化流程管理: 由于Pool的默认大小是CPU的核数，如果你不幸拥有8核CPU，你要提交至少9个子进程才能看到等待效果。
    with Pool(10) as pool:
        # pool.map(num_sqrt, range(300))
        for i in range(30):
            result = pool.apply_async(num_sqrt, args=(i,))
            result.get()

        # 有 with 不需要 close() 和 join()
        # 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
        # pool.close()
        # pool.join()
    print('Child process end.')