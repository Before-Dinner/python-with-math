a = 9
b = 14

if a < b :
  num = a
else :
  num = b

for n in range(1, num+1) :
  if a % n == 0 and b % n == 0:
    GCD = n

if GCD == 1:
  print("서로소")
else :
  print("최대공약수 =", GCD)