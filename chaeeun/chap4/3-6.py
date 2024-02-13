bus1 = 0
bus2 = 0
LCM = 0

bus1 = int(input("1번 버스의 배차 간격을 입력하세요 : "))
bus2 = int(input("2번 버스의 배차 간격을 입력하세요 : "))

if bus1 > bus2:
  num = bus1
else :
  num = bus2

for n in range(num, bus1 * bus2 + 1):
  if n % bus1 == 0 and n % bus2 == 0 :
    LCM = n
    break

print("두 버스가 동시에 정류장에 도착하는 시간은", LCM, "분 후입니다.")