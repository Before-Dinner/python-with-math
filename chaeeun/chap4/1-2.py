data = [40, 25, 55]
total = 0
avr = 0

print("주어진 데이터는", data, "입니다")

for i in data :
  total = total + i

avr = total / 3
print("총점은", total, "이고, 평균은", avr, "입니다.")