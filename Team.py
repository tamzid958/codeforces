n = input()
n = int(n)
counter = 0
for i in range(0, n):
    x, y, z = input().split()
    x = int(x)
    y = int(y)
    z = int(z)
    if(x+y+z >= 3):
        counter += 1

print(counter)
