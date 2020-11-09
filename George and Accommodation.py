n = int(input())
counter = 0
for i in range(n):
    p, q = input().split()
    p = int(p)
    q = int(q)
    if p+2 <= q:
        counter += 1


print(counter)
