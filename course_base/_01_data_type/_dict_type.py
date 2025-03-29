########### 字典（Dictionary） ############
print(dict())
var22 = {"age": 18, "蓝瘦": "香菇"}
print(type(var22))
#
# dic1 = dict((("a", "b"), ("c", "d")))
# print(dic1)
#
# dic1 = dict([("a", "b"), ("c", "d")])
# print(dic1)
#
# dic1 = dict({("a", "b"), ("c", "d")})
# print(dic1)
#
dic1 = dict(zip(["姓名", "年龄"], ["张三", 28]))
print(dic1)
print(list(zip(["姓名", "年龄"], ["张三", 28])))
#
# dic1 = dict.fromkeys(("name", "age", "sex"))
# print(dic1)
# dic2 = dict.fromkeys(("name", "age", "sex"), "Idon't know!")
# print(dic2)

dic = {"身高":175, "体重":65}
value = dic.get("体重")
print(value) # 65
value = dic["体重"]
print(value) # 65
value = dic.get("体", "KeyError000")
print(value) # 返回一个字符串："KeyError"
# value = dic["体"]
# print(value)

dic3= {'数学': 12, '语文': 95, '英语': 98, '物理': 32, '化学': 65, '生物': 69}
print(sum(dic3.values()))