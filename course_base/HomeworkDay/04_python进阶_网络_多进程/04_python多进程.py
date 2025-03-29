# （1）请使用多任务形式完成：
# 一边编程、一边听音乐、一边跟同事聊天。
# 要求如下：
# a.使用多进程完成；
# b.执行效果图。

from multiprocessing import Process, current_process
import os, subprocess, signal

def kill_subprocess_v1(pid):
    try:
        os.kill(pid, signal.SIGILL)
        print(f"进程 {pid} 已成功终止")
    except ProcessLookupError:
        print(f"没有找到进程 {pid}")
    except PermissionError:
        print(f"没有权限终止进程 {pid}")

# kill -9 pid 只在linux系统生效
def kill_subprocess_v2_linux(pid):
    try:
        subprocess.run(['kill', '-9', str(pid)], check=True)
        print(f"进程 {pid} 已成功终止")
    except ProcessLookupError:
        print(f"没有找到进程 {pid}")
    except PermissionError:
        print(f"没有权限终止进程 {pid}")

def program():
    pid = os.getpid()
    cp = current_process()
    print(f'{cp.name} - {pid}: play program...')

    # 杀死当前进程，则后面的打印代码不执行
    kill_subprocess_v1(pid) # 不在进程内部 调用 terminate() 或 kill() 方法
    # 打印
    print(cp.pid, pid, os.getppid())


def music():
    pid = os.getpid()
    cp = current_process()
    print(f'{cp.name} - {pid}: listen music...')

    print(cp.pid, pid, os.getppid())

    while True:
    # for _ in range(10000):
        print('listen music...')

def chat():
    pid = os.getpid()
    cp = current_process()
    print(f'{cp.name} - {pid}: chat with someone...')
    print(cp.pid, pid, os.getppid())

    while True:
    # for _ in range(10000):
        print('chat with someone...')

if __name__ == '__main__':
    print(current_process().pid, os.getpid(), os.getppid())

    p_program = Process(target=program, name="program-1")
    p_music = Process(target=music, name="music-1")
    p_chat = Process(target=chat, name="chat-1")

    # p_music.daemon = True
    # p_chat.daemon = True

    p_program.start()
    p_music.start()
    p_chat.start()

    # p_program.join()
    # p_music.join()
    # p_chat.join()