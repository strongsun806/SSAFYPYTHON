def find_pat(text, N):
    pat = ['AB', 'CD']
    for i in range(N-1):  # 기준위치 i,k
        for j in range(N-1):
            cnt = 0
            for r in range(2):
                for c in range(2):
                    if text[i+r][j+c] == pat[r][c]:
                        cnt += 1
            if cnt == 4 :
                return 'YES'
    return 'NO'


N = int(input())
text = [input() for _ in range(N)]

print(find_pat(text, N))