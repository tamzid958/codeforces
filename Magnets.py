n = int(input())
count = 1
lst = []
for i in range(n):
    lst.append(input())

for i in range(n-1):
    if(lst[i] != lst[i+1]):
        count += 1
print(count)
