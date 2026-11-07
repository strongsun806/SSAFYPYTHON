'''
합이 0인 부분집합이 있는가

N개의 정수(음수 포함)가 주어진다.
공집합을 제외한 부분집합 중에 합이 0인 것이 하나라도 있으면 1, 없으면 0을 출력하시오.

입력
2
5
-7 -3 -2 5 8
5
1 2 3 4 5

출력
#1 1
#2 0
'''
# 첨에는 size 없이 풀다가 부분집합을 전역 변수로 받아와야하고 len(부분집합) 해줘야 해서 이렇게 수정함
def dfs(idx, total, size):
    global found
    if found:   # 이미 찾았으면 더 볼 필요 없음
        return

    if idx == N:    # 재귀 종료 조건
        # 공집합을 제외한 부분집합이라고 했기 때문에
        # size가 0보다 크고 합이 0일 때 발견한 것
        if size > 0 and total == 0: 
            found =1
        return

    dfs(idx + 1, total + arr[idx], size + 1)    # 부분집합에 포함하는 경우
    dfs(idx + 1, total, size)                   # 부분집합에 포함하지 않는 경우

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    found = 0
    dfs(0, 0, 0)
    print(f'#{tc} {found}')
