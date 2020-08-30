m, n, a = input().split()

m = int(m)
n = int(n)
a = int(a)

x = m/a
y = n/a


if m % a != 0:

    x = x + 1

if n % a != 0:

    y = y + 1

x = int(x)
y = int(y)
print(x*y)
