T = int(input())
for tc in range(1, T+1):
    n = int(input())
    num = list(map(int, input()))
 
    cnt = 0
    result = 0
    for i in range(n):
        if num[i] == 1:
            cnt += 1
            if cnt > result :
                result = cnt
        elif num[i] == 0:
            cnt = 0
 
    print(f'#{tc} {result}')
                             