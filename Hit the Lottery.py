balance = int(input())

c1 = int(balance / 100)
remain = int(balance % 100)

c2 = int(remain / 20)
remain = int(remain % 20)

c3 = int(remain / 10)
remain = int(remain % 10)

c4 = int(remain / 5)
remain = int(remain % 5)

c5 = remain


print(c1+c2+c3+c4+c5)
