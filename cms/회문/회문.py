import sys
sys.stdin = open("sample_input.txt","r")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    str_list = [list(input()) for _ in range(N)]
    ans = ""
    for i in range(N):
        for j in range(N-M+1):     
            word = str_list[i][j:j+M]
            if word == word[::-1]:
                ans = "".join(word)
                break

        for j in range(N):
            for r in range(N-M+1):
                word_ex =[]

                for i in range(r, r+M):    
                    word_ex.append(str_list[i][j])

                if word_ex == word_ex[::-1]:
                    ans = "".join(word_ex)
                    break
            if ans :
                break

    print(f"#{tc} {ans}")
