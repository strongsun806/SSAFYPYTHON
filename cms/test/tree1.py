'''
완전 이진트리에서 11번 정점의 조상노드의 번호
'''

n=11
while n >0:
    n//=2
    print(n)

def pre_order(T):   # 전위순회, 방문한 정점(부모) 먼저 처리
    if T:   # 0이 아니면 (존재하는 정점이면)
        print(T)    # visit(T) T에서 할일 처리
        pre_order(left[T])  # 왼쪽 자식(서브트리)로 이동
        pre_order(right[T]) # 오른쪽 자식(서브트리)로 이동

N = int(input())    # 1번 부터 N번 정점이 존재
E = N -1 # 간선 수
arr = list(map(int, input().split()))

# 부모를 인덱스로 자식번호 저장
left = [0]*(N+1)    #N번 인덱스 필요
right = [0]*(N+1)

for i in range(E):
    p,c=arr[i*2], arr[i*2+1]
    if left[p]==0:
        left[p]=c

    else:
        right[p]=c

pre_order(1)
# 자식을 인덱스로 부모번호 저장
