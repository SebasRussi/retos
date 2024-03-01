def e1(n):
  if(n == 0):
    return 0
  digit = n % 10
  if(digit != 0 and digit % 4 == 0):
    return 1 + e1(n//10)
  return 0 + e1(n//10)
e1(45697)
print(e1(4697))