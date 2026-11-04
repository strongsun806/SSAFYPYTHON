import sys
sys.stdin = open("D2_2001. 파리 퇴치/input.txt", "r")

T = int(input())  # 테스트 케이스 개수 input 받기
  
for test_case in range(1, T + 1):
    N, M = map(int, input().split())  # N은 5이상 15이하, M은 2이상 N이하
  
    # 2차원 matrix 만들기
    matrix_fly = []
    for i in range(N):
        row = []
        row.extend(map(int, input().split()))
        matrix_fly.append(row)
  
    # for row in matrix_fly:
    #     print(row)
  
    what_is_max_value = 0
    for i in range(N - M + 1):     # 이렇게 해야 파리채의 왼쪽 위 기준으로 했을때 오른쪽이 삐져나가지 않음 ㅇㅇ
        for j in range(N- M + 1):  # 밑에 기준으로 따졌을 때, 얘도 마찬가지임 ㅇㅇ
  
            sum_kill_fucking_fly = 0       # 이 위치에 둬야 파리채 위치가 바뀔 때 초기화되면서 다시 계산에 사용할 수 있음 ㅇㅇ
            for a in range(M):
                for b in range(M):
                    sum_kill_fucking_fly += matrix_fly[i + a][j + b]
  
            # for문 다 돌았으면 이제 초기화 전에 그 값을 사용해야해서 여기에 뒀음
            # max 값을 갱신하는 조건문임 ㅇㅇ
            if sum_kill_fucking_fly > what_is_max_value:
                what_is_max_value = sum_kill_fucking_fly
  
    print(f'#{test_case} {what_is_max_value}')