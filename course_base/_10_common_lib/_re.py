import re

p = re.compile(r"^ab")
print(p.findall("abcd\nabfg"))

p = re.compile(r"^ab", flags=re.MULTILINE)
print(p.findall("abcd\nabfg"))

p = re.compile(r".*")
print(p.findall("abc"))

p = re.compile(r"b(?:.+)a(?:.+)e")
m = p.match("babacdefg")
print(m)

p = re.compile(r'blue|white|red')
""" 把每一个从左开始非重叠匹配的字符串用其他字符串替换 """
print(p.sub('colour', 'blue socks and red shoes'))