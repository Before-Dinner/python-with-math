a = 120
b = 180
n = 2
GCD = 1

while 1 :
  if n > a or n > b :
    break

  if a % n == 0 and b % n == 0:
    GCD = GCD * n
    a = a / n
    b = b / n
  else :
    n = n + 1

if GCD == 1 :
  print("서로소")
else :
  print("최대공약수 = ", GCD)