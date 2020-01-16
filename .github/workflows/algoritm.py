import math


a = []
b = []
j = 0
for i in "lorem":
    a.append(i)
    b.append(j)
    j += 1
for i in range(0, len(a)):
    for j in range(i, len(a)):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]
            b[i], b[j] = b[j], b[i]
maxi = len(a)
mini = 0
mid = math.floor((maxi+mini)/2)
k = 0
num = "m"
while True:
    if maxi == mini or (mini + 1 == maxi and a[mid] < num):
        mid = 0
        k = 0
        print("Error")
        break
    elif a[mid] > num:
        k += 1
        maxi = mid
    elif a[mid] < num:
        mini = mid
        k += 1
    else:
        k += 1
        mid = b[mid] + 1
        break
    mid = math.floor((mini+maxi)/2)
print(mid)
print(k)
