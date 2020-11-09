n = int(input())
lst = {}
for i in range(0, n):
    s = input()
    if s in lst:
        print(s+str(lst[s]))
        lst[s] += 1
    else:
        print("OK")
        lst[s] = 1
