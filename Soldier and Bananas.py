k, n, w = input().split()
k = int(k)
n = int(n)
w = int(w)
x = 0
for i in range(1, w+1):
    x += i*k

x = x - n
if(x >= 0):
    print(x)
else:
    print(0)
