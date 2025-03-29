from multiprocessing import Value, current_process, Process, Lock

# 默认情况下，进程之间不共享内存。每个进程都在自己的内存空间中运行，以实现隔离和安全性
# 然而，复制大量数据的开销并不总是能接受。Python 提供了显式机制来在需要时在进程间共享内存。以下是一些例子：
# * `multiprocessing.shared_memory`（Python 3.8+）
# * `multiprocessing.Value`
# * `multiprocessing.Array`
# 但在使用这些机制时，我们需要非常小心，因为共享内存可能会引发竞争条件问题——线径不安全。例如，以下程序使用 `multiprocessing.Value` 来共享一个整数变量，在四个进程中共享内存：
def num_shard(shard_count, lock):
    # print('*'*30)
    # print(shard_count)

    # for i in range(10):
    #     with lock:
    #         shard_count.value += 1
    #         print(f'{current_process().name}-{current_process().pid}: result - {shard_count.value}...')

    lock.acquire()
    for i in range(10):
        shard_count.value += 1
        print(f'{current_process().name}-{current_process().pid}: result - {shard_count.value}...')
    lock.release()

if __name__ == '__main__':
    shard_counter = Value('i', 0)
    lock = Lock()
    processes = [Process(target=num_shard, args=(shard_counter,lock), name=f'process-{i}')  for i in range(0, 300)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()
    print('Child process end.')