total2 = count = 0
n = int(input())
a = input().split()
a = list(map(int, a))
a.sort()
total = int(sum(a)/2)
a.sort(reverse=True)
for i in range(len(a)):
    total2 += a[i]
    count += 1
    if(total < total2):
        break

print(count)
