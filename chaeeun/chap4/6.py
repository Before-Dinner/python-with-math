# 6-1
x = float(input("절댓값을 구할 실수를 입력하세요 : "))

if x < 0 :
  print(x, "의 절댓값은", -x)
else :
  print(x, "의 절댓값은", x)

# 6-2
x = int(input("절댓값을 구할 수를 입력하세요 : "))
print("%d의 절댓값은 %d" %(x, abs(x)))