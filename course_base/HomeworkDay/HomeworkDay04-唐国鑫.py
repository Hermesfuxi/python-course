"""
1.键盘录入3个整数并接收, 将其最大值打印到控制台上.
		# 思路1: if语句.
"""
num1 = eval(input("请输入第一个整数："))
num2 = eval(input("请输入第二个整数："))
num3 = eval(input("请输入第三个整数："))
print(max(num1, num2, num3))

if num1 > num2:
    if num1 > num3:
        print(num1)
    else:
        print(num3)
else:
    if num2 > num3:
        print(num2)
    else:
        print(num3)


"""
2.循环实现计算 1 ~ 100之间的奇数和, 并将结果打印到控制台上.
# 思路1: while循环.
# 思路2: for循环.
"""

#思路1: while循环.
sum_num = 0
i = 1
while i <= 100:
    if i % 2 != 0:
        sum_num += i
    i += 1
print(f'1 ~ 100之间的奇数和为{sum_num}')

# 思路2: for循环.
sum_num = 0
for i in range(1,101):
    if i%2!=0:
        sum_num += i
print(f'1 ~ 100之间的奇数和为{sum_num}')

"""
3. 猜数字游戏, 随机生成1个 1 ~ 100之间的数字,
   让用户来猜, 并进行对应的提示. 
"""
import random
random_num = random.randint(1,100)
while True:
    guess_num = eval(input("请输入一个1~100之间的数字："))
    if guess_num == random_num:
        print("恭喜你猜对了！")
        break
    elif guess_num > random_num:
        print("猜大了！")
    else:
        print("猜小了！")


"""
4. 模拟登陆, 只给3次机会, 登录成功则程序结束, 登陆失败则提示剩余登陆次数.
"""
username = "admin"
password = "123456"
for i in range(3):
    username_input = input("请输入用户名：")
    password_input = input("请输入密码：")
    if username_input == username and password_input == password:
        print("登录成功！")
        break
    else:
        print(f"登录失败, 剩余登录次数{2-i}次！")


"""
5. 打印水仙花数, 将所有的水仙花数 及 水仙花数的总个数 打印到控制台上.
		水仙花数解释:
			1.水仙花数是1个三位数.
			2.它的各个位数的立方和相加等于它本身.
			  例如: 153 = 1 * 1 * 1 + 5 * 5 * 5 + 3 * 3 * 3  它就是1个水仙花数.
		提示:
			水仙花数一共有4个
"""
count = 0
for i in range(100,1000):
    if i == (i//100) ** 3 + (i//10%10) ** 3 + (i%10) ** 3:
        print(i)
        count += 1
print(f'水仙花数的总个数为{count}')