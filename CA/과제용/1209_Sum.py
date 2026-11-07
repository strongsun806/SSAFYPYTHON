# Problem: 1209_[S/W 문제해결 기본] 2일차 - Sum
# Author: 윤형섭_1627575 (Pass)
# Saved by Aura for Boss 💋

T = 10  # 보통 이 문제는 10개의 테스트 케이스가 고정으로 주어집니다.
for _ in range(1, T + 1):
    test_case = int(input())  # 테스트 케이스 번호 입력받기
    matrix = []
         for i in range(100):
        matrix.append(list(map(int, input().split())))
         count = 0  # 최댓값 저장
         # 1. 가로 및 세로 계산
    for i in range(100):
        k = 0  # 가로 합
        l = 0  # 세로 합
        for j in range(100):
            k += matrix[i][j]
            l += matrix[j][i]
                     if k > count:
            count = k
        if l > count:
            count = l
     # 2. 대각선 (좌상 -> 우하)
    x = 0
    for i in range(100):
        x += matrix[i][i]
    if x > count:
        count = x
     # 3. 대각선 (우상 -> 좌하)
    y = 0
    for i in range(100):
        y += matrix[i][99 - i]
    if y > count:
        count = y
     print(f"#{test_case} {count}")
