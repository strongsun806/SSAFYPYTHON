# 1. MST(Prim, Kruskal) - 무향 그래프
#     vs
# 2. 최단 경로(Dijkstra) - 유향 그래프

# 총 3가지 알고리즘은 전부 탐욕 알고리즘임
# 제발 서로 헷갈리지 마세요!

# 목표:
# 1차. 얘네들의 동작 방식을 그림으로 그리고 이해하기. 설명 가능하도록
# 2차. 코드 짜기

##########################################################################
###                                M S T                               ###
##########################################################################

# Prim: MST를 만들어가는 알고리즘
# 1. 임의의 정점을 선택
# 2. 선택한 정점들에 연결되는 간선 중에 최소 비용 간선 선택
# 3. 최소 비용 간선을 선택하면, 하나의 정점이 선택될거임 ㅇㅇ
# 4. 새로운 정점이 하나 선택되면, 새롭게 선택된 정점을 포함해서
#    다시 또 연결된 간선들이 나올거임
#    그 중에서도 또 최솟값 나오는 정점 선택하기
#    모든 정점이 선택될 때까지 반복

# Kruskal: MST를 만드는 알고리즘
# 1. 간선 비용기준 오름차순 정렬
# 2. 비용이 작은 간선부터 선택
# 3. 단, 간선을 선택하는 과정에서 '사이클'이 발생하면,
#    해당 간선은 선택하지 않음
#    (정점을 같은 간선을 두 번 지나지 않고 되돌아 올 수 있으면 사이클)
# 4. 모든 정점을 선택하면 MST 완성

# 일단 위의 2가지 설명할 수 있는게 1차 목표

# 밑에는 2차 목표인 코드짜기

# 선택된 정점들에서 각 정점으로 가는 비용
# weight [inf | inf | inf | inf | inf | inf | inf]
#          0     1     2     3     4     5     6
# ->     [inf | inf | inf |  0  | inf | inf | inf] -> 3번을 임의로 선택
# ->     [inf | inf | inf |  0  |  34 |  18 | inf] -> (교재 그림 참고) 5번 선택됨
# ->     [ 31 |  21 |  46 |  0  |  34 |  18 |  25]

# import sys
# sys.stdin = open("input_teacher_prim_kruskal.txt", "r")

# # import heapq

# V, E = map(int, input().split())

# adj = [[0] * (V + 1) for _ in range(V + 1)] # 인접 행렬 만들기
# for _ in range(E):
#     a, b, w = map(int, input().split())
#     adj[a][b] = w
#     adj[b][a] = w

# # for row in adj:
# #     print(row)

# def prim(start):
#     # MST에서 선택된 정점들로부터 각 정점들로 가는 비용
#     weights = [0xffffffff] * (V + 1)
#     MST = set()
#     weights[start] = 0

#     while True:
#         if len(MST) == V+1:
#             break


#         # 선택된 정점들에서 다른 정점으로 가는 비용 중에 최소 비용 선택하기
#         min_idx = -1
#         min_v = 0xffffffff

#         for i in range(V + 1):  # i: 정점 번호
#             if i not in MST and weights[i] < min_v:
#                 min_idx = i
#                 min_v = weights[i]
#     # 금일 라이브에서는 이 부분을 heapq로 풀었음
#     # 이 반복문 다 돌고나면, 최소 비용으로 갈 수 있는 정점이 선택됨

#         MST.add(min_idx)

#         for i in range(V + 1):
#             # 원래 내가 알고 있던 i번 연결 비용: weights[i]
#             # min_idx가 추가되면서 새로운 연결 비용: adj[min_idx][i]
#             if adj[min_idx][i] and i not in MST and adj[min_idx][i] < weights[i]:
#                 weights[i] = adj[min_idx][i]

#     print(weights)

# prim(0)


############ Kruskal #############
# 사이클 판단 어케하는지가 핵심임 ㅇㅇ
# -> 연결이 되면 같은 그룹으로 구성, 같은 그룹 안의 정점을 연결하는 사이클을 발생시킴!

# import sys
# sys.stdin = open("input_teacher_prim_kruskal.txt", "r")

# # import heapq

# # 그룹 나누기
# # 각 정점의 대표자를 설정
# # 시작은 각 정점을 모두 다른 그룹으로 만들기
# V, E = map(int, input().split())
# edges = [list(map(int, input().split())) for _ in range(E)]
# # print(edges)

# # 각 정점의 대표자를 저장하는 배열
# parent = [x for x in range(V + 1)]
# # print(parent)  # [0, 1, 2, 3, 4, 5, 6]

# # 두 정점을 하나의 그룹으로 만들기 -> Union
# # -> 이걸 하려면, 현재 두 정점의 두 대표를 하나로 만들어주기를 해야함
# # -> 각 정점의 대표 찾기가 선행되어야함 ㅇㅇ

# # 정점의 대표 찾기
# def find_set(x):
#     # 정점의 부모 번호가 스스로라면,
#     # 해당 정점은 그 그룹의 대표자임 ㅇㅇ
#     if parent[x] == x:
#         return x
    
