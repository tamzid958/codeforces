n = input()
x = n.replace("7", "")
y = x.replace("4", "")

if y == "" and "7" in n and "4" in n:
    print("YES")
else:
    a = int(n)
    if(a % 4 == 0 or a % 7 == 0 or a % 47 == 0 or a % 74 == 0):
        print("YES")
    else:
        print("NO")
