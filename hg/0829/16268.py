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
# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
# 여러 개의 테스트 케이스를 순서대로 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    # 1. N(행), M(열) 입력
    N, M = map(int, input().split())
    
    # 2. NxM 풍선 격자판 입력
    grid = [list(map(int, input().split())) for _ in range(N)]
    
    # 상, 하, 좌, 우 델타 배열
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    max_flower = 0  # 최대 꽃가루 수를 저장할 변수
    
    # 3. 모든 좌표 (r, c)를 순회하며 확인
    for r in range(N):
        for c in range(M):
            # 현재 터뜨린 위치의 꽃가루 수로 초기화
            current_sum = grid[r][c]
            
            # 4. 상하좌우 딱 1칸씩만 확인 (step 필요 없음)
            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                
                # 격자판 범위 내에 있을 때만 더하기
                if 0 <= nr < N and 0 <= nc < M:
                    current_sum += grid[nr][nc]
            
            # 5. 최댓값 갱신
            if current_sum > max_flower:
                max_flower = current_sum
                
    # 6. 양식에 맞게 출력
    print(f"#{test_case} {max_flower}")
    # ///////////////////////////////////////////////////////////////////////////////////