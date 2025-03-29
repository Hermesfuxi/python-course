# f = open("./test.txt", "w", encoding='utf-8')
# f.write("Python 是一个非常好的语言。\n是的，的确非常好!!\n" * 4)
# f.close()
#
# f = open("./test.txt", "r", encoding='utf-8')
# # str = f.read()
# str = f.readlines()
# f.close()
# print(str)

# with open("./test.txt", "w", encoding='utf-8') as f:
#     f.write("python\n" * 10)
#     print("123456", file=f)
#     print(1,2,3,4,5,6,7, sep='-', end='\n\n', file=f)
#
#
# with open("./test.txt", "r", encoding='utf-8') as file:
#     print(file.read())

# f1 = open('./text1.txt', 'w', encoding='utf-8')
# for i in range(100):
#     f1.write(f"{i}\n")
# f1.close()
#
# f2 = open('./text1.txt', 'r', encoding='utf-8')
# for line in f2:
#     print(line)
# f2.close()
with open('text1.txt', 'rb') as f1, open(f'text-备份.txt', 'wb') as f2:
    while True:
        data = f1.read(1024)
        if not data:
            break
        f2.write(data)