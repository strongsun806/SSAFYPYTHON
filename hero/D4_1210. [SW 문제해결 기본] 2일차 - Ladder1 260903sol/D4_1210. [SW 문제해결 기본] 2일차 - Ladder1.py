import sys
sys.stdin = open("D4_1210. [SW 문제해결 기본] 2일차 - Ladder1/input.txt", "r")

T = 10  # 테스트 케이스는 10개라고 주어짐
 
for test_case in range(1, T+1):
    tc = int(input())  # 테스트 케이스 번호
# 내가 봤을 땐 핵심 로직을 크게 둘로 나누는게 나을거같음
# 1. 왼쪽이나 오른쪽에 1이 나타날때까지 위로 쭉 올라가는 로직(while 쓰면 좋을 듯)
# 2. 왼쪽 또는 오른쪽으로 돌아서 쭉 진행하고 다시 위로 도는 로직(이것도 while 쓰면 좋을듯)
# 이게 맞나 모르겠는데, 위/왼/오른쪽 각각에 대해서 전진하는 것을 따로 구현하되,
# 대신에 전진하다가 막히거나, 길이 나오거나와 같은 이슈가 생기면 방향 전환은 똑같이 하는 느낌으로 구현해보고싶음.
# 위쪽 방향일 때, 전진: 행 값에 -1
# 왼쪽 방향일 때, 전진: 열 값에 -1
# 오른쪽 방향일 때, 전진: 열 값에 +1
# 자세한건 밑에서 설명해보겠음 ㅇㅇ
 
# 가장 바깥 반복문은 while이 눈에 들어옴
# 어차피 사다리타기는 해당하는 end점에서부터 위로 올라가는 것이 가장 빠른 찾기임
# 따라서 while문에서 row의 index값이 0일 때의 column의 index값이 출력해야하는 값이 될거임
 
    matrix_ladder = []
    for i in range(100):
        matrix_ladder.append(list(map(int, input().split())))
 
    # 위에서 만들고 내용을 넣은 matrix 안에서 시작점인 2의 index 찾기
    start_index = []
    # 어차피 맨 밑줄에 있을테니까 굳이 2중 for문을 쓰지 않아도 됨
    for j in range(100):
        if matrix_ladder[99][j] == 2:
            start_index.extend([99, j])
            break
 
    # 위쪽 행이 0이 될 때까지 무한 반복
    # 일단 시작할 때는 현재 index가 start index가 됨
    current_index = start_index  # [99, j]
    result = -1  # 반복문이 끝났을 때 열 index 값을 결과로 받을 변수. 열 값은 range(0, 100)이므로 초기값을 -1로 설정
    while current_index[0] > 0:  # current_index는 index 0에 행 index를 받고, index 1에 열 index를 받기 때문
                                 # >= 0을 하면 반복문이 한 번 더 실행되면서 행 값이 -1이 될 수도 있음
         
        # 맨 왼쪽(0)에서 더 왼쪽 검사하면 터지니까 인덱스 경계 체크부터 박고 시작함
        if current_index[1] - 1 >= 0 and matrix_ladder[current_index[0]][current_index[1] - 1] == 1:  # 현재 위치의 왼쪽에 길이 있을 때.
            # 안쪽 반복문도 돌다가 벽 뚫고 나가면 안 되니까 경계 조건 똑같이 묶어줌
            while current_index[1] - 1 >= 0 and matrix_ladder[current_index[0]][current_index[1] - 1] == 1:  # 왼쪽 가로줄이 끝날 때까지 반복문 돌리기
                current_index[1] += -1  # 왼쪽으로 열 인덱스 한 칸씩 땡김
            current_index[0] += -1  # 좌로 전진 다 끝났으니까 위로 한 칸 올려서 왔던 길 다시 안 돌아가게 탈출시킴
 
        # 맨 오른쪽(99)에서 더 오른쪽 검사하면 index out of range 나니까 여기도 경계 체크 필수임
        elif current_index[1] + 1 < 100 and matrix_ladder[current_index[0]][current_index[1] + 1] == 1:  # 현재 위치의 오른쪽에 길이 있을 때.
            # 여기도 마찬가지로 가로줄 끝까지 가다가 벽에 박아서 터지는 거 막으려고 조건 추가함
            while current_index[1] + 1 < 100 and matrix_ladder[current_index[0]][current_index[1] + 1] == 1:  # 오른쪽 가로줄이 끝날 때까지 반복문 돌리기
                current_index[1] += +1  # 오른쪽으로 열 인덱스 한 칸씩 밀어줌
            current_index[0] += -1  # 우로 전진 다 끝났으니까 여기도 똑같이 위로 한 칸 올려서 무한루프 방지함
 
        else:  # 왼쪽 오른쪽 다 길이 없을 때.
            current_index[0] += -1  # 양옆에 길 없으면 그냥 묻지도 따지지도 않고 위로 한 칸 전진
 
        # 반복마다 그때의 열 index 값을 할당하고 while문 종료 시의 값을 출력하면 됨.
        result = current_index[1]
 
    print(f'#{tc} {result}')