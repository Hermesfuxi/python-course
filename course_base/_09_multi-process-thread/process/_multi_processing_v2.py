from multiprocessing import Process, current_process
import os

def num_sqrt(num):
    print(f'subprocess {current_process().name} - {current_process().pid}: result 为 {num * num}')

if __name__ == '__main__':
    print(f'main parent process: {os.getppid()}')
    print('main process %s.' % os.getpid())

    processes = []
    for i in range(0, 100):
        process = Process(target=num_sqrt, args=(i,), name=f'p-{i}')
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print('Child process end.')