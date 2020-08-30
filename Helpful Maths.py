math_eqn = input()
lst = []
lst2 = []
a = b = c = 0
for i in range(0, len(math_eqn)):
    if(math_eqn[i] == "1" or math_eqn[i] == "2" or math_eqn[i] == "3"):
        lst.append(int(math_eqn[i]))

lst.sort()
n = len(lst)
for i in range(0, n):
    lst2 = str(lst[i])+"+"

for i in range(0, n-1):
    print(str(lst[i])+"+", end="")

print(lst2[:-1])
