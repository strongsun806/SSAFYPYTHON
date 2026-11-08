# DFS (인접행렬) = 가능한 모든 정점 1번씩 탐색
# now를 바꿔가며 하기


name = "BACD"
arr = [
    [0, 0, 1, 1],
    [1, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 0, 0]]

n = len(name)
# B A C D 순서
used = [0] * n  # 정점의 개수만큼 방문 체크

def dfs(now):

    print(name[now], end=' ')

    for i in range(n):
        if arr[now][i] == 1 and used[i] == 0:
            used[i] = 1
            dfs(i)

used[1] = 1  # 탐색 시작 인덱스에 1 중복 체크
# dfs(1)  # 탐색 시작 인덱스

#########################
# DFS (인접 리스트) = 한 정점에서 다른 정점까지의 도착할 수 있는 경우가 몇 가지?
# 4 6
# 0 2
# 0 3
# 1 0
# 1 2
# 2 0
# 2 3
# N, M = map(int, input().split())
arr = [[] for _ in range(n)]
print(arr)
# for _ in range(M):
#     start, end = map(int, input().split())
#     arr[start].append(end)

# used = [0] * N

# cnt = 0

# def dfs2(now):
#     global cnt
#     if now == 3:
#         cnt += 1
#     # print(name[now], end=' ')


#     for i in arr[now]:
#         if used[i] == 0:
#             used[i] = 1
#             dfs2(i)
#             used[i] = 0

# used[1] = 1
# dfs2(1)
# print(cnt)

###########################
from collections import deque

q = deque()
used = [0] * n
q.append(0)
used[0] = 1
name = "ABCD"
while q:
    now = q.popleft()
    print(name[now], end=' ')
    for i in arr[now]:
        if used[i] == 0:
            used[i] = 1
            q.append(i)


##############################
# arr = [i for i in range(6)]
print(arr)
arr = [0, 1, 2, 3, 4, 5]
rank = [0] * 6

def findboss(member):
    if arr[member] == member:  # 자기 자신이 보스라면(그 그룹의 보스 찾음)
        return member
    ret = findboss(arr[member])  # 보스가 아니라면 arr 배열의 값을 가지고 보스 찾기
    arr[member] = ret  # 경로 단축(시간 단축 관련해서, 이거 존나 중요 ㅇㅇ)
    return ret

def union(a, b):
    fa = findboss(a)
    fb = findboss(b)
    if fa == fb:  # 두 보스가 같으면 이미 같은 그룹
        return

    # arr[fb] = fa  # 두 보스가 다르면 a의 보수가 통합 장
    # 이건 옵션이라 필수는 아님
    if rank[a] == rank[b]:
        rank[a] += 1
        arr[fb] = fa
    elif rank[a] > rank[b]:
        arr[fb] = fa
    else:
        arr[fa] = fb



union(0, 1)
union(3, 4)
union(1, 4)
union(1, 3)
union(5, 4)

y, x = map(int, input().split())  # 숫자 2개 입력 후 같은 그룹인지 출력
if findboss(y) == findboss(x):
    print("이미 같은 그룹")
else:
    print("다른 그룹")