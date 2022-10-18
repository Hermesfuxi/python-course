########### 字符串（String）############
# String 是不可变的，它是序列
# print(str()) # 返回空字符串
# print(str(123456789))

########### 一、引号 ############
# s1 = 'hello world'
# s2 = "hello world"
# print(s1)
# print(s2)
# print(s1 == s2) # True, 单引号或双引号在 python 中同义

'''faergnsrldgkjbnleosnrgslkdgjnsg
rbghd'''
# s1 = '''faergnsrldgkjbnleosnrgslkdgjnsg
# rbghd'''
# print(s1) # 结果如其所示，会自动分行, 相当于注释

# 如何输出引号
# print("\"\"") # 使用转义
# print("''") # 单引号或双引号 换着用
# print('""')
# print('""""')
# print('''""''')

########### 二、格式化 ############
########### 1、格式化 ： % 类型
# print("它说它叫%s, 今年%d岁, 每天睡%f小时!"%("小狗", 10, 1.5))

# # repr() 方法可以将读取到的格式字符，比如换行符、制表符，转化为其相应的转义字符。
# s="物品\t单价\t数量\n包子\t1\t2"
# print(s)
# print(repr(s))
# # 可简化为如下：
# print("a;ergtr;\nAWRHAETRS")
# print(r"a;ergtr;\nAWRHAETRS")
# print(R"a;ergtr;\nAWRHAETRS")

# import datetime
# d = datetime.date.today()
# print(type(d)) # <class 'datetime.date'>
# print("%s" % d) # 2022-07-21
# print("%r" % d) # datetime.date(2022, 7, 21)

# print("%c,%c,%c,%c" % (65, 90, 97, 122))
# print("%c,%c,%c,%c" % ("A", "Z", "a", "z"))

# 格式化 - 进制转换
# print("%o" % 13) # 结果为 15  - 8进制
# print("%#o" % 13) # 0o15  -  8进制，在八进制数前面显示 '0o'
# print("%x" % 13) #  d  -  16进制
# print("%#x" % 13) # 0xd  -  16进制， 在十六进制前面显示 '0x'
# print("%X" % 13) #  D  -  16进制
# print("%#X" % 13) # 0XD  -  16进制，在十六进制前面显示 '0x'

# print("123用科学计数法表示为%e" % 123) # 1.230000e+02
# print("123用科学计数法表示为%E" % 123) # 1.230000E+02

PI = 3.141592653
# print("PI1 = %10.3f" % PI)
# print("PI1 = %010.3f" % PI)
# print("PI1 = %.3f" % PI)
# print("PI1 = %.f" % PI)
# print("PI1 = %10f" % PI)
# print("PI1 = %010f" % PI)
# print("PI1 = %f" % PI)  # %f默认精确到小数点后6位，并四舍五入
# print("PI1 = %-f" % PI) # 左对齐, 默认为右对齐
# print("PI1 = %+f" % PI) # 在正数前面显示正号
#
# # '*'号：定义最小显示宽度或者小数位数
# print("PI1 = %.*f" % (3, PI))
# print("PI1 = %*f" % (3, PI))

########### 格式化 %g/%G
# print("%g" % 1.23456789)  # 保留6位有效数字, 并四舍五入
# print("%g" % 12345.6789)
# print("%g" % 123456.789)
# print("%g" % 1234567.89)  # 保留6位有效数字, 整数部分大于6位则用科学计数法表示
# print("%g" % 9.87654321)  # 保留6位有效数字, 并四舍五入
#
# print("%G" % 1.23456789)
# print("%G" % 12345.6789)
# print("%G" % 123456.789)
# print("%G" % 1234567.89)

########### 2、格式化 format 函数 ############
# {}是占位符, 当里面为空时, 默认从左往右选择数据
# a = "它说它叫{}, 它今年{}岁, 它宝宝{}个月了!".format("旺财", 2, 3)
# print(a)
# # 占位符可以填入右边数据的顺序索引来填入对应数据
# a = "它说它叫{1}, 它今年{0}岁, 它宝宝{2}个月了!".format(2, "旺财", 3)
# print(a)
# # 还可以通过关键字来赋值，可复用
# c = "它说它叫{name}, 它今年{age01}岁, 它宝宝{age02}个月了!它已经存在{age01}年".format(name="旺财", age01=2, age02=3)
# print(c)

