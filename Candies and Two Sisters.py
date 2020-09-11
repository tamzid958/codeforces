n = int(input())
lst = []

for i in range(n):
    a = int(input())
    if a % 2 == 0 and a != 0:
        lst.append(int(a/2)-1)
    else:
        lst.append(int(a/2))
print(*lst, sep="\n")
