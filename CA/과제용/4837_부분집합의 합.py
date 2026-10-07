# Problem: 4837_[S/W 문제해결 기본] 2일차 - 부분집합의 합
# Author: 윤형섭_1627575 (Pass)
# Saved by Aura for Boss 💋

A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
all_subsets = [[]]  # 공집합부터 시작
 for num in A:
    new_subsets = []
    # 지금까지 만들어둔 부분집합 각각에 현재 숫자를 추가해서 새 부분집합 만들기
    for sub in all_subsets:
        new_subsets.append(sub + [num])
    # 기존 리스트 뒤에 새로 만든 것들을 합침
    all_subsets.extend(new_subsets)
  # 2. 테스트 케이스 처리
T = int(input())
 for tc in range(1, T + 1):
    N, K = map(int, input().split())
    answer = 0
     # 만들어둔 모든 부분집합을 하나씩 순회하며 조건 검사
    for sub in all_subsets:
        # 원소 개수 확인
        if len(sub) == N:
            # 원소 합 구하기 (기본 반복문으로 직접 누적)
            total = 0
            for x in sub:
                total += x
             # 합이 K와 같은지 확인
            if total == K:
                answer += 1
     print(f"#{tc} {answer}")
