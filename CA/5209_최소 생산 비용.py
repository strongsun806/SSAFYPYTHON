# ========================================================
# 문제: 13126_5209. [파이썬 S/W 문제해결 구현] 5일차 - 최소 생산 비용
# 난이도: D3
# 작성자: 윤형섭 (1627575)
# 제출 결과: Pass
# 저장 일시: 2026-10-07 11:27:07
# ========================================================

#import sys
# sys.stdin = open("input.txt", "r")
 T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
     # 비용 판떼기(행렬) 만들기
    matrix = []
    for i in range(N):
        matrix.append(list(map(int, input().split())))
    # pprint(matrix)
     visited = [False] * N  # 공장 선택 여부 체크 리스트
    min_cost = 999999  # 최소 생산 비용
     # product_idx: 현재 배정할 제품 번호 (0 ~ N-1)
    # current_cost: 지금까지 누적된 생산 비용
    def dfs(product_idx, current_cost):
        global min_cost
         # 가지치기: 현재 누적 비용이 이미 알고 있는 최솟값보다 크거나 같으면 바로 컷!
        if current_cost >= min_cost:
            return
         # N개 제품 배정이 모두 끝났을 때
        if product_idx == N:
            if current_cost < min_cost:
                min_cost = current_cost
            return
         # j번째 공장에 배정하기
        for j in range(N):
            if not visited[j]:  # 아직 선택 안 된 공장이라면
                visited[j] = True  # 공장 사용 표시
                # 다음 제품 배정하러 재귀 호출 (비용 누적)
                dfs(product_idx + 1, current_cost + matrix[product_idx][j])
                visited[j] = False  # 다시 원상복구 (백트래킹)
     # 0번 제품부터 비용 0원으로 탐색 시작
    dfs(0, 0)
     print(f'#{test_case}', min_cost)
