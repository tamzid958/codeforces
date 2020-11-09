t = int(input())

for i in range(t):
    stack = []
    count = 0
    a = int(input())
    if a % 1000 != 0 and a > 1000:
        count += 1
        stack.append(int(a / 1000)*1000)
        a = a % 1000
    if a % 100 != 0 and a > 100:
        count += 1
        stack.append(int(a / 100)*100)
        a = a % 100
    if a % 10 != 0 and a > 9:
        count += 1
        stack.append(int(a / 10)*10)
        a = a % 10
    count += 1
    stack.append(a)
    print(count, sep="\n")
    print(*stack)