"""  format 函数
:后面可以附带填充的字符，默认为空格
^、<、> 分别表示居中、左对齐、右对齐，后面附带宽度限定值
使用b、d、o、x 分别输出二进制、十进制、八进制、十六进制数
字
使用逗号（,）输出金额的千分位分隔符 
"""
# print("{:>8}".format("1"))
# print("{:0>8}".format("1"))
# print("{:0<8}".format("1"))
# print("{:a<8}".format("1"))
# print("{:8.2f}".format(PI))
# print("{:0<8.2f}".format(PI))

# num = 100
# print("{:b}".format(100)) # 二进制
# print("{:d}".format(100))
# print("{:o}".format(100)) # 八进制
# print("{:x}".format(100)) # 十六进制
# print("{:,}".format(1234567890))
#
# print(f"{num:b}")
# print(f"{num:d}")
# print(f"{num:o}")
# print(f"{num:x}")
# print(f"{123456789:,}")
#
# print(f"{PI:>10.2f}")
# print(f"{PI:0>10.2f}")
# print(f"+{PI:0<10.2f}")

# a = "\\" # 单个反斜杠
# s1 = "hello world"
# print(a.join(s1))

########### 三、常用函数 ############
# str1 = ' \thello wrold h \n'
# print(str1.strip())  # 默认移除空白符（空格、换行符、制表符等）
# print(str1.strip().strip("h"))
# print(str1.strip().rstrip("h"))
# print(str1.strip().lstrip("h"))


## 对齐：居中、居左、居右
# str1 = "hell"
# print(str1.center(11))
# print(str1.center(3, "F"))
# # 当左右填充不平衡时，原字符串长度为奇数时，左边填充更少，原字符串长度为偶数时，左边填充更多
# print(str1.center(5, "F"))  #
# print(str1.center(7, "F"))  #
# str2 = "hello"
# print(str2.center(6, "F"))
# print(str2.center(8, "F"))
#
# str1 = "hello "
# print(str1.ljust(11, "F"))
# print(str1.ljust(3, "F"))
# print(str1.rjust(11, "F"))
# print(str1.rjust(3, "F"))

# 拆分
str1 = "hello world"
print(str1.partition("l"))
print(str1.partition("ll"))
print(str1.partition("hd"))

print(str1.rpartition("l"))
print(str1.rpartition("ll"))
print(str1.rpartition("hd"))

#
str1 = "hello world"
#
# print(str1.startswith("h"))
# print(str1.startswith("he"))
# print(str1.startswith(" w"))
# print(str1.startswith(" w", 5, 8))
# print(str1.startswith((" w", "h")))
#
# print(str1.endswith("d"))
# print(str1.endswith("ld"))
# print(str1.endswith("lo"))
# print(str1.endswith("lo", 1, 5))
# print(str1.endswith(("d", "lo")))

# print(str1.isalnum())  # 如果字符串中的所有字符都是字母、文字或数字，则返回 True，否则为 False
# print(str1.replace(" ", "").isalnum())
# print(str1.isalpha())  # 如果字符串中的所有字符都是字母、文字，则返回True，否则为 False
# print("123456789".isdigit())  # 如果字符串中的所有字符都是数字，则返回True，否则为 False
# print(str1.isdigit())
# print(str1.isspace()) # 如果字符串中只有空白符（空格、换行符、制表符等），则返回 True，否则为 False

# print("123456789".isascii())
# print("abcdefghi".isascii())
# print("123456789".isdecimal())
# print("abcdefghi".isdecimal())

# print("123456789".isidentifier())  # 如果字符串是Python中的有效标识符，则isidentifier()方法返回True。如果不是，则返回False。
# print("abcdefghi".isidentifier())
# print(str1.islower())
# print(str1.isupper())

# print(str1.isnumeric())
# print("123456789".isnumeric())

# print(str1.isprintable())
print("str1".istitle())
print("Str1".istitle())
print("Str1 print".istitle())
print("Str1 Print".istitle())


a = "hello world"
print(a.capitalize()) # Hello world
print(a.title())  # Hello World
print(a.title().swapcase())  # 颠倒交换， hELLO wORLD