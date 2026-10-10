import sys
sys.stdin = open("input.txt", "r")


def who_is_winner(index_p1, index_p2):  # p1이 번호가 더 작은 쪽이 되도록 하기
    # index_p1, index_p2에는 가위바위보 값 자체가 아니라 "학생 번호(index)"가 들어옴
    # ex) index_p1 = 2라면 2번 학생이 뭘 냈는지는 list_srp[2]로 확인

    # 비겼을 때는 편의상 번호가 더 작은쪽이 이기도록함
    if list_srp[index_p1] == list_srp[index_p2]:
        return index_p1

    # p1이 이기는 경우를 if문안에 두고 return index_p1 하기
    # 1: 가위, 2: 바위, 3: 보
    # 가위(1)는 보(3)를 이기고, 바위(2)는 가위(1)를 이기고, 보(3)는 바위(2)를 이김
    if (list_srp[index_p1] == 1 and list_srp[index_p2] == 3) or \
        (list_srp[index_p1] == 2 and list_srp[index_p2] == 1) or \
        (list_srp[index_p1] == 3 and list_srp[index_p2] == 2):
        return index_p1

    # 나머지 경우는 p2가 이기는 경우이므로 return index_p2 하기
    else:
        return index_p2
    

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    list_srp = list(map(int, input().split()))
    
    list_srp.insert(0, 0) 
    # 또는 이걸 빼고 맨 밑에서 print(tournament_srp(0, N - 1) + 1) 을 해야함
    # -> 우리가 input 받은 값들은 index 0번부터 N-1번까지 저장되지만,
    #    문제에서는 1번부터 N번까지라고 명시했기 때문
    # -> 앞에 의미없는 0 하나를 추가해서 "(학생 번호) == (list의 index)"로 맞춰준거임
    #    후자의 방법을 택한다면, "(실제 학생 번호) == (우리가 계산에 쓴 해당 학생의 index) + 1"이므로 마지막에 1을 더해줌


    #====================== 재귀사용법 ==========================

    # def recursive(현재문제):

    #     # 1. 종료 조건
    #     if 가장_작은_문제:
    #         return 가장_작은_문제의_답

    #     # 2. 문제를 더 작게 만들어서 재귀
    #     작은문제의_답 = recursive(더_작은_문제)

    #     # 3. 작은 문제의 답을 이용해서 현재 문제의 답 만들기
    #     현재문제의_답 = 작은문제의_답을_이용한_계산

    #     # 4. 현재 문제의 답을 위로 돌려주기
    #     return 현재문제의_답

    #===========================================================
    

    # i번 학생부터 j번 학생까지 중에서 최종 승자의 번호(index)를 return하는 함수
    # ex) tournament_srp(1, 4) -> 1~4번 학생끼리 대결시킨 후 최종 승자 번호를 return
    def tournament_srp(i, j):

        # 1. 종료 조건
        # 그룹을 계속 반으로 나누다가 i와 j가 같아졌다면 그 그룹에는 학생이 딱 1명만 남은거임
        # 혼자 있으면 당연히 그 학생이 그 그룹의 승자니까 자기 번호를 그대로 return
        if i == j:
            return i

        # 현재 그룹을 왼쪽 그룹 / 오른쪽 그룹으로 나누기 위한 가운데 index
        # ex) i=1, j=4라면 index_mid=2 -> [1, 2] / [3, 4]로 나뉨
        index_mid = (i + j) // 2

        # 2. 문제를 더 작게 만들어서 재귀
        # 왼쪽 그룹의 최종 승자가 누군지는 재귀한테 맡기기
        # 계속 반으로 쪼개다가 i == j가 되면 return을 시작하고,
        # 그 return값들을 이용해서 대결하면서 다시 위로 올라오게 됨
        winner_left = tournament_srp(i, index_mid)

        # 오른쪽 그룹도 똑같이 재귀를 돌려서 오른쪽 그룹의 최종 승자 번호 받아오기
        winner_right = tournament_srp(index_mid + 1, j)

        # 3, 4. 작은 문제의 답을 이용해서 현재 문제의 답 만들고 return
        # 여기까지 왔다는건 왼쪽 그룹 승자와 오른쪽 그룹 승자를 둘 다 알아냈다는 뜻
        # 둘을 who_is_winner에 넣어서 대결시키고, 이긴 사람의 번호를 현재 그룹의 승자로 return
        return who_is_winner(winner_left, winner_right)

    # 처음에는 1번부터 N번까지 전체 학생을 하나의 그룹으로 넣고 시작
    # 재귀를 통해 그룹을 계속 쪼갠 다음, 각 그룹의 승자를 위로 올리면서 최종 1명의 번호가 return됨
    print(f'#{test_case} {tournament_srp(1, N)}')