'''
두 그룹으로 나눈 합의 최소 차이

N개의 양의 정수를 두 그룹으로 나눈다.(한 그룹이 비어도 됨).
두 그룹의 합의 차이(절대값)의 최소값을 출력하시오.

입력
2
5
1 2 3 4 5
4
3 1 4 2

출력
#1 1
#2 0
'''
def dfs(idx, S):
    global min_v
    if idx == N:
        diff = abs(total - 2 * S)
        if diff < min_v:
            min_v = diff
        return
    
    dfs(idx + 1, S + arr[idx])
    dfs(idx + 1, S)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    # 두 그룹의 합의 차이(절대값)의 최소값
    # 전체 합 total
    # 그룹 A의 합 >> S, 그룹 B의 합 >> total - S
    # |B-A|의 최소값 찾기..
    total = sum(arr)
    min_v = total
    dfs(0,0)
    print(f'#{tc} {min_v}')