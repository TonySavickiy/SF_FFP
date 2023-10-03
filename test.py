# Данный кусок кода является примером декорирования для функции с аргументами

def dec(func):
  dic = dict()
  def wrapper(*args, **kwargs):
    nonlocal dic
    if args[0] not in dic:
      x = func(*args,**kwargs)
      dic[args[0]] = x
      print('Значение добавлено в словарь')
      return x
    else:
      x = dic[args[0]]
      print('В этот раз значение взято из словаря')
      return x
  return wrapper

@dec
def sq(a):
  return a*123456789


print(sq(12))
print(sq(12))
print(sq(13))
print(sq(14))