'''
합이 K인 부분집합의 개수

N개의 서로 다른 양의 정수와 K가 주어진다.
원소의 합이 정확히 K인 부분집합의 개수를 출력하시오.

입력
1
5 10
1 2 3 4 5

출력
#1 3
'''

def dfs(idx, total):
    global cnt
    if total > K:   # K보다 합이 크면 볼 필요 없음!! 이것이 가지치기
        return
    
    if idx == N:    # 재귀 종료 조건
        if total == K:
            cnt += 1
        return

    dfs(idx + 1, total + arr[idx])  # 부분집합으로 넣는 경우
    dfs(idx + 1, total)             # 부분집합으로 안 넣는 경우


T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0

    dfs(0, 0)
    print(f'#{tc} {cnt}')