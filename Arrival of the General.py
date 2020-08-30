n = int(input())
heights = list(map(int, input().split()))

maxVal = heights[0]
maxValIdx = 0
minVal = heights[n-1]
minValIdx = n-1

for i in range(0, n):
    if heights[i] > maxVal:
        maxVal = heights[i]
        maxValIdx = i

    if heights[i] <= minVal:
        minVal = heights[i]
        minValIdx = i

swaps = maxValIdx
swaps += (n - 1) - minValIdx

if maxValIdx > minValIdx:
    swaps -= 1


print(swaps)
