# ========================================================
# 문제: 4866_[S/W 문제해결 기본] 4일차 - 괄호검사
# 난이도: D2
# 작성자: 윤형섭 (1627575)
# 제출 결과: Pass
# 저장 일시: 2026-10-07 11:47:10
# ========================================================

T = int(input())
for test_case in range(1, T + 1):
  sentense = str(input())
   # 1. pure에 괄호만 넣기
  pure = []
  for i in sentense:
    if i in "(){}":
      pure += [i]
   stack = []
   for char in pure:
         if char == "(" or char == "{":
      stack.append(char)
          elif char == ")":
      if not stack or stack.pop() != "(":
        print(f"#{test_case} 0")
        break
    elif char == "}":
      if not stack or stack.pop() != "{":
        print(f"#{test_case} 0")
        break
  else:
         if stack:
      print(f"#{test_case} 0")
    else:
      print(f"#{test_case} 1")
