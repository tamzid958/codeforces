n = int(input())
c = 0
lst = []
for i in range(0, n):
    a = input().split()
    c += int(a[1]) - int(a[0])
    lst.append(c)

print(max(lst))
