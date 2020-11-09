t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    c = abs(b-a)
    s = int(c/10)
    if c - (s*10) != 0:
        s = s+1
    print(s)
