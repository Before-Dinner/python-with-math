a = 14
b = 9
GCD = 0
num = a if a < b else b 

for i in range(1, num+1):
    GCD = i if a % i == 0 and b % i == 0 else GCD

print("coprime") if GCD == 1 else print(GCD)