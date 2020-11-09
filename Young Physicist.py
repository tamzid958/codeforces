n = int(input())
lst = []
co_1 = co_2 = co_3 = 0
for i in range(0, n):
    coordinate = input().split()

    lst.append(coordinate)
for i in range(0, n):
    co_1 += int(lst[i][0])
    co_2 += int(lst[i][1])
    co_3 += int(lst[i][2])


if co_1 == 0 and co_2 == 0 and co_3 == 0:
    print("YES")
else:
    print("NO")
