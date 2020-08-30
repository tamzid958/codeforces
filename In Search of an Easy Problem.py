n = int(input())
a = list(map(int, input().split()))
counter = 0
for i in range(n):
    if(a[i] == 1):
        break
    else:
        counter += 1

if(counter == len(a)):
    print("EASY")
else:
    print("HARD")
