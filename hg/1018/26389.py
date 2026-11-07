T = int(input())
for tc in range(1, T + 1):
  s = input().strip()

  has_e = 'E' in s
  has_w = 'W' in s
  has_s = 'S' in s
  has_n = 'N' in s

  # 동-서 짝이 맞지 않거나, 남-북 짝이 맞지 않으면 불가능
  if (has_e and not has_w) or (has_w and not has_e) or \
     (has_s and not has_n) or (has_n and not has_s):
    print(f"No")
  else:
    print(f"Yes")