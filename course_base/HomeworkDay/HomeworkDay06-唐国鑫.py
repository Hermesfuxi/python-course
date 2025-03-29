# 编写一个函数 `greet`，接受一个参数 `name`，并返回字符串 `"Hello, [name]!"`。
def greet(name: str) -> str:
    return(f'Hello, [{name}]!')

print(greet('John'))

# 编写一个函数 `add`，接受两个参数 `a` 和 `b`，返回它们的和。如果 `a` 或 `b` 不是数字，返回 `"参数必须是数字"`。
def add(a: int, b: int) -> int | str:
    if isinstance(a, int) and isinstance(b, int):
        return a + b
    else:
        return('参数必须是数字')

print(add(1, 2))

# 编写一个函数 `average`，接受任意数量的参数，返回这些参数的平均值。
def average(*args: int) -> float:
    if len(args) == 0:
        return 0
    else:
        return sum(args) / len(args)

print(average(1, 2, 3, 4, 5))

# 编写一个函数 `outer`，在函数内部定义另一个函数 `inner`，`inner` 函数返回传入参数的平方。`outer` 函数返回 `inner` 函数的调用结果。
def outer():
    def inner(x: int) -> int:
        return x ** 2
    return inner
print(outer()(2))

def outer1(num):
    def inner(x: int) -> int:
        return x ** 2
    return inner(num)
print(outer1(2))

# 编写一个函数 `modify_global`，在函数内部修改全局变量 `x = 10`，将其值改为 `20`。使用 `global` 关键字。
x = 10
def modify_global():
    global x
    x = 20

modify_global()
print(x)

# 使用 `lambda` 表达式编写一个函数，接受两个参数 `x` 和 `y`，返回它们的乘积。
print((lambda x, y: x * y)(1,1))

# 编写一个列表推导式，生成一个包含1到20之间所有偶数的平方的列表。
print([x**2 for x in range(2, 21, 2)])
