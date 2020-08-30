import math
n = int(input())
sum = 0
if(n % 2 == 0):
    print(int(n/2))
else:
    print(-math.ceil((n/2)))
