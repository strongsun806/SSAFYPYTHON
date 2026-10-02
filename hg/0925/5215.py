# 햄버거 다이어트
# import sys

# sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N, L = map(int, input().split())

    # dp[c] = 칼로리 합이 c일 때 얻을 수 있는 최대 맛 점수
    dp = [0] * (L + 1)

    for _ in range(N):
        score, cal = map(int, input().split())

        # 같은 재료를 중복 선택하지 않도록 뒤에서부터 역순 순회
        for c in range(L, cal - 1, -1):
            if dp[c - cal] + score > dp[c]:
                dp[c] = dp[c - cal] + score

    # L 칼로리 이하에서 얻을 수 있는 최댓값 출력
    print(f"#{tc} {dp[L]}")