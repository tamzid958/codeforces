s = input()
counter = counter2 = 0
for i in range(1, len(s)):
    if(s[i].islower()):
        counter += 1
    if(s[i].isupper()):
        counter2 += 1


def caps_lock():
    if(s[0].islower() and counter == 0):
        print(s.title())
        return
    if(counter2+1 == len(s)):
        print(s.lower())
    else:
        print(s)


caps_lock()
