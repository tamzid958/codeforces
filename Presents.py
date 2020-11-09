n = int(input())
a = list(map(int, input().split()))

for i in range(n+1):
    for j in range(n):
        if(a[j] == i):
            print(j+1, end=" ")
