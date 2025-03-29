
'''
1.定义一个字符串，如str1 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"。
编写一个程序，使用随机数从字符串中抽取4个字符，用于生成验证码。
'''
import random
def verification_code_v1(str_code, num):
    if num > len(str_code):
        print("输入的数字过大")
        return
    if num < 0:
        print("输入的数字过小")
        return
    if num == 0:
        return ""
    return str_code[random.randint(0, len(str_code) - 1)] + verification_code_v1(str_code, num - 1)

def verification_code_v2(str_code, num):
    list1 = []
    for i in range(num):
        list1.append(str_code[random.randint(0, len(str1) - 1)])
    return "".join(list1)

def verification_code_v3(str_code, num):
    return "".join(random.choices(str_code, k=num))

str1 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(verification_code_v1(str1, 4))
print(verification_code_v2(str1, 4))
print(verification_code_v3(str1, 4))


'''
2.已知列表 list1 = [11, 22, 33, 22, 11, 55], 请对其进行去重, 并将去重后的结果打印到控制台上.
'''
list1 = [11, 22, 33, 22, 11, 55]

print(list(set(list1)))

print(list(dict.fromkeys(list1,1).keys()))


'''
3.键盘录入1个字符串并接收, 计算其中每个字符出现的次数, 并将结果打印到控制台上.
  例如:
    录入: abcbcAABBB11133
    输出: a(1)b(2)c(2)A(2)B(3)1(3)3(2)	格式一致即可, 不要求顺序.
'''

def count_str_v1(input_str):
    output_str = ""
    for i in sorted(set(input_str)):
        output_str += f"{i}({input_str.count(i)})"
    return output_str

def count_str_v2(input_str):
    output_dict = {}
    for i in input_str:
        if i not in output_dict:
            output_dict[i] = input_str.count(i)

    output_str = ""
    for i in sorted(output_dict):
        output_str += f"{i}({output_dict[i]})"
    return output_str

input_str = input("请录入字符串: ")
print(count_str_v1(input_str))
print(count_str_v2(input_str))

'''
4给定一个集合numbers，集合中包含1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15元素，
求该集合中所有奇数的和是多少.
'''
numbers = range(1, 16)
print(sum(i for i in numbers if i % 2 != 0))
print(sum(filter(lambda x: x % 2 != 0, numbers)))
print(sum(numbers[::2]))