# Problem: 4831_[S/W 문제해결 기본] 1일차 - 전기버스
# Author: 윤형섭_1627575 (Pass)
# Saved by Aura for Boss 💋

def can(station_index, K, N, M):
    gas = K
    result = 0
     # 마지막 충전소 다음의 목적지(종점 N)를 추가해 인덱스 초과 방지
    stations = station_index + [N]
     for i in range(N):
        # 1. 이동 전 gas가 0이면 더 이상 진행 불가
        if gas == 0:
            return 0
         # 1칸 이동 후 gas 소모
        gas -= 1
        current_pos = i + 1
         # 2. 도착한 위치가 충전소인지 확인
        if current_pos in station_index:
            idx = stations.index(current_pos)
            next_target = stations[idx + 1]  # 다음 충전소 또는 종점
             # 다음 지점까지 가기 위한 거리가 현재 남은 gas보다 크다면 충전
            if gas < (next_target - current_pos):
                gas = K
                result += 1
     return result
  T = int(input())
for test_case in range(1, T + 1):
    K, N, M = list(map(int, input().split()))  # 3 10 5
    station_index = list(map(int, input().split()))  # 1 3 5 7 9
    print(f'#{test_case} {can(station_index, K, N, M)}')
