n = input()
n = int(n)
counter = 0
for i in range(0, n):
    x, y, z = input().split()
    x = int(x)
    y = int(y)
    z = int(z)
    if(x+y+z == 3 or x+y == 2 or y+z == 2 or x+z == 2):
        counter = counter + 1
print(counter)
