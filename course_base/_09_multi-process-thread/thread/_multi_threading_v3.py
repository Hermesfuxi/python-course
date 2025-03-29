from threading import Thread, current_thread
from concurrent.futures import ThreadPoolExecutor

import time, os


def num_sqrt(num1, num2):
    result = num1 * num2
    print(f'thread {current_thread().name} - {current_thread().native_id}: {num1} * {num2} = {result}')
    return result

print('--------------init------------------')

if __name__ == '__main__':
    print(f'thread {current_thread().name} - {current_thread().native_id}: main thread start')

    # 使用 with 上下文管理器 管理线程池
    # with ThreadPoolExecutor(max_workers=4) as executor:
    #     executor.map(num_sqrt, range(100))

    # 手动管理线程池（不使用 with 语句）
    executor = ThreadPoolExecutor(max_workers=4)

    # 提交单个任务，返回一个Future对象（代表异步操作的结果）
    # for i in range(100):
    #     future = executor.submit(num_sqrt, i, i+1)
    #     future.result()

    # 批量提交任务，按顺序返回结果
    results = executor.map(num_sqrt, [i for i in range(100)], [i+1 for i in range(100)])
    for result in results:
        print(result)

    # 阻塞等待所有任务完成，再关闭线程池
    executor.shutdown(wait=True)

    for i in range(10):
        print("father running...")
        time.sleep(1)