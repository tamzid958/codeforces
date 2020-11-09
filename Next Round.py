n, k = input().split()
n = int(n)
k = int(k)
counter = 0
ele = input().split()

for i in range(0, n):
    if int(ele[i]) >= int(ele[k-1]) and int(ele[i]) != 0:
        counter = counter + 1

print(counter)