#     parent[x] = find_set(parent[x])  # 원정씨 코드 ㅇㅇ
#                                      # 난 아직 이해가 잘 안가니까 GPT랑 이야기하기

#     # 정점의 부모가 스스로가 아니라면, 부모의 대표자를 찾아서 반환
#     return find_set(parent[x])

# # 이렇게도 가능
# # def find_set(x):
# #     if parent[x] != x:
# #         parent[x] = find_set(parent[x])

# #     return parent[x]
    

# # 두 정점을 하나의 그룹으로 만들기(Union)
# # -> 두 정점의 두 대표를 하나로 만들어주기
# def union(x, y):
#     # x의 대표를 y의 대표로 만들면(또는 반대로..)
#     px = find_set(x)  # px의 부모는 px
#     py = find_set(y)  # py의 부모는 py

#     parent[py] = px

# # print(find_set(2))
# # print(find_set(3))
# # union(2, 3)
# # print('---------')
# # print(find_set(2))
# # print(find_set(3))
# # 숫자들 바꿔서 여러 실험 해보기

# def kruskal():
#     # 1. 간선 비용 기준으로 오름차순 정렬
#     edges.sort(key=lambda x:x[2])
#     # 그냥 edges.sort()를 하면 맨 앞의 간선 번호 기준으로 됨 ㅇㅇ
#     # -> key값 받아와서 정렬하기

#     # 모든 간선에 대해서 선택 여부 판단
#     MST = []
#     for edge in edges:
#         # 선택했을 때 사이클이 안생기면 선택
#         # -> 두 정점이 같은 그룹이 아니라면 선택
#         a, b, weight = edge
#         if find_set(a) != find_set(b):  # 각 대표자가 다르면 다른 그룹이니까 사이클이 생기지 않음
#             union(a, b)  # 선택했으니까 같은 그룹으로 만들어주기
#             MST.append(edge)

#     return MST

# print(kruskal())

# c.f) 게리맨더링(백준)


##########################################################################
###                             Dijkstra                               ###
##########################################################################

# 음의 가중치가 흔하진 않은데 암튼 허용하지 않음 ㅇㅇ

# Prim이랑 비슷한 점 - weight 사용하긴함 ㅇㅇ 
# Prim이랑 다른 점 - weight 샬라샬라 ㅠ 뭐더라

# 일단 당장 알고있는 비용 중에서 최소 비용이 최단거리라고 생각하는거임
# 돌아가면 더 들거라고 생각하는 방법이라함 ㅇㅇ 신기하네 무슨 자신감이여

# 1. 시작점에서 다른 정점까지 가는 비용계산
# 2. 그 중에서 가장 작은 비용이면 경로 확정
# 3. 그 경로로 다른 정점까지 가는 비용 계산해보고, 더 작으면 수정하기
# 4. 목적지까지 비용이 확정 될 때까지 1 ~ 3번 반복

import sys
sys.stdin = open("input_teacher_dijkstra.txt", "r")

import heapq

V, E = map(int, input().split())
adj = [[0] * (V + 1) for _ in range(V + 1)]
for _ in range(E):
    s, e, w = map(int, input().split())
    # 유향 그래프니까
    adj[s][e] = w
    # 이 만큼의 가중치를 가진다~ 까지 저장하면 좋겠다~


def dijkstra(start, end):
    # 시작점에서 다른 정점으로 가는 비용
    weights = [0xffffffff] * (V + 1)

    # 이미 비용계산이 완료되었는지 여부 체크
    done = [0] * (V + 1)
    weights[start] = 0

    while True:  # (사실 V + 1번만 돌리면 나오는거라 굳이 while을 안써도 된다고 함 ㅇㅇ)
        # 시작점에서 최소 비용으로 갈 수 있는 정점 찾기
        min_idx = -1
        min_value = 0xffffffff
        for i in range(V + 1):
            if weights[i] < min_value and not done[i]:
                min_idx = i
                min_value = weights[i]

        done[min_idx] = 1  # 해당 정점까지 가는 비용 확정
        if min_idx == end:  # 목적지까지 비용 계산했다면 멈춰!!!
            break

        # 한 정점까지 가는 비용이 확정
        # -> 이제 그 정점을 경유해서 다른 정점으로 가는 비용 계산할거임
        # -> 만약 정점을 경유해서 다른 정점까지 가는 비용이 더 적으면, 비용 수정하기
        # -> 새롭게 선택된 정점에서 다른 정점까지의 비용 계산: adj[min_idx][i]
        for i in range(V + 1):
            # 1. 연결되어있고,

            # 2. 시작점에서 min_idx 정점을 거쳐서 i까지 가는 비용과 (weights[min_idx] + adj[min_idx][i])
            #    원래 알고있던 시작점에서 i까지 가는 비용           (weights[i])
            #    둘을 비교해야함 ㅇㅇ

            # 3. i번까지 비용이 확정이 안났다면
            if adj[min_idx][i] and (weights[min_idx] + adj[min_idx][i]) < weights[i] and not done[i]:
                weights[i] = (weights[min_idx] + adj[min_idx][i])

    return weights

print(dijkstra(0, 5))