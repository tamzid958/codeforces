n, m = map(int, input().split())


for i in range(1, n+1):
    for j in range(m):
        if(i % 4 == 0):
            if j == 0:
                print("#", end="")

            else:
                print(".", end="")
        elif(i % 4 == 2):
            if j == m-1:
                print("#", end="")

            else:
                print(".", end="")

        else:
            print("#", end="")

    print("")
