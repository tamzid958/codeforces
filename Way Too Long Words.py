lst = []
ele = ""
n = input()
n = int(n)
for i in range(0, n):
    ele = input()
    try:
        ele = int(ele)
    except ValueError:
        if(len(ele) > 10):
            shortword = (str(ele[0]) + str(len(ele) - 2) +
                         str(ele[len(ele) - 1]))
        else:
            shortword = ele
        lst.append(shortword)

for i in range(0, n):
    print(lst[i])
