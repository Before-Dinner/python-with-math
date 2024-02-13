chocolate = int(input("chocolate:" ))
candy = int(input("candy:" ))

GCD = 0
candy *= 12
chocolate *= 15
num = chocolate if chocolate < candy else candy

for i in range(1, num+1):
    GCD = i if candy % i == 0 and chocolate % i ==0 else GCD

print(GCD)
print(int(candy/GCD), int(chocolate/GCD)) 