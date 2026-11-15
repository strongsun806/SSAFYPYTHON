# 로컬에서 파일로 테스트할 때만 사용
import sys
sys.stdin = open('sample_input.txt')


def check(user_x, user_y, charger):
    # -1: 충전기를 선택하지 않는 경우
    available = [-1]

    for i in range(len(charger)):
        x, y, coverage, power = charger[i]

        distance = abs(x - user_x) + abs(y - user_y)

        if distance <= coverage:
            available.append(i)

    return available


T = int(input())

# (x, y) 기준: 정지, 상, 우, 하, 좌
move = [(0, 0), (0, -1), (1, 0), (0, 1), (-1, 0)]

for tc in range(1, T + 1):
    M, A = map(int, input().split())

    command_A = list(map(int, input().split()))
    command_B = list(map(int, input().split()))

    # 0초에는 이동하지 않고 초기 위치에서 충전
    command_A.insert(0, 0)
    command_B.insert(0, 0)

    start_A = (0, 0)
    start_B = (9, 9)

    charger = []
    total = 0

    for _ in range(A):
        x, y, coverage, power = map(int, input().split())

        # 좌표를 0~9 기준으로 변환
        x -= 1
        y -= 1

        charger.append((x, y, coverage, power))

    # 0초부터 M초까지 총 M+1번 충전
    for t in range(M + 1):
        # 사용자 A 이동
        direction_A = command_A[t]
        dx, dy = move[direction_A]

        ax, ay = start_A
        start_A = (ax + dx, ay + dy)

        # 사용자 B 이동
        direction_B = command_B[t]
        dx, dy = move[direction_B]

        bx, by = start_B
        start_B = (bx + dx, by + dy)

        # 각 사용자가 접속 가능한 충전기 목록
        available_A = check(start_A[0], start_A[1], charger)
        available_B = check(start_B[0], start_B[1], charger)

        best = 0

        # 모든 충전기 선택 조합 확인
        for a in available_A:
            for b in available_B:
                if a == -1 and b == -1:
                    current = 0

                elif a == -1:
                    current = charger[b][3]

                elif b == -1:
                    current = charger[a][3]

                elif a == b:
                    # 같은 충전기를 공유하므로 합은 성능 한 번
                    current = charger[a][3]

                else:
                    # 서로 다른 충전기 사용
                    current = charger[a][3] + charger[b][3]

                if current > best:
                    best = current

        total += best

    print(f"#{tc} {total}")