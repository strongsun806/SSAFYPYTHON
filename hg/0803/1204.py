#1204 최빈수 구하기

def solve():
  T_case = int(input())

  for _ in range(1, T_case + 1):
    tc = input().strip()  # 테스트 케이스 번호
    scores = list(map(int, input().split()))  # 1000명의 점수

    # 점수별 빈도수 계산
    counts = [0] * 101
    for s in scores:
      counts[s] += 1

    max_freq = 0
    ans_score = 0

    for score in range(101):
      if counts[score] >= max_freq:
        max_freq = counts[score]
        ans_score = score

    print(f"#{tc} {ans_score}")


if __name__ == "__main__":
  solve()