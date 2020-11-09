import re

s = input()

uppercase = re.findall('([A-Z])', s)
lowercase = re.findall('([a-z])', s)

if(len(uppercase) > len(lowercase)):
    s = s.upper()
else:
    s = s.lower()

print(s)
