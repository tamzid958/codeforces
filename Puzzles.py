x, y = map(int, input().split())
l = sorted(list(map(int, input().split())))

m = 1000
for i in range(y-x+1):
    d = l[i+x-1] - l[i]
    if d < m:
        m = d
print(m)
