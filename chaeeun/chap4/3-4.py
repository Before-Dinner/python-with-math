a = 8
b = 12

if a > b :
  num = a
else :
  num = b

for n in range(num, a * b + 1):
  if n % a == 0 and n % b == 0 :
    break
  else :
    n = n + 1

print("최소공배수 = ", n)