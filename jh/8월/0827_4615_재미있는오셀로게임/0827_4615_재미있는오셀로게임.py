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
import sys
sys.stdin = open("input1.txt", "r")
from pprint import pprint
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    # 판의 크기와 돌을 두는 횟수
    N, M = map(int, input().split())
    # 기본 틀 생성
    box = [[0]*N for _ in range(N)]
    box[N//2][N//2] = 2
    box[N//2-1][N//2-1] = 2
    box[N//2-1][N//2] = 1
    box[N//2][N//2-1] = 1
    for m in range(M):
        I , J , K = map(int, input().split())
        I = I - 1
        J = J - 1
        box[I][J] = K
        # 8방향 탐색
        # 좌상단
        a = 1
        while I - a >= 0 and J - a >= 0:
            if box[I-a][J-a] == 0:
                break
            elif box[I-a][J-a] != K:
                box[I-a][J-a] = K
            elif box[I-a][J-a] == K:
                break
            a += 1
        # 상단
        a = 1
        while I - a >= 0:
            if box[I-a][J] == 0:
                break
            elif box[I-a][J] != K:
                box[I-a][J] = K
            elif box[I-a][J] == K:
                break
            a += 1
        # 우상단
        a = 1
        while I - a >= 0 and J + a < N:
            if box[I-a][J+a] == 0:
                break
            elif box[I-a][J+a] != K:
                box[I-a][J+a] = K
            elif box[I-a][J+a] == K:
                break
            a += 1
        # 좌측
        a = 1
        while J - a >= 0:
            if box[I][J-a] == 0:
                break
            elif box[I][J-a] != K:
                box[I][J-a] = K
            elif box[I][J-a] == K:
                break
            a += 1
        # 우측
        a = 1
        while J + a < N:
            if box[I][J+a] == 0:
                break
            elif box[I][J+a] != K:
                box[I][J+a] = K
            elif box[I][J+a] == K:
                break
            a += 1
        # 좌하단
        a = 1
        while I + a < N and J - a >= 0:
            if box[I+a][J-a] == 0:
                break
            elif box[I+a][J-a] != K:
                box[I+a][J-a] = K
            elif box[I+a][J-a] == K:
                break
            a += 1
        # 하단
        a = 1
        while I + a < N:
            if box[I+a][J] == 0:
                break
            elif box[I+a][J] != K:
                box[I+a][J] = K
            elif box[I+a][J] == K:
                break
            a += 1
        # 우하단
        a = 1
        while I + a < N and J + a < N:
            if box[I+a][J+a] == 0:
                break
            elif box[I+a][J+a] != K:
                box[I+a][J+a] = K
            elif box[I+a][J+a] == K:
                break
            a += 1
        pprint(box, width=40)
    cnt_1=0
    cnt_2=0
    for i in range(N):
        for j in range(N):
            if box[i][j] == 1:
                cnt_1 +=1
            elif box[i][j] == 2:
                cnt_2 +=1
    print(f'#{test_case} {cnt_1} {cnt_2}')







    #     # 좌상단
    #     a = 1
    #     while I - a >= 0 and J - a >= 0:
    #         if box[I-a][J-a] == 0:
    #             break
    #         if box[I-a][J-a] != K:
    #             box[I-a][J-a] = K
    #         elif box[I-a][J-a] == K:
    #             break
    #         a += 1

    #     # 상단
    #     a = 1
    #     while I - a >= 0:
    #         if box[I-a][J] == 0:
    #             break
    #         if box[I-a][J] != K:
    #             box[I-a][J] = K
    #         elif box[I-a][J] == K:
    #             break
    #         a += 1
 
    #     # 우상단
    #     a = 1
    #     while I - a >= 0 and J + a < N:
    #         if box[I-a][J+a] == 0:
    #             break
    #         if box[I-a][J+a] != K:
    #             box[I-a][J+a] = K
    #         elif box[I-a][J+a] == K:
    #             break
    #         a += 1
 
    #     # 좌측
    #     a = 1
    #     while J - a >= 0:
    #         if box[I][J-a] == 0:
    #             break
    #         if box[I][J-a] != K:
    #             box[I][J-a] = K
    #         elif box[I][J-a] == K:
    #             break
    #         a += 1
 
    #     # 우측
    #     a = 1
    #     while J + a < N:
    #         if box[I][J+a] == 0:
    #             break
    #         if box[I][J+a] != K:
    #             box[I][J+a] = K
    #         elif box[I][J+a] == K:
    #             break
    #         a += 1
 
    #     # 좌하단
    #     a = 1
    #     while I + a < N and J - a >= 0:
    #         if box[I+a][J-a] == 0:
    #             break
    #         if box[I+a][J-a] != K:
    #             box[I+a][J-a] = K
    #         elif box[I+a][J-a] == K:
    #             break
    #         a += 1
 
    #     # 하단
    #     a = 1
    #     while I + a < N:
    #         if box[I+a][J] == 0:
    #             break
    #         if box[I+a][J] != K:
    #             box[I+a][J] = K
    #         elif box[I+a][J] == K:
    #             break
    #         a += 1
 
    #     # 우하단
    #     a = 1
    #     while I + a < N and J + a < N:
    #         if box[I+a][J+a] == 0:
    #             break
    #         if box[I+a][J+a] != K:
    #             box[I+a][J+a] = K
    #         elif box[I+a][J+a] == K:
    #             break
    #         a += 1
    #     pprint(box, width=20)
    # cnt_1=0
    # cnt_2=0
    # for i in range(N):
    #     for j in range(N):
    #         if box[i][j] == 1:
    #             cnt_1 +=1
    #         else:
    #             cnt_2 +=1
    # print(cnt_1, cnt_2)