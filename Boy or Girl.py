x = input()


def removeDuplicate(str):
    s = set(str)
    s = "".join(s)
    if(len(s) % 2 == 0):
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")


removeDuplicate(x)
