n = int(input())
counter = 0
for i in range(0, n):
    x, y, z = map(int, input().split())
    if(x+y+z >= 2):
        counter = counter + 1
print(counter)
