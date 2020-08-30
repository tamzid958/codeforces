n, k = input().split()
n = int(n)
k = int(k)
count = 0

if(n % 2 == 0):
    count = int(n/2)
else:
    count = int((n+1)/2)

if(k <= count):
    print(int((k*2)-1))
else:
    print(int(k-count)*2)
