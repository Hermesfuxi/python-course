# import keyword
#
# print(keyword.kwlist)
#
# a, b, c, d = 1, 1.5, True, 4+3j
# print(a, b, c, d)
# print(type(a), type(b), type(c), type(d))
#
# flag = isinstance(a, int)
# print(flag)

# print(help(zip))

# info = {"经理": ("曹操", "刘备", "孙权" , "赵云"), "技术员": ("曹操", "孙权", "张飞", "关羽")}
# set_1 = set(info["经理"])
# set_2 = set(info["技术员"])
# print(f"既是经理也是技术员的有:{set_1 & set_2}")
# print(f"是经理，但不是技术员的有:{set_1 - set_2}")
# print(f"经理和技术员共有{len(set_1 | set_2)}人")

# import copy
# a = b = [333, ("1", "2"), [555, 666], {0: {}}]
# c = a.copy()
# d = copy.deepcopy(b)
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
