# 定义一个参数为不定长（可变）类型的函数fun，同时传入一个列表和字典，求列表里的数字元素和字典里的value值它们的累积结果
# 例如：列表[1,2,3]，字典{‘a’: 4,‘b’: 5, ‘c’: 6},定义一个函数fun，输出它们的累积结果（1+2+3+4+5+6）
from typing import Union

def fun2(*args, **kwargs):
    total = 0
    # 遍历不定长参数中的列表
    for arg in args:
        if isinstance(arg, (int, float)):
            total += arg
        elif isinstance(arg, dict):
            total += fun2(*arg.values())
        elif isinstance(arg, list):
            total += fun2(*arg)

    # 遍历不定长参数中的字典
    for kwarg in kwargs:
        arg = kwargs[kwarg]
        if isinstance(arg, (int, float)):
            total += arg
        elif isinstance(arg, dict):
            total += fun2(*arg.values())
        elif isinstance(arg, list):
            total += fun2(*arg)
    return total

# 测试函数
my_list = [1, 2, 3]
my_list2 = [1, 2, 3, 'a', 'b', 'c', my_list]
my_dict = {'a': 4, 'b': 5, 'c': 6}
my_dict2 = {'a': 4, 'b': 5, 'c': 6, 'd': 'e', 'e': 'f', 'lst2': my_list2}
print(fun2(my_list,*my_list, my_dict, *my_dict, **my_dict))
print(fun2(my_list, **my_dict))
print(fun2(*my_list, my_dict, *my_dict, **my_dict))
print(fun2(my_list2, *my_list2, my_dict2, **my_dict2))
