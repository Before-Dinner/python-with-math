# 5-1
num = 0
k = 2
num = int(input("소인수분해 할 자연수를 입력하세요 : "))

while 1 :
  if (num % k) == 0 :
    print(k)
    num = num // k
    if num == 1:
      break
  else :
    k = k + 1

# 5-2
num = 0
k = 2

num = int(input("소인수분해 할 자연수를 입력하세요 : "))

print(num,"=",end='')
while 1 :
  if (num % k) == 0 :
    print(k, end = '')
    num = num // k
    if num == 1 :
      break
    else :
      print("x", end = '')
  else:
    k = k + 1