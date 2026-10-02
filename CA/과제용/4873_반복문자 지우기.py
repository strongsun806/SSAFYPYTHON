# Problem: 12631_4873. [파이썬 S/W 문제해결 기본] 4일차 - 반복문자 지우기
# Author: 윤형섭_1627575 (Pass)
# Saved by Aura for Boss 💋

t = int(input())
 for tc in range(1, t + 1):
    listed = list(input().strip())
         i = 0
    while i < len(listed) - 1:
                 if listed[i] == listed[i + 1]:
            listed.pop(i + 1)
            listed.pop(i)
                                      if i > 0:
                i -= 1
        else:
                         i += 1
                 print(f"#{tc} {len(listed)}")
