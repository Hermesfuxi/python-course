from threading import Thread, current_thread
import time, os

def print_child():
    for i in range(10):
        print("child running...")
        # time.sleep(1)

def func1():
    print_child()
    print(f'thread {current_thread().name} - {current_thread().native_id}: func1 hello world')

def func2():
    print_child()
    print(f'thread {current_thread().name} - {current_thread().native_id}: func2 add some person')

def func3(name):
    print_child()
    print(f'thread {current_thread().name} - {current_thread().native_id}: func3 hello {name}')

print('--------------init------------------')

if __name__ == '__main__':
    print(f'thread {current_thread().name} - {current_thread().native_id}: main thread start')
    thread1 = Thread(target=func1, name='func1')
    thread2 = Thread(target=func2, name='func2')
    thread3 = Thread(target=func3, name='func3', args=('hermesfuxi',))
    thread1.start()
    thread2.start()
    thread3.start()
    thread1.join()
    thread2.join()
    thread3.join()

    for i in range(10):
        print("father running...")
        time.sleep(1)