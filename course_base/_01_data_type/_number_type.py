########### 整数（int）############
a = int()
print(a) # 默认为0

a = int(3.99)
print(a) # 为 3，取整数部分
b = int(-3.99)
print(b) # 为 -3， 取整数部分

a = int("12")
print(a)
# a = int("12.1") # 报错：浮点型的字符串不可转化

a = int("0101010", base=2) # 二进制转十进制
print(a)

a = int("11", base=8) # 八进制转十进制
print(a)

a = int("0o11", base=8) # 前面加0o说明是八进制, 八进制转十进制
print(a)

a = int("17", base=16) # 基于16进制的"17"转为十进制
print(a)

a = int("0x17", base=16) # 前面加0x说明是十六进制，十六进制转十进制
print(a)

########### 浮点数（float）############
a = 123
b = "123"
c = "123.00"
print(float())
print(float(a))
print(float(b))
print(float(c))

########### 布尔型（bool） ############
print(bool())  # 默认为 False
print(bool(0)) # 0 对应 False
print(bool(1)) # 1 对应 True
print(bool("0")) # "0" 与 数字不同，代表有值，为 True
print(bool(None)) # None 对应 False
print(bool([])) # 空数组 对应 False


########### 复数（complex） ############
print(complex()) # 默认为 0j
print(complex(2,3)) # (2+3j), 第一个参数为实部，第二个参数为虚部
print(complex(2)) # (2+0j), 只传入一个参数时，虚部自动为 0
print(complex("3.2")) # (3.2+0j), 数字与字符串同理
# print(complex("3.2", "2")) # 报错：不同传两个字符串
print(complex("3.2+1j")) # (3.2+1j), 注意 + 号两边不能有空格，否则报错
# print(complex("3.2+1i"))  # 报错：不是任意字段串都可以的
