def test(*args):
    print(args)
    print(*args)

print(test(1, 2, 3))