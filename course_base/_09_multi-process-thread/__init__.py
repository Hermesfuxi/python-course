from multiprocessing import Process
import os

def func1():
    print('func1 hello world')

def func2():
    print('func2 add some person')

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p1 = Process(target=func1)
    p2 = Process(target=func2)
    print('Child process will start.')
    p1.start()
    p2.start()