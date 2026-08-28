# D2 백만 장자 프로젝트
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




'''
아래의 구문은 input.txt 를 read only 형식으로 연 후,
앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.
따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
아래 구문을 사용하기 위해서는 import sys가 필요합니다.
단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
#import sys
#sys.stdin = open("input.txt", "r")

# 테스트 케이스 개수 T 입력받기
T = int(input())

# T번만큼 반복하기
for test_case in range(1, T + 1):
    # 날짜 수 N 입력받기
    N = int(input())
    
    # 각 날의 매매가를 리스트로 입력받기
    prices = list(map(int, input().split()))
    
    max_profit = 0  # 총 이익을 저장할 변수
    max_price = 0   # 지금까지의 최대 판매가
    
    # 앞에서부터 생각하면 어려우니까
    # 가장 마지막 날인 젤 뒤부터 거꾸로 확인하도록 함수 짰어용
    for i in range(N - 1, -1, -1):
        price = prices[i]
        
        # 만약 오늘 가격이 젤 비싼 가격보다 크면
        if price > max_price:
            max_price = price  # 최고가를 오늘 가격으로 
        else:
            # 아니면
            # 오늘 사서 제일 비싼 날(max_price)에 팔면 댐
            max_profit += (max_price - price)
            
    # 정답 출력하기
    print(f"#{test_case} {max_profit}")