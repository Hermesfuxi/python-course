# import keyword
# print(keyword.kwlist)
# print(keyword.iskeyword('if'))

# print(help(zip))
# print("="*20)
#
# import math
# print(help(math))
# print("="*20)
# print(dir(math))

#
# a, b, c, d = 1, 1.5, True, 4+3j
# print(a, b, c, d)
# print(type(a), type(b), type(c), type(d))

# a = 1
# flag = isinstance(a, int)
# print(flag)

# import copy
# a = b = [333, ("1", "2"), [555, 666], {0: {}}]
# c = a.copy()  # 浅拷贝
# d = copy.deepcopy(b) # 深拷贝
#
# print(id(a) == id(b))
# print(id(a) == id(c))
# print(id(a) == id(d))
# print(id(a[0]) == id(c[0]))
# print(id(a[0]) == id(d[0]))
# print(id(a[1]) == id(c[1]))
# print(id(a[1]) == id(d[1]))
# print(id(a[1][-1]) == id(d[1][-1]))
# print(id(a[2][-1]) == id(d[2][-1]))
# print(id(a[-1][0]) == id(d[-1][0]))