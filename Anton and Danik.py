n = int(input())
s = input()
s = sorted(list(s))
anton = danik = 0
for i in range(len(s)):
    if(s[i] == 'A'):
        anton += 1
    else:
        danik += 1

if(anton > danik):
    print("Anton")
elif(danik > anton):
    print("Danik")
else:
    print("Friendship")
