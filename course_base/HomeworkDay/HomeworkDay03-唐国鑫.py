# 基础题:
# 	1.定义两个变量, title='大白菜'，price=3.5，按照如下格式进行输出：今天蔬菜特价了，大白菜只要3.5元/斤。
title = '大白菜'
price = 3.5
print(f'今天蔬菜特价了，{title}只要{price}元/斤。')

# 	2.定义两个变量, name='孙悟空'，mobile='18878569090'，按照以下格式进行输出"姓名：孙悟空，联系方式：18878569090"
name = '孙悟空'
mobile = '18878569090'
print(f'姓名：{name}，联系方式：{mobile}')

# 	3.AA制餐厅
# 		需求: 假设你是一位很棒的AA制餐厅的服务员，你的任务是计算每位顾客的应付金额。
# 		输入顾客人数，并赋值给total_friends变量。
# 		输入总账单数值，并赋值配给 total_bill 变量。
# 		在账单费用上加上20%的税，并计算最终账单总额均摊给顾客金额，然后打印
flag1 = True
while flag1:
    try:
        total_friends = int(input("请输入顾客人数(正整数):"))
        if total_friends <= 0:
            raise ValueError("顾客人数必须是正整数")

        total_bill = float(input("请输入总账单数值(￥):"))
        if total_bill < 0:
            raise ValueError("总账单数值(￥)必须是非负数")

        total_amount_per_person = (total_bill * 1.2) / total_friends
        print(f'账单均摊，每位顾客的应付金额：{total_amount_per_person:.2f}(￥)')

        flag1 = False

    except ValueError as e:
        print(f"输入错误: {e}")
    except Exception as e:
        print(f"发生了一个错误: {e}")



# 进阶题:
# 	1.键盘输入身高，体重，求BMI = 体重(kg)/身高(m)的平方
flag2 = True
while flag2:
    try:
        height = float(input("请输入您的身高(m):"))
        if height <= 0 or height >= 3:
            raise ValueError("正常的身高数据为0~3m之间，注意单位")

        weight = float(input("请输入您的体重(kg):"))
        if height <= 0 or weight >= 500:
            raise ValueError("正常的体重数据在0~500kg之间，注意单位")

        BMI = weight / (height * height)
        print(f'您的 BMI指标(=体重(kg)/身高(m)的平方)为：{BMI:.2f}')

        flag2 = False

    except ValueError as e:
        print(f"输入错误: {e}")
    except Exception as e:
        print(f"发生了一个错误: {e}")
