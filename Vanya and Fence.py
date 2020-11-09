n, h = input().split()
n = int(n)
h = int(h)

a = list(map(int, input().split()))
counter = 0
for i in range(n):
    if(a[i] <= h):
        counter += 1

    else:
        if(a[i] / 2 <= h):
            counter += 2

print(counter)
