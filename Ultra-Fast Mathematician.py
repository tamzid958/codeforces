a = input()
b = input()
a = list(a)
b = list(b)
c = []
for i in range(len(a)):
    if(a[i] == b[i]):
        c.append("0")
    else:
        c.append("1")

print(*c, sep='')
