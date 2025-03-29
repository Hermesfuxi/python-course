from threading import Thread, current_thread
from concurrent.futures import ThreadPoolExecutor
import time

# 使用global关键字实现线程间通信：
# 声明一个全局变量后，同一个进程中的线程可以共享数据
g_sum=100

def change_g(num):
    global g_sum
    print(g_sum)
    for i in range(num+1):
        g_sum += i
    print(f'thread {current_thread().name} - {current_thread().native_id}: result 为 {g_sum}')

if __name__ == '__main__':
    print(f'thread {current_thread().name} - {current_thread().native_id}: main thread start')
    # 手动管理线程池（不使用 with 语句）
    with ThreadPoolExecutor(max_workers=4) as executor:
        for i in range(1, 100):
            future = executor.submit(change_g, i)
            future.result()

    for i in range(10):
        print("father running...")
        time.sleep(1)