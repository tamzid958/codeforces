n = int(input())
s = input()
s = s.lower()
s = ''.join(set(s))

if(len(s) == 26):
    print("YES")
else:
    print("NO")
