T = int(input())
for tc in range(1, T + 1):
  A, B, C, D = map(int, input().split())

  # 겹치는 구간의 시작과 끝을 먼저 계산을 해준드아
  start = max(A, C)
  end = min(B, D)

  # 겹치는 시간 계산 (0보다 작아지면 겹치지 않는 것이므로 0으로 처리)
  overlap = max(0, end - start)

  print(f"#{tc} {overlap}")