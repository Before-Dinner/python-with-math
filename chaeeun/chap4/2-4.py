# 서로소
for n in range(1, 9) :
  if 8 % n == 0 and 12 % n == 0 :
    GCD = n

if GCD == 1 :
  print("서로소")
else :
  print("최대공약수 =", GCD)