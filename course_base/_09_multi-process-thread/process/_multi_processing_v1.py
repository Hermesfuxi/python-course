from multiprocessing import Process, current_process
import os, time

def print_child():
    for i in range(10):
        print("child running...")
        # time.sleep(1)

def func1():
    print_child()
    print(f'subprocess {current_process().pid}: func1 hello world')
    print(os.getpid(), os.getppid(), __name__)

def func2():
    print_child()
    print(f'subprocess {current_process().pid}: func2 add some person')
    print(os.getpid(), os.getppid(), __name__)

def func3(name):
    print_child()
    print(f'subprocess {current_process().pid}: func3 hello {name}')
    print(os.getpid(), os.getppid(), __name__)

print('--------------init------------------')

#  `os.fork()` 函数在 Unix/Linux/Mac 系统上会返回两次，一次在父进程中返回子进程的 ID，一次在子进程中返回 0。
#  具体来说，当父进程调用 `os.fork()` 函数时，它会得到一个大于 0 的整数，这个整数就是子进程的 ID；
#  而当子进程调用 `os.fork()` 函数时，它会得到一个等于 0 的整数。
#  因此，我们可以通过判断返回值来确定当前进程是父进程还是子进程。

if __name__ == '__main__':
    # Windows 不支持 fork()，而是使用 spawn() 方式来创建新进程。
    # 而这种方式每个子进程都会从头开始启动 Python 解释器，并重新执行整个脚本文件以初始化子进程。
    # 因此，在 Windows 上，模块会被重新加载，因为每次启动新的子进程时，Python 都会重新导入并执行主模块中的代码
    # 也就是说， init 会打印多遍，次数 = 主进程（1） + 子进程数
    # 问题在于，进程也会执行生成自身进程的代码，所以必须写在 __name__ 内，才能避免进程的无限嵌套循环
    print(f'main parent process: {os.getppid()}')
    print(f'main process {os.getpid()}.')
    p1 = Process(target=func1)
    p2 = Process(target=func2)
    p3 = Process(target=func3, args=('hermesfuxi',))
    print('Child process will start.')

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

    # 这里用 join 阻塞父进程运行，运行结果为先打印10次“child running...”，然后再打印10次“father running...”
    # 去掉join()，父子进程并发运行=，运行结果为“child running...”、“father running...”交替打印

    for i in range(10):
        print("father running...")
        time.sleep(1)

    print('Child process end.')