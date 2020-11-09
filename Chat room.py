s = input()
n = len(s)
l = 0
for i in range(n):
    if s[i] == 'h' and l == 0:
        l += 1
    elif s[i] == "e" and l == 1:
        l += 1
    elif s[i] == "l" and l == 2:
        l += 1
    elif s[i] == "l" and l == 3:
        l += 1
    elif s[i] == "o" and l == 4:
        l += 1
    if(l == 5):
        break

if(l == 5):
    print("YES")
else:
    print("NO")
