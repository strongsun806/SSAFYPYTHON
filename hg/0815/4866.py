# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''

#import sys


'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
#sys.stdin = open("input.txt", "r")

T = int(input()) # 테스트 케이스 개수 입력받음

for tc in range(1, T + 1):
    line = input() # 한 줄 통째로 받아오기
    stack = [] # 괄호 담아둘 리스트(스택으로 해뒀음)
    result = 1 # 일단 성공(1)이라고 기본값 정해둠

    for char in line:
        # 열린 괄호 들어오면 일단 스택에 넣음 
        if char == '{' or char == '(':
            stack.append(char)
        
        # 닫는 중괄호 } 만났을 때
        elif char == '}':
            # 아직 열린 괄호가 남아있고, 그게 { 일 때만 제대로 된 짝으로 인식
            if stack and stack[-1] == '{':
                stack.pop() # 짝 찾았으니까 털어내고
            else:
                result = 0 # 짝 안 맞거나 열린 적도 없으면 탈락
                break
                
        # 닫는 소괄호 ) 만났을 때
        elif char == ')':
            # 남아있는 마지막 괄호가 ( 인지 확인하기... 
            if stack and stack[-1] == '(':
                stack.pop() # 꺼내주깅
            else:
                result = 0 # 실패했으면 브레이크
                break

    # 다 돌았는데도 스택에 남아있는 열린 괄호가 있으면 짝 안 맞은 거임
    if stack:
        result = 0

    print(f"#{tc} {result}")