'''
N 개의 서로 다른 양의 정수, R, K 가 주어진다.
원소가 정확히 R개이면서 합이 K인 부분집합의 개수를 출력하시오

입력
1
5 2 6
1 2 3 4 5

출력
#1 2
'''
def dfs(idx, size, total):
    global cnt
    if size > R:    # size가 R보다 큰 경우는 볼 필요 없음!!
        return

    if total > K:   # total이 K보다 큰 경우는 볼 필요 없음!!
        return
    
    if idx == N:
        if size == R and total == K:
            cnt += 1
        return

    dfs(idx + 1, size + 1, total + arr[idx])
    dfs(idx + 1, size, total)

T = int(input())

for tc in range(1, T+1):
    N, R, K = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    dfs(0,0,0)
    print(f'#{tc} {cnt}')