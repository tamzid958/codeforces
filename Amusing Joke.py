lst = []


for i in range(3):
    a = input()
    lst.append(a)

if sorted(lst[0]+lst[1]) == sorted(lst[2]):
    print("YES")
else:
    print("NO")
