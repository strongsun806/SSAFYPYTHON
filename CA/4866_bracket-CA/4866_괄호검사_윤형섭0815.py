import sys

sys.stdin = open("input.txt", "r")

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