n = int(input())
a = list(map(int, input().split()))
count = max_counter = 0
for i in range(n):
    if(a[i] >= a[i-1]):
        count += 1
        max_counter = max(max_counter, count)

    else:
        count = 1
print(max_counter)
