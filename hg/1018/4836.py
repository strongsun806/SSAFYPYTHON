# 색칠하기 문제풀이

T = int(input())
for tc in range(1, T + 1):
  N = int(input())

  # 10x10 격자 초기화
  grid = [[0] * 10 for _ in range(10)]

  for _ in range(N):
    r1, c1, r2, c2, color = map(int, input().split())

    # 주어진 영역에 색상 칠하기
    for r in range(r1, r2 + 1):
      for c in range(c1, c2 + 1):
        grid[r][c] += color  # 빨강(1) 또는 파랑(2)을 더함

  # 보라색(값 3)이 된 칸의 개수 카운트
  purple_count = 0
  for r in range(10):
    for c in range(10):
      if grid[r][c] == 3:
        purple_count += 1

  print(f"#{tc} {purple_count}")