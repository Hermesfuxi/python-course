from typing import Iterable, Iterator

class MyStr(Iterable):
    def __init__(self) -> None:
        pass

    # 支持迭代协议（有__iter__()方法）
    def __iter__(self):
        pass

    # 支持迭代器协议：实现__iter__() 和 __next__()方法
    def __next__(self):
        pass

    # 支持序列协议（有__getitem__()方法，且数字参数从0开始）
    def __getitem__(self, item):
        pass