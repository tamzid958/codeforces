a = [int(n) for n in input().split()]

k = max(a)

b = [abs(x-k) for x in a if x != k]
b.reverse()

print(*b)
