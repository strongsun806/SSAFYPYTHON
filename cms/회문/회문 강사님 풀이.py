# data에 길이 M인 회문이 있으면 찾아서 반환하는 함수
def solve(data):
    #  검사할 문장의 시작점 순회
    for i in range(N):   # 모든 행 검사
        for j in range(N-M+1):   # 열은 M보다 작은 뒤쪽은 검사 안함
            #  j열에서 시작하는 길이 M짜리 회문 검사
            is_find = True
            for k in range(M//2):
                # j+k번이랑 j+M-1-k번이랑 비교
                if data[i][j+k] != data[i][j+M-1-k]:
                    is_find = False   # 회문 아님
                    break
            # 회문이면 회문 반환
            if is_find:   # j번 부터 j+M-1 번까지 회문이다
                palinedrome = ''
                for l in range(j, j+M):
                    palinedrome +=data[i][l]
                return palinedrome

    for i in range(N):   # 복사해서 열 검사
        for j in range(N-M+1):  
            is_find = True
            for k in range(M//2):
                # 행 열 바꿔서 적용
                if data[j+k][i] != data[j+M-1-k][i]:
                    is_find = False
                    break
            if is_find:
                palinedrome = ''
                for l in range(j, j+M):
                    # 행 열 바꿔서 적용
                    palinedrome += data[l][i]
                return palinedrome
import sys
sys.stdin = open("sample_input.txt","r")

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = [input().strip() for _ in range(N)]
    result = solve(data)
    print(f"#{tc} {result}")