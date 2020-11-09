n = int(input())
lst = []
index_one = []
index_two = []
guest = 0
for i in range(n):
    a = list(map(int, input().split()))
    lst.append(a[0])
    lst.append(a[1])

index_one = lst[0::2]
index_two = lst[1::2]

for i in range(n):
    guest += index_two.count(index_one[i])


print(guest)
