# sys.stdin = open("input.txt", "r")

def find_set(x, parent):
    if parent[x] == x:
        return x
    parent[x] = find_set(parent[x], parent)
    return parent[x]

def union(x, y, parent):
    rx = find_set(x, parent)
    ry = find_set(y, parent)
    if rx != ry:
        parent[ry] = rx
        return True
    return False

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    edges = []
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        edges.append((n1, n2, w))
        
    # 가중치 오름차순 정렬 (크루스칼)
    edges.sort(key=lambda x: x[2])
    parent = [i for i in range(V + 1)]
    
    total_w = 0
    cnt = 0
    
    for n1, n2, w in edges:
        if union(n1, n2, parent):
            total_w += w
            cnt += 1
            if cnt == V:
                break
                
    print(f"#{tc} {total_w}")
