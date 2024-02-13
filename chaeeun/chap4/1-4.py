count = 0
total = 0
avr = 0
my_score = 0

count  = int(input("반 전체 인원수를 입력해 주세요 : "))

for n in range(count):
  score = int(input("수학 점수를 입력하세요: "))
  total = total + score

avr = total / count

print("수학 점수의 총점은", total, "점이고 평균 점수는", avr, "점입니다.")

my_score = int(input("자신의 수학 점수를 입력하세요 : "))

if(my_score >= avr) :
  print("당신의 점수는 반 평균 점수 이상입니다.")
else :
  print("당신의 저수는 반 평균 점수 미만입니다.")