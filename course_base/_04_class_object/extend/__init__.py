


class GrandFather(object):
    def __init__(self):
        print("GrandFather init")

    def speak(self):
        print("I am GrandFather")


class Parent1(GrandFather):
    def __init__(self):
        super().__init__()
        print("Parent1 init")

    def speak(self):
        print("I am Parent1")

class Parent2(GrandFather):
    def __init__(self):
        super().__init__()
        print("Parent2 init")

    def speak(self):
        print("I am Parent2")

class Child1(Parent1, Parent2):
    def __init__(self):
        super().__init__()
        print("Child1 init")

Child1().speak()
# 孙对象的__init__方法调用了两个父对象的__init__方法，但是只调用了一次祖父对象的__init__方法
# 孙对象的speak方法只调用了第一个父对象的speak方法，未调用第二个父对象和祖父对象的speak方法。
print('*'*20)

class Child2(Parent1, GrandFather):
    def __init__(self):
        super().__init__()
        print("Child2 init")

Child2().speak()