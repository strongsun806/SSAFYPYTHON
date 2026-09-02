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
sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    '''

        이 부분에 여러분의 알고리즘 구현이 들어갑니다.

    '''
    # ///////////////////////////////////////////////////////////////////////////////////
    N, X = map(int, input().split())
    
    box = [list(map(int, input().split())) for _ in range(N)]
    
    # 전체 가능한 수
    total = 2*N
    # total = 0
    # 행 체크, 각 행의 마지막은 기준점으로 안잡아도됨 기준에서 다음 요소를 비교 높이 차이 계산
    for i in range(N):
        for j in range(N - 1):
            # 높이가 2 이상 차이나는 경우 제거
            if box[i][j] - box[i][j+1] >= 2 or box[i][j] - box[i][j+1] <= -2:
                total -=1
                break
            # # 높이가 높아지는 경우 이전의 길이가 x만큼 있는지 확인 후 제거
            # land = 0
            # if box[i][j] - box[i][j+1] == -1:
            #     for k in range(X):
            #         if 0 <= j-k < N - 1 and  box[i][j-k] == box[i][j]:
            #             land += 1
            #     if land < X :
            #         total -=1
            # 높이가 낮아지는 경우 이후의 길이가 x만큼 있는지 확인 후 제거
            elif box[i][j] - box[i][j+1] == 1:
                land = 0
                for k in range(X):
                    if 0 <= j+k+1 < N and box[i][j+k+1] == box[i][j+1]:
                        land += 1
                if land < X :
                    total -=1
                    break
            # 높이가 올라가는 경우, 높이가 낮아졌다가 올라가는 경우 경사로 2개 필요 2X만큼의 평지 필요 후 제거
            elif box[i][j] - box[i][j+1] == -1:
                land = 0
                back = 1
                # 경사로가 시작점 밖으로 나가는 경우
                if j-X+1 < 0:
                    total -=1
                    break
                is_na = False
                while j-back >= 0:
                    land +=1
                    # 기준점으로 뒤로 가면서 비교 : 높아지거나 -1, 낮아지거나 1
                    if box[i][j] - box[i][j-back] == 1:
                        if land < X :
                            total -=1
                            is_na = True
                            break
                    if box[i][j] - box[i][j-back] == -1:
                        if land < 2*X :
                            total -=1
                            is_na = True
                            break
                    back +=1
                if is_na == True:
                    break
    # 열 체크
    for i in range(N):
        for j in range(N - 1):
            # 높이가 2 이상 차이나는 경우 제거
            if box[j][i] - box[j+1][i] >= 2 or box[j][i] - box[j+1][i] <= -2:
                total -=1
                break
            # 높이가 높아지는 경우 이전의 길이가 x만큼 있는지 확인 후 제거
            # elif box[j][i] - box[j][i+1] == -1:
            #     land = 0
            #     for k in range(X):
            #         if 0 <= i-k < N and  box[j][i-k] == box[j][i]:
            #             land += 1
            #     if land < X :
            #         total -=1
            # 높이가 낮아지는 경우 이후의 길이가 x만큼 있는지 확인 후 제거
            elif box[j][i] - box[j+1][i] == 1:
                land = 0
                for k in range(X):
                    if 0 <= j+k+1 < N and box[j+k+1][i] == box[j+1][i]:
                        land += 1
                if land < X :
                    total -=1
                    break
            # 높이 가 올라가는 경우
            elif box[j][i] - box[j+1][i] == -1:
                land = 0
                back = 1
                # 경사로가 시작점 밖으로 나가는 경우
                if j-X+1 < 0:
                    total -=1
                    break
                # 기준점으로 뒤로 가면서 비교 : 높아지거나 -1, 낮아지거나 1
                while j-back >= 0:
                    land +=1
                    is_na = False
                    if box[j][i] - box[j-back][i] == 1:
                        if land < X :
                            total -=1
                            is_na = True
                            break
                    if box[j][i] - box[j-back][i] == -1:
                        if land < 2*X :
                            total -=1
                            is_na = True
                            break
                    back +=1
                if is_na == True:
                    break
    print(f'#{test_case} {total}')