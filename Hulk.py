n = int(input())

for i in range(n):
    if(i % 2 == 0):
        print("I hate", end=" ")
    if(i % 2 != 0):
        print("I love", end=" ")
    if(i < n-1):
        print("that", end=" ")


print("it", end="")
