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
 
#파리퇴치
T = int(input())  # 전체 테스트 케이스 수 입력
 
for tc in range(1, T + 1):  # tc를 1부터 T까지 반복하는 반복문으로 먼저 썼음
    N, M = map(int, input().split())  # N: 배열 크기, M: 파리채 크기
    grid = [list(map(int, input().split())) for _ in range(N)]  # N x N 격자판을 입력받아왔음 
    #이 그리드 그리는 건 진짜 자주 나오는 것 같으니까 이거는 외워두는 게 좋을 듯 치트시트도 만들어야겠다
 
    max_flies = 0  # 잡을 수 있는 파리의 최댓값을 저장할 변수
 
    # M x M 파리채가 격자판을 벗어나지 않는 영역만 탐색
    for r in range(N - M + 1):  # 시작 행 인덱스 (0 ~ N-M)
        for c in range(N - M + 1):  # 시작 열 인덱스 (0 ~ N-M)
             
            current_flies = 0  # 현재 (r, c) 위치에서 잡은 파리 수
             
            # (r, c)를 좌상단으로 하는 M x M 영역 내부의 파리 수 합산
            for dr in range(M):
                for dc in range(M):
                    current_flies += grid[r + dr][c + dc]
 
            # 현재 위치의 파리 수가 기존 최댓값보다 많다면 갱신
            if current_flies > max_flies:
                max_flies = current_flies
 
    # 결과 출력 (파이썬 내장 max 함수를 써서 max_flies = max(max_flies, current_flies)로 쓸 수도 있습니다)
    print(f"#{tc} {max_flies}")