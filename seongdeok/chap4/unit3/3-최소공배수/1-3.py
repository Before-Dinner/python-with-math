a = 8
b = 12
num = a if a < b else b
n = 0
for i in range(num, a*b+1):
    if i % a == 0 and i % b == 0:
        break
print(i)

for i in range(1, 11):
    print(i)
    #i+=1 우와 신기하다!!

a = 120
b = 180
n = 2
LCM = 1

while a > n and b > n:
    if a % n == 0 and b % n == 0:
        LCM = LCM * n
        a /= n
        b /= n 
    else:
        n += 1

print(int(LCM * a * b))

bus1 = 0
bus2 = 0
LCM = 0

bus1 = int(input("bus1: "))
bus2 = int(input("bus2: "))

num = bus1 if bus1 < bus2 else bus2

for i in range(num, bus1 * bus2 + 1):
    if i % bus1 == 0 and i % bus2 == 0:
        LCM = i     
        break
    
print(LCM)