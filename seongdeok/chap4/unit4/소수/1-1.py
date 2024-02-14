for i in range(2, 30+1):
    for n in range(2, i+1):
        if(i % n == 0):
            break
    if(n == i):
        print(n)

start = 0 
end = 0

start = int(input("start: "))
end = int(input("end: "))

count = 0

for i in range(start, end+1):
    for j in range(2, i+1):
        if(i % j == 0):
            break
    if(i == j):
        count += 1 
            
print(count)