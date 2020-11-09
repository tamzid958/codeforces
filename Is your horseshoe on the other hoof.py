s = sorted(list(map(int, input().split())))
d = 3
for i in range(3):
    if(s[i] != s[i+1]):
        d -= 1

print(d)
