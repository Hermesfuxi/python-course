from threading import Thread, current_thread
import time, os


def num_sqrt(num):
    print(f'thread {current_thread().name} - {current_thread().native_id}: result 为 {num * num}')

print('--------------init------------------')

if __name__ == '__main__':
    print(f'thread {current_thread().name} - {current_thread().native_id}: main thread start')
    threads = []
    for i in range(0, 100):
        thread = Thread(target=num_sqrt, args=(i,),name=f'thread {i}')
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    for i in range(10):
        print("father running...")
        time.sleep(1)