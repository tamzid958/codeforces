n = int(input())

if (n <= 11):
    if (n == 8):
        print("4 4")
    if (n == 10):
        print("4 6")
    else:
        print("-1")
if (n % 2 == 0):
    print("4", n - 4)


else:
    print("9", n - 9)
