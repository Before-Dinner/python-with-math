candy = 0
chocolate = 0
n_candy = 0
n_chocolate = 0
GCD = 0

candy = int(input("사탕 박스의 수를 입력: "))
chocolate = int(input("초콜릿 박스의 수를 입력: "))

n_candy = candy * 12
n_chocolate = chocolate * 15

if n_candy < n_chocolate :
  num = n_candy
else :
  num = n_chocolate

for n in range(1, num+1) :
  if n_candy % n == 0 and n_chocolate % n == 0 :
    GCD = n

print("봉지는", GCD, "개가 필요하고")
print("사탕", int(n_candy/GCD), "개와 초콜릿", int(n_chocolate/GCD), "개를 넣습니다")