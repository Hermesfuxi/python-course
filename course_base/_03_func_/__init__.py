import time
def timer(func, params):
    start_time = time.time()
    result = func(params)
    end_time = time.time()
    print(f"{func.__name__} 函数执行时间为: {end_time - start_time}s")
    return result

def fibonacci_sequence_v1(n: int):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_sequence_v1(n - 1) + fibonacci_sequence_v1(n - 2)

def fibonacci_sequence_v2(n: int):
    if n == 0 or n == 1:
        return n
    else:
        a = 0
        b = 1
        c = 1
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return c


if __name__ == '__main__':
    print(timer(fibonacci_sequence_v1, 40))
    print(timer(fibonacci_sequence_v2, 40))