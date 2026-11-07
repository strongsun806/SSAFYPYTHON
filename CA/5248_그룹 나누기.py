# sys.stdin = open("input.txt", "r")

def find_set(x):
    if parent[x] == x:
        return x
    parent[x] = find_set(parent[x])
    return parent[x]

def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)
    if root_x != root_y:
        parent[root_y] = root_x

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    listed = list(map(int, input().split()))
    
    # 1번부터 N번까지 각자 자신을 대표자로 초기화
    parent = [i for i in range(N + 1)]
    
    # M쌍의 신청서 짝 맞춰서 union
    for i in range(0, len(listed), 2):
        p1 = listed[i]
        p2 = listed[i + 1]
        union(p1, p2)
        
    # 각 원소의 대표자를 찾아 집합(그룹) 개수 구하기
    groups = set()
    for i in range(1, N + 1):
        groups.add(find_set(i))
        
    print(f"#{tc} {len(groups)}")
