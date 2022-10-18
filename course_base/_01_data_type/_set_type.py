########### 集合（Set）############
print(set())
# a = set("abdefga")
# b = set("abc")
# c = set("aef")
#
# print(c <= a)
# print(a - b)
# print(a | b)
# print(a & b)
# print(a ^ b)
#
# print(a.isdisjoint(b)) # False, 是否不相交
# print(a.issuperset(b)) # False
# print(a.issubset(c)) # False
# print(c.issubset(a)) # True

str1="hermesfuxi"
print(set(str1))
list1=[1,2,3,"4"]
dict1={1:"hermes", 2:"fuxi", ("hermes", "key"): 2}
set1={ 1, 3, ("key", "value")}

print(set1.union(list1))
print(set1.intersection(list1))
print(set1.difference(list1))
print(set1.symmetric_difference(list1))

set1.update(list1)
print(set1)
set1.intersection_update(list1)
print(set1)
set1.difference_update(list1)
print(set1)
set1.symmetric_difference_update(list1)
print(set1)

a = {1, 2, 3, 4}
a.remove(3)
print(a)
# a.remove(3) 从集合中移除元素 elem。 如果 elem 不存在于集合中则会引发 KeyError

a.discard(2)
print(a)
a.discard(2)
print(a)
