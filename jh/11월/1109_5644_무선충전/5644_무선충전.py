import sys
sys.stdin = open('sample_input.txt')

def check(user_x, user_y, charger):
    avilable = [-1]   
    for i in range(len(charger)):
        x, y, coverage, power = charger[i]
        distance = abs(x - user_x) + abs(y - user_y)
        if distance <= coverage:
            avilable.append(i)
    return avilable

T = int(input())
move = [(0, 0), (0, -1), (1, 0), (0, 1), (-1, 0)]
for tc in range(1, T+1):
    M, A = map(int, input().split())
    command_A = list(map(int, input().split()))
    command_B = list(map(int, input().split()))
    command_A.insert(0, 0)
    command_B.insert(0, 0)
    start_A = (0, 0)
    start_B = (9, 9)
    charger= []
    total = 0
    for _ in range(A):
        x, y, coverage, power = map(int, input().split())
        x -= 1
        y -= 1
        charger.append((x, y, coverage, power))

    for t in range(M+1):
        direction_A = command_A[t]
        dx, dy = move[direction_A]
        ax, ay = start_A
        start_A = (ax+dx, ay+dy)
        direction_B = command_B[t]
        dx, dy = move[direction_B]
        bx, by = start_B
        start_B = (bx+dx, by+dy)
        availabe_A = check(start_A[0], start_A[1], charger)
        availabe_B = check(start_B[0], start_B[1], charger)

        best = 0
        for a in availabe_A:
            for b in availabe_B:
                if a == -1 and b == -1:
                    current = 0
                elif a == -1:
                    current = charger[b][3]
                elif b == -1:
                    current = charger[a][3]
                elif a == b:
                    current = charger[a][3]
                else:
                    current = charger[a][3] + charger[b][3]
                if current > best:
                    best = current
        total += best

    print(f'#{tc} {total}')

    


    
