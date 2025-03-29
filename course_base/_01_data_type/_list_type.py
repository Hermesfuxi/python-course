########### 列表（List）############
# num_list = [1, -2, 5, -3]
# num_list.sort()
# print(num_list)
#
# num_list.sort(reverse=True)
# print(num_list)
#
# num_list.sort(reverse=False)
# print(num_list)

# li = [1, 2.3, 2+3j, "4", True, False]
# print(li.pop()) # 未给定参数，则删除最后一个元素并返回
# print(li) # 删除元素后的列表
# print(li.pop(2)) # 删除索引2对应的元素
# print(li) # 删除元素后的列表

# list1 = [1, 3, 2, 6, 1, 1, 4]
# list2 = list(reversed(list1))
# print(len(list1) - 1 - list2.index(1))
# print(list1)
#
# var2 = [[123], ]
# print(type(var2))
#
# var6 = (123)
# print(type(var6))

lst = [1,2,3,4,5,6,7,8,9,10]
for (index, item) in enumerate(lst):
    print(index, item)
    item *= 2

print([item*2 for item in lst])