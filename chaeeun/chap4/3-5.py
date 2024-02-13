a = 120
b = 180
n = 2
LCM = 1

while 1 :
  if n > a or n > b :
    break

  if a % n == 0 and b % n == 0 :
    LCM = LCM * n
    a = int(a / n)
    b = int(b / n)
  else :
    n = n + 1

LCM = LCM * a * b
print("최소공배수 =", LCM)