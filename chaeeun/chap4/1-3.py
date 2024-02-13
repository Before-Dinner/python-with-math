data = 0
total = 0
avr = 0

for i in range(3) :
  data = int(input("정수를 입력하세요 : "))
  total = total + data

avr = total / 3
print("총점은", total, "이고, 평균은", avr, "입니다.")