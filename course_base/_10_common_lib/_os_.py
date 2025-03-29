import os, glob, sys

# ret = os.access("./foo.txt", os.F_OK)
# print(f'F_OK - 返回值 {ret}')

print(os.getcwd())
# print(os.getpid())

# 用于从目录通配符搜索中生成文件列表
print(glob.glob('*.py'))

print(sys.argv)