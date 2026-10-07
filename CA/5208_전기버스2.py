# ========================================================
# 문제: 13125_5208. [파이썬 S/W 문제해결 구현] 5일차 - 전기버스2
# 난이도: D3
# 작성자: 윤형섭 (1627575)
# 제출 결과: Pass
# 저장 일시: 2026-10-07 11:27:21
# ========================================================

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    data = list(map(int, input().split()))
    N = data[0]  # 정류장 수 (목적지는 N번)
    battery = data[1:]  # 1번 정류장부터 N-1번 정류장까지 배터리 용량 리스트
    # print(N, battery)
     min_count = 999999  # 최소 교환 횟수 저장용 큰 수
     # idx: 현재 정류장 인덱스 (0번이 1번 정류장)
    # count: 지금까지 교환한 횟수
    def dfs(idx, count):
        global min_count
         # 가지치기: 이미 현재 교환 횟수가 최솟값 이상이면 더 볼 필요도 없음
        if count >= min_count:
            return
         # 현재 정류장에서 갈 수 있는 거리 (멀리 가는 것부터 역순 탐색해서 가지치기 효율 높임!)
        for step in range(battery[idx], 0, -1):
            next_idx = idx + step
             # 목적지(N-1 인덱스)에 도착하거나 넘어선 경우
            if next_idx >= N - 1:
                if count < min_count:
                    min_count = count
                break  # 제일 멀리 가서 도달했으므로 더 작은 step은 볼 필요 없음
            else:
                # 다음 정류장으로 가서 배터리 교환하므로 count + 1
                dfs(next_idx, count + 1)
     # 1번 정류장(idx=0)에서 출발! 처음 배터리는 장착된 상태이므로 교환 횟수는 0부터 시작
    dfs(0, 0)
     print(f'#{test_case}', min_count)
