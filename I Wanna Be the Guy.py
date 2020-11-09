import sys
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
x = a[0]
y = b[0]
a.pop(0)
b.pop(0)
c = a+b
d = c
c = sorted(list(dict.fromkeys(c)))
if(x == 0 and y == 0):
    print("Oh, my keyboard!")
    sys.exit()


def find_missing(c):
    return [i for i in range(c[0], c[-1]+1)
            if i not in c]


c = find_missing(c)
if len(c) == 0 and n in d and 1 in d:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
