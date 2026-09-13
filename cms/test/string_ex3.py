N = int(input())
txt = [input() for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(N):
        if txt[i][j] == "#" :
            cnt += 1

print(cnt)