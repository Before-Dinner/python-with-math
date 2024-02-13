count = 0
start = 0
end = 0
start = int(input("시작 값을 입력하세요(단, 2이상) :"))
end = int(input("종료 값을 입력하세요 : "))

for n in range(start, end + 1):
  for m in range(2, n + 1):
    if(n % m) == 0 :
      if m == n :
        count = count + 1
      break

print(start, "에서", end, "사이에 있는 소수의 개수 :", count)