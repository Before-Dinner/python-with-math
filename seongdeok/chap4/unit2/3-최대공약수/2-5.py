a = 120
b = 180
n = 2
GCD = 1

while a > n and b > n:
    if a % n == 0 and b % n == 0:
        GCD = GCD * n
        a /= n
        b /= n
    else:
        n += 1

print("coprime") if GCD == 1 else print(GCD)