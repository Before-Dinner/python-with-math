from operator import xor

print("hello")
print("10진수 13은 2진수", bin(13), "입니다.") #13을 2진수로 변환한다.
print("2진수 1101은 10진수", 0b1101, "입니다.") #1101을 10진수로 변환한다.  
print()

a = 5
b = 2

print("덧셈:", a, "+", b, "=", a + b)
print("곱셈:", a, "*", b, "=", a * b)
print("뺄셈:", a, "-", b, "=", a - b)
print("나눗셈:", a, "/", b, "=", a / b)
print("제곱:", a, "**", b, "=", a ** b)
print("몫:", a, "//", b, "=", a // b)
print("나머지:", a, "%", b, "=", a / b)
print()

A = True
B = False

print("A= ",A)
print("B= ",B)
print("A and B= ",A and B)
print("A or B= ",A or B)
print("Not A= ",not A)
print("A xor B= ",xor(A,B))
print()

Three = 3
Four = 4

print("3 == 4 ->", Three==Four)
print("3 > 4 ->", Three>Four)
print("3 >= 4 ->", Three>=Four)
print("3 < 4 ->", Three<Four)
print("3 <= 4 ->", Three<=Four)
print("3 != 4 ->", Three!=Four)
print()

print("쉬프트 연산")
print(4 << 1)
print(4 << 2)
print(12 >> 1)
print(12 >> 2)
print(5 >> 1)
print()

## 알고리즘 순서도 표현 구조는 크게 3가지로 나눌 수 있다.
## 1. 순차구조 2. 선택구조 3. 반복구조