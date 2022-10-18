# f = open("./test.txt", "w", encoding='utf-8')
# f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n" * 4)
# f.close()
#
# f = open("./test.txt", "r", encoding='utf-8')
# # str = f.read()
# str = f.readlines()
# f.close()
# print(str)

with open("./test.txt", "w", encoding='utf-8') as file:
    file.write("python\n" * 10)

with open("./test.txt", "r", encoding='utf-8') as file:
    print(file.read())