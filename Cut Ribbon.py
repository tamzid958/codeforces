import sys
sys.setrecursionlimit(500000000)


def f(n):
    if n in memo.keys():
        return memo[n]

    ans = float("-inf")
    if n == 0:
        return 0
    for length in l:

        if n >= length:
            ans = max(ans, 1 + f(n - length))

    memo[n] = ans
    return ans


memo = dict()


l = list(map(int, input().split()))
n, l = l[0], l[1:]
print(f(n))
