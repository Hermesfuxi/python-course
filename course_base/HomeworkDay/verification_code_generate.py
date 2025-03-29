# 定义一个字符串，如str1 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"。编写一个程序，使用随机数从字符串中抽取4个字符，用于生成验证码。 [上传文件题]
import random

def verification_code(str_code, num):
    list1 = []
    for i in range(num):
        list1.append(str_code[random.randint(0, len(str_code) - 1)])
    return "".join(list1)

print(verification_code('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ', 4))
