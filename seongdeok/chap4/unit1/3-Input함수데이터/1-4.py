total = 0
data = 0
count = 0

count = int(input("total count: "))

for i in range(count):
    data = int(input("math score: "))
    total += data
print(total)
avr = total / count
print(avr)

myScore = int(input("my math score: "))
if myScore >= avr:
    print("you win")
else:
    print("you lose")