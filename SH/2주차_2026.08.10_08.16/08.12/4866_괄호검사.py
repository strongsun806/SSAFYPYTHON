"""
풀이 구상
빈 리스트를 만들어서 괄호만 넣을 수 있도록 구성
닫는 괄호가 나왔을 때 짝이 된다면 리스트 마지막에 여느 괄호가 있게되기 때문에 그것을 확인
만약 아니라면 결과값을 0으로 설정
"""

import sys
sys.stdin = open("sample_input.txt", "r")


T = int(input())

for test_case in range(1, T + 1):
    text = input()

    # 괄호만 넣을 빈 리스트 생성
    stack = []
    # 정상인 경우를 기본값으로 설정
    result = 1

    for char in text:
        # 반복문을 활용해 하나씩 확인하다가 여는 소괄호, 중괄호일 경우 stack리스트에 추가
        if char == '(' or char == '{':
            stack.append(char)

        # 만약 닫는 소괄호라면 stack리스트가 비어있거나 마지막 인덱스가 여는 소괄호가 아니라면 결과값을 0으로 변경 후 break
        elif char == ')':
            if not stack or stack[-1] != '(':
                result = 0
                break
            # 만약 닫는 소괄호라면 여는 소괄호를 stack리스트에서 제거
            stack.pop()

        # 만약 닫는 중괄호라면 stack리스트가 비어있거나 마지막 인덱스가 닫는 소괄호가 아니라면 결과값을 0으로 변경 후 break
        elif char == '}':
            if not stack or stack[-1] != '{':
                result = 0
                break
            # 만약 닫는 중괄호라면 여는 중괄호를 stack리스트에서 제거
            stack.pop()

    # pop 함수를 사용해서 제거했기 때문에 짝이 맞다면 stack리스트가 비어있어야 정상 아니라면 비정상
    if stack:
        result = 0

    print(f"#{test_case} {result}")