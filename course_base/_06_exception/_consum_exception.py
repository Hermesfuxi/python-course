# 自定义异常类: 写一个只接收整数的加法计算器，当输入的不是整数时引发异常

# 先定义一个模板的基类，再派生其他类，这样会显得清晰明了，不至于与其他类混淆
class CalcException(Exception):
  pass

class NumException(CalcException):
  # 输入非整数会引发此异常
  def __init__(self, num1, num2):
    self.num1 = num1
    self.num2 = num2

  ''' 返回异常的描述 '''
  def __str__(self):
    return f'{self.num1} or {self.num2} 中有非整数，这里只接收整数'


def calcSumInt(num1, num2):
  try:
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
      raise NumException(num1, num2)
  except Exception as e:
    print(e)
    return 0
  else:
    return num1 + num2

print(calcSumInt(1.1, 2.1))
print(calcSumInt(1.1, '2.1'))