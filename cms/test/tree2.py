# 이진 트리 저장하기(이진트리 표현)
'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
V= int(input())
edges=list(map(int,input().split()))
# 정짐이 13개고, 13번 인덱스 까지 필요 (V+1)개 짜리 만드는데,
# 0번은 왼쪽자식 번호, 1번은 오른쪽 자식 번호 저장
tree= [[-1]*2 for _ in range(V+1)]
for i in range(0,(V-1)*2, 2):
    if tree[edges[i]][0]==-1:
        tree[edges[i]][0] = edges[i+1]
    else:
        tree[edges[i]][1] = edges[i+1]

print(tree)
# 트리를 순회! 전위순회, 중위순회, 후위순회
# 어차피 모든 노드 탐색해야하니 '모든 길 찾기'라는 건 똑같음
# 해당 노드의 작업을 언제하냐의 차이
# 트리는 재귀적인 구조를 가진다!

# v번에서 방문해서 작업을 수행하는 함수
# v번에서 일을 하긴 할건데, 모든 노드를 탐색하기 위해서는
# 다른 노드(자식노드)로 이동하는 게 필요한데, 포함해서 작성
def traversal(v):
    if v == -1: #없는 정점
        return
    print(v,end=' ')
    # 왼쪽자식 방문하고
    traversal(tree[v][0])
    # 오른쪽 자식 방문
    traversal(tree[v][1])

traversal(1)