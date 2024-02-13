GCD = 0
for i in range(1, 13):
    if 8 % i == 0 and 12 % i == 0:
        GCD = i
    
if GCD == 1:
    print("coprime")
else:
    print(GCD) 