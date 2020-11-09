a, b = input().split()
a = int(a)
b = int(b)
counter = loop = 0
while(loop == 0):
    a = a*3
    b = b*2
    if(a <= b):
        counter += 1
    else:
        loop = 1


print(counter+1)
