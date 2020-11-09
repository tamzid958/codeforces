n, l = map(int, input().split())
m = 0
a = sorted(list(map(int, input().split())))

for i in range(n-1):
    if(a[i+1] - a[i] > m):
        m = a[i+1] - a[i]

x = a[0]
y = m/2
ans = max(x, y)
z = l - a[n-1]
ans = max(z, ans)
print(ans)
