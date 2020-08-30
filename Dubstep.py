import re
s = input()
s = s.replace("WUB", " ")
s = re.sub(' +', ' ', s)
print(s.lstrip())
