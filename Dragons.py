s, n = map(int, input().split())
game = []
flag = True
for i in range(n):
    dragon_health, bonus = map(int, input().split())
    game.append([dragon_health, bonus])

game = sorted(game)
for i in range(n):
    if s > game[i][0]:
        s += game[i][1]
    else:
        flag = False
        break
if flag:
    print("YES")
else:
    print("NO")
