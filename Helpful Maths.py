math_eqn = input()
lst = []
new_string = ""
a = b = c = 0
for i in range(0, len(math_eqn)):
    if(math_eqn[i] == "1" or math_eqn[i] == "2" or math_eqn[i] == "3"):
        lst.append(int(math_eqn[i]))

lst.sort()

for i in range(len(lst)):
    new_string = new_string + str(lst[i]) + "+"


print(new_string[:-1])
