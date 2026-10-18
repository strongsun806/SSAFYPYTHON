import sys
sys.stdin = open("D2_1204. [SW 문제해결 기본] 1일차 - 최빈수 구하기/input.txt", "r")

T = int(input()) # 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    tc = int(input()) # 테스트 케이스 번호
    list_num = list(map(int, input().split())) # 0이상 100이하의 숫자 1000개를 리스트에 받기

    # 최빈값을 구하기 위해 0부터 100까지의 숫자가 얼마나 많이 나왔는지 확인하기 위해서 101개의 0값이 담긴 리스트 생성
    choi_bin_list = []
    for i in range(100+1):
        choi_bin_list.append(0)

    # 위에서 만든 101개 원소를 가진 리스트의 인덱스값인 0부터 100은 학생들의 점수분포와 같다.
    # 따라서 순회하며 해당하는 값이 나오면 위의 리스트에 1씩 카운팅을 하면 된다.
    # list_num[i] 자체가 점수이므로 위의 리스트에서 해당하는 인덱스에 +1을 해주는 방식이다.
    # 순회가 끝났을 때, 해당 리스트에서 가장 큰 값을 갖는 인덱스 번호 자체가 출력해야하는 최빈수가 되는 것이다.
    for i in range(1000):
        choi_bin_list[list_num[i]] += 1

    # 순회 완료 -> 최댓값의 인덱스값 찾기
    # 주의) 인덱스값 자체가 출력해야하는 점수기 때문에 정렬을 쓰면 안됨 ㅇㅇ
    num = -1 # 카운팅 제일 많은 놈 찾기위한 비교 숫자
    choi_bin_value = 0 # 인덱스 값, 즉 구하고자 하는 최빈수는 여기에 담아두기
    for i in range(len(choi_bin_list)):
        # '최빈수가 여러 개 일 때에는 가장 큰 점수를 출력하라'는 문구는 >가 아닌 >=를 쓰라는 지시라고 보여짐.
        if choi_bin_list[i] >= num:
            num = choi_bin_list[i]  # 이게 없으면 매번 -1과 비교하기 때문에 최빈수가 100으로 나오는 오류가 생김.
            choi_bin_value = i      # 인덱스값인 i자체가 점수이므로 이 값이 곧 출력할 값임.

    print(f'#{tc} {choi_bin_value}')
