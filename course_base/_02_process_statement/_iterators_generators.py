# lst = [1, 2, 3, 4]
# it = iter(lst)
# # print(it.__next__())
# # print(it.__next__())
# # print(it.__next__())
# # print(it.__next__())
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))


# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self
#
#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration
#
# myNumbers = MyNumbers()
# myIter = iter(myNumbers)
# for i in myIter:
#     print(i)

# 使用 yield 实现斐波那契数列
import sys


def febonacci(n: int):
    a1, a2 = 0, 1
    # n >= 2
    if n >= 2:
        for i in range(n):
            yield a1
            a1, a2 = a2, a1 + a2
    else:
        yield 0

# for i in febonacci(20):
#     print(i)

f = febonacci(20)
while True:
    try:
        print(next(f))
    except StopIteration:
        sys.exit()