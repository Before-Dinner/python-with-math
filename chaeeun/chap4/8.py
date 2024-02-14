# 8-1
import math

print('16의 제곱근 : ', 16**0.5, ',', -16**0.5)
print('25의 제곱근 : ', math.sqrt(25), ',', -math.sqrt(25))

# 8-2
a = float(input('실수를 입력하세요 : '))

if a > 0 :
  print(a, '제곱근 :', a ** 0.5, ',', -a**0.5)
elif a == 0 :
  print(a, '의 제곱근 : 0')
else :
  print(a, '의 제곱근 : 구할 수 없음')

# 8-3
while 1 :
  a = float(input('실수를 입력하세요 :'))
  print('=>', a, '의 제곱근 ', end = '')
  if a > 0:
    print(a**0.5, ',', -a**0.5)
  elif a == 0 :
    print(0)
  else :
    print("구할 수 없음")
    break