import numpy as np
from typing import Iterable

# np_arr1 = np.array((1, 2, 3, 4))
# print(np_arr1, type(np_arr1))
# np_arr2 = np.array([1, 2, 3, 4])
# print(np_arr2, type(np_arr2))
# np_arr3 = np.array({1: 3, 2:6, 3:9, 4:12})
# print(np_arr3, type(np_arr3))
# np_arr3 = np.array({1, 2, 3, 4})
# print(np_arr3, type(np_arr3))

# np_arr3 = np.array([[1, 2], [3, 4]])
# print(np_arr3)
#
# np_arr4 = np.array([[1, 2], [3, 4]], ndmin=3, dtype=int)
# print(np_arr4)
# np_arr4 = np.array([[1, 2], [3, 4]], ndmin=3, dtype=float)
# print(np_arr4)
# np_arr4 = np.array([[1, 2], [3, 4]], ndmin=3, dtype=complex)
# print(np_arr4)
# np_arr4 = np.array([[1, 2], [3, 4]], ndmin=3, dtype=np.int32)
# print(np_arr4)
# np_arr4 = np.array([[1, 2], [3, 4]], ndmin=3, dtype=np.complex_)
# print(np_arr4)
#
# dt = np.dtype(np.int32)
# print(dt)
# dt = np.dtype('i4')
# print(dt)

# dt = np.dtype((str, int))
# dt = np.dtype([('age',np.int8)])
# print(dt) # 结果为 <U1  :  '<' 表示字节顺序，小端（最小有效字节存储在最小地址中）, U表示Unicode，数据类型, 1表示元素位长，数据大小

# 将数据类型应用于 ndarray 对象, 类型字段名可以用于存取实际 列
# dt = np.dtype([('aawghreage', np.int8)])
# np_arr = np.array([(1,), (2,), (3,)], dtype=dt)
# print(np_arr)
# print(np_arr['aawghreage'])

# 定义一个结构化数据类型 student，包含字符串字段 name，整数字段 age，及浮点字段 marks，并将这个 dtype 应用到 ndarray 对象。
# student = np.dtype([('name', 'S10'), ('age', int), ('marks', float)])
# np_arr = np.array([
#             ('hermesfuxi', 29, 62.52),
#             ('aerh', 24, 51.2),
#             ('john', 32, 96.52),
#         ],
#         dtype=student)
# print(np_arr)

# np_arr = np.arange(24)
# print(np_arr, np_arr.shape)
# print(np_arr.ndim, np_arr.shape, np_arr.dtype, np_arr.itemsize, np_arr.real, np_arr.imag, np_arr.data)
# # print(dir(np_arr.flags))
# print(np_arr.flags.c_contiguous)
#
# np_arr2 = np_arr.reshape((3, 2, 4))
# print(np_arr2)
# print(type(np_arr2))
#
# a = np.array([[1, 2, 3], [4, 5, 6]])
# a.shape = (3, 2)
# print(a)
# print(a.ndim)

# np_arr = np.empty((3, 3, 2), dtype=int)
# print(np_arr)

# a = np.zeros((5,2), dtype=int)
# print(a)
# a = np.zeros_like((5,2), dtype=int)
# print(a)
# a = np.ones((5,2), dtype=int)
# print(a)
# a = np.ones_like((5,2,1), dtype=int)
# print(a)

# print(np.asarray([100, 2, 3]))
# print(np.asarray((1, 200, 3)))

s = b'hello world'
# a = np.frombuffer(s, dtype='S1', offset=2)
# print(a)
#
# d = np.fromiter('hello world', dtype='S12')
# print(d)
#
# x = np.arange(10, 20, 2)
# print(x)
#
# print(np.linspace(1, 10, 10, endpoint=False))
# print(np.linspace(1, 10, 10, endpoint=True))
# print(np.logspace(1, 4, 5, endpoint=True, dtype=np.int64))
# print(np.logspace(0, 4, 4, endpoint=False, dtype=np.int64))
# print(np.logspace(0, 10, 11, endpoint=True, dtype=np.int64, base=2))
#
# y = np.empty((2, 3, 4), dtype=int)
# print(type(y.shape))
# print(y)
# print('============================')
# print(y[..., 1])
# print('============================')
# print(y[0, ..., 3])
#
# np_arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(np_arr)
# print(np_arr[[0, 1, -1], [0, 1, -1]])
# print(np_arr[np_arr>5])
#
# x = np.array([np.nan, np.nan, 1, 3])
# print(x[~np.isnan(x)])
#
# a = np.array([1,  2+6j,  5,  3.5+5j])
# print(a[np.iscomplex(a)])

# x = np.arange(32).reshape((8, 4))
# print(x)
# print(x[1])  # 一维数组 [4 5 6 7]
# print(x[[1]])  # 二维数组 [[4 5 6 7]]
# print(x[[1], [2]])  # 二维数组 [6]
# # print(x[[[1]]])  # 报错，但显示二维数组 [[4 5 6 7]]
# print(x[[[1]], [[2]]])  # 二维数组 [[6]]

# print(x[[1, 5, 7, 2]])  # 行索引选中
# print(x[..., [0, 3, 1, 2]]) # 列索引选中
# print(x[[1, 5, 7, 2], [0, 3, 1, 2]])  # 行列索引定位，交叉选中
# 以下二者结果相同：多个索引数组，连续多个索引定位
# print(x[[1, 5, 7, 2]][..., [0, 3, 1, 2]])
# print(x[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])]) #

# NumPy 广播(Broadcast)
# np_arr1 = np.array([1, 2, 3, 4])
# np_arr2 = np_arr1 * 100
# if np_arr1.shape == np_arr2.shape:
#     print(np_arr1 * np_arr2)

# a = np.transpose(np.arange(4) * 10 * np.ones((4, 4), dtype=int))[..., :-1]
# print(a)
# b = np.array([0, 1, 2])
# print(a + b)
# bb = np.tile(b, (4, 1))  # 重复 b 的各个维度
# print(bb)
# print(a + bb)

# a = np.arange(12).reshape((3, 4))
# print(a)
# print(a.T)
# for i in np.nditer(a):
#     print(i, end=',')
# print()
# for i in np.nditer(a.T):
#     print(i, end=',')
# print()
#
# for i in np.nditer(a, order='F'):
#     print(i, end=',')
# print()
# for i in np.nditer(a.T, order='F'):
#     print(i, end=',')
# print()
# for i in np.nditer(a, order='C'):
#     print(i, end=',')
# print()
# for i in np.nditer(a.T, order='C'):
#     print(i, end=',')
# print()
#
# for i in np.nditer(a, op_flags=['readwrite']):
#     i *= 2
# print(a)
#
# f = np.nditer(a, flags=['f_index'])
# while not f.finished:
#     print(f'{f.index}->{f[0]}', end=', ')
#     # it.iternext()表示进入下一次迭代，如果不加这一句的话，输出的结果就一直都是 0 且不间断地输出
#     f.iternext()
# print()
#
# f = np.nditer(a, flags=['c_index'])
# while not f.finished:
#     print(f'{f.index}->{f[0]}', end=', ')
#     # it.iternext()表示进入下一次迭代，如果不加这一句的话，输出的结果就一直都是 0 且不间断地输出
#     f.iternext()
# print()
#
# f = np.nditer(a, flags=['multi_index'])
# while not f.finished:
#     print(f'{f.multi_index}->{f[0]}', end=', ')
#     # it.iternext()表示进入下一次迭代，如果不加这一句的话，输出的结果就一直都是 0 且不间断地输出
#     f.iternext()
# print()
#
# f = np.nditer(a, flags=['external_loop'], order='F')
# while not f.finished:
#     print(f[0])
#     # it.iternext()表示进入下一次迭代，如果不加这一句的话，输出的结果就一直都是 0 且不间断地输出
#     f.iternext()
# print()

# a = np.arange(0, 60, 5)
# a = a.reshape(3, 4)
# b = np.array([1, 2, 3, 4], dtype=int)
# print([a, b])
# for i1, i2 in np.nditer([a, b]):
#     print(f'{i1}:{i2}')

# a = np.arange(1, 28).reshape((3, 3, 3))
# print(a)
# print('=================')
# b = np.rollaxis(a, 2, 0)
# print(b)

# x = np.array([[1], [2], [3]])
# y = np.array([4, 5, 6])
#
# # 对 y 广播 x
# b = np.broadcast(x, y)
# print(b.shape)
#
# a = np.arange(4).reshape(1, 4)
# print(f'原数组为：\n{a}')
# a1 = np.broadcast_to(a, (4, 4))
# print(f'广播之后，数组变为:\n{a1}')
#
# *c, = b.iters
# for item1 in c:
#     for item2 in item1:
#         print(item2, end=',')
#     print()
#
# d = np.empty(b.shape)
# print(d.shape)
# print(d)
# d.flat = [u + v for (u, v) in b]
# print(d)

# x = np.arange(4).reshape(2, 2)
# print(f'数组为：\n{x}')
# y = np.expand_dims(x, axis=0)

# a, b = 13, 17
# print(bin(a), bin(b))

# print(np.char.add(['hello'], ['world']))
# print(np.char.multiply('hello ', 4))
# print(np.char.center('hello', 20, '*'))
# print(np.char.capitalize('hello'))

# a = np.array([0, 30, 45, 60, 90])
# a_sin = np.sin(a * np.pi / 180)
# print(a_sin)
# print(np.arcsin(a_sin))

# a_cos = np.cos(a * np.pi / 180)
# print(a_cos)

# a = np.array([0,30,45,60,90])
# print ('含有正弦值的数组：')
# sin = np.sin(a*np.pi/180)
# print (sin)
# print ('\n')
# print ('计算角度的反正弦，返回值以弧度为单位：')
# inv = np.arcsin(sin)
# print (inv)

# a = np.array([[3, 7, 5], [8, 4, 3], [2, 4, 9]])
# print(np.amin(a))
# print(np.amin(a, 0))
# print(np.amin(a, 1))
# print(np.amax(a))
# print(np.amax(a, 0))
# print(np.amax(a, 1))
#
# a = np.random.randint(2,40,size=(2,3,4))
# print(a)
# print("="*90)
# # 0为最外层对比，即shape 第一位
# print(np.amin(a,0))
#
# print("="*90)
#
# # 1为次外层对比，即shape 第二位
# print(np.amin(a,1))
# print("="*90)
#
# # 2为再次外层对比，即shape第三位
# print(np.amin(a,2))
# print("="*90)
#
# # 先0后2，逐次对比
# print(np.amin(a,(0, 2)))
#
# print(np.ptp(a))
# print(np.ptp(a, axis=1))
# print(np.ptp(a, axis=0))

# print(np.std([1, 2, 3, 4]))
# print(np.var([1, 2, 3, 4]))
#
# a = np.array([[3, 7], [9, 1]])
# print(np.sort(a)[..., ::-1])

a = np.array([3, 4, 2, 1])
print(np.partition(a, 3))

x = np.arange(9.).reshape(3, 3)
print(np.where(x > 5))
print(x[np.where(x > 5)])
print(x[x > 5])


# x = np.arange(81).reshape((3, 3, 3, 3)) + 1
# print(x)
# np.save('81式.npy', x)
# y = np.load('81式.npy')
# print(y)
