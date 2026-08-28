# 4366. 정식이의 은행 업무

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

# import sys


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

T = int(input())

for test_case in range(1, T + 1):
    bin_str = input()  # 2진수 글자 (예: '1010')
    tri_str = input()  # 3진수 글자 (예: '212')
    
    # 2진수에서 한 자리 바꿔서 만든 10진수 숫자들 넣어둘 리스트 먼저
    bin_numbers = []
    

    # 1. 2진수에서 한 자릿수만 틀리게 만들어보기

    for i in range(len(bin_str)):
        
        # 글자 하나만 바꾼 새로운 2진수 글자 만들기
        new_bin = ""
        for j in range(len(bin_str)):
            if i == j:
                # 바꿀 위치라면: 0은 1로, 1은 0으로 뒤집기
                if bin_str[j] == '0':
                    new_bin = new_bin + '1'
                else:
                    new_bin = new_bin + '0'
            else:
                # 안 바꿀 위치는 원래 글자 그대로 붙이기
                new_bin = new_bin + bin_str[j]
        
        # 만든 2진수를 직접 10진수 숫자로 계산하기 
        num = 0
        for char in new_bin:
            num = num * 2 + int(char)  # 2씩 곱하면서 더하면 10진수가 된다는 사실을 알아냇다...
            
        bin_numbers.append(num)  # 후보 리스트에 저장했습ㄴ다
        

    # 2. 3진수에서 한 자릿수만 틀리게 만들어보기

    answer = 0
    
    for i in range(len(tri_str)):
        # 3진수는 각 자리에 '0', '1', '2' 가 들어갈 수 있음
        for change_char in ['0', '1', '2']:
            
            # 원래 있던 글자랑 다른 글자로만 바꾸기
            if tri_str[i] != change_char:
                
                new_tri = ""
                for j in range(len(tri_str)):
                    if i == j:
                        new_tri = new_tri + change_char  # 글자 교체
                    else:
                        new_tri = new_tri + tri_str[j]  # 그대로 붙이기
                
                # 만든 3진수를 직접 10진수 숫자로 계산
                num = 0
                for char in new_tri:
                    num = num * 3 + int(char)  # 3씩 곱하면서 더하기
                
                # 방금 만든 숫자가 아까 2진수로 만들어둔 후보에 있는지 확인해주기
                if num in bin_numbers:
                    answer = num
                    break
                    
        if answer != 0:
            break
            
    # 정답 출력
    print(f"#{test_case} {answer}")