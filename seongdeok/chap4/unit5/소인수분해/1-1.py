num = 0
k = 2

num = int(input())
while num != 1:
    if(num % k == 0):
        print(k)
        num //= k
    else:
        k += 1


num = int(input("value: "))
k = 2
while num > 1:
    if num % k == 0:
        num //= k
        print(k)
    else:
        k += 1