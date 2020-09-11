n = int(input())
closest_num = []
for i in range(n):
    a = list(map(int, input().split()))
    if(a[0] % a[1] != 0):
        q = int(a[0] / a[1])
        closest_num.append((a[1] * (q + 1) - a[0]))
    else:
        closest_num.append(0)


print(*closest_num, sep="\n")
