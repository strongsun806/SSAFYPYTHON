import sys
sys.stdin = open("./sample_in.txt", "r")

"""
문제 구상
흰색과 검은색 돌이 있음
한줄로 이루어진 게임판에 흰돌과 검은돌이 일렬로 되어있음
하나의 돌을 선택하는데
선택한 돌을 두고 마주보는 돌들에 대해
마주보는 돌들이 서로 같은 색이면 선택한 돌과 같은 색으로 바꾸고
마주보는 돌들이 서로 다른 색이면 그대로 둔다.

"""

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    game_board = list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())

        center = i - 1

        for d in range(1, j + 1):
            left = center - d
            right = center + d

            if 0 <= left < N and 0 <= right < N:
                if game_board[left] == game_board[right]:
                    game_board[left] = 1-game_board[left]
                    game_board[right] = 1-game_board[right]


    print(f"#{test_case}", end=' ')
    print(*game_board)
                



# i 번째 돌을 사이에 두고 마주보는 j개의 돌에 대해, 각각 같은 색이면 뒤집고,
# 다른색이면 그대로 둔다. 주어진 돌을 벗어나는 경우 뒤집기는 중지된다.

# 2 번째 돌을 사이에 두고 마주보는 2개의 돌에 대해, 각각 같은 색이면 뒤집고,
# 다른색이면 그대로 둔다. 주어진 돌을 벗어나는 경우 뒤집기는 중지된다.

# 2 번째 돌을 사이에 두고 마주보는 3개의 돌에 대해, 각각 같은 색이면 뒤집고,
# 다른색이면 그대로 둔다. 주어진 돌을 벗어나는 경우 뒤집기는 중지된다.