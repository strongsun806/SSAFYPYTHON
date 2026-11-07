# 음식별 소모량: MILK, TOMATO, EGG, ONION, CARROT, KIMCHI, RICE, PASTA
RECIPES = [
    (0, 1, 2, 1, 0, 0, 2, 0),  # 오므라이스
    (2, 0, 0, 1, 0, 0, 0, 2),  # 크림파스타
    (1, 2, 0, 0, 0, 0, 0, 2),  # 토마토크림파스타
    (0, 0, 2, 1, 1, 0, 2, 0),  # 계란볶음밥
    (0, 0, 1, 0, 0, 2, 2, 0),  # 김치볶음밥
    (0, 0, 0, 1, 1, 1, 0, 2),  # 김치파스타
]

def dfs(day, current_waste):
    global ans, N, inv
    
    if current_waste >= ans:
        return
        
    if day > N:
        ans = min(ans, current_waste)
        return

    for recipe in RECIPES:
        # 재료 먼저 체크하기
        if (inv[0] < recipe[0] or inv[1] < recipe[1] or inv[2] < recipe[2] or 
            inv[3] < recipe[3] or inv[4] < recipe[4] or inv[5] < recipe[5] or 
            inv[6] < recipe[6] or inv[7] < recipe[7]):
            continue

        # 재료 사용해서 차감하기
        for i in range(8):
            inv[i] -= recipe[i]

        # 유통기한 만료 처리
        added_waste = 0
        temp_saved = 0
        
        if day == 5 and N >= 5:
            added_waste = inv[0]
            temp_saved = inv[0]
            inv[0] = 0
        elif day == 8 and N >= 8:
            added_waste = inv[1]
            temp_saved = inv[1]
            inv[1] = 0
        elif day == 12 and N >= 12:
            added_waste = inv[2]
            temp_saved = inv[2]
            inv[2] = 0
        elif day == 15 and N >= 15:
            added_waste = inv[3]
            temp_saved = inv[3]
            inv[3] = 0

        # 다음 날 어떻게 됐는지 탐색
        dfs(day + 1, current_waste + added_waste)

        # 백트래킹
        if day == 5 and N >= 5:
            inv[0] = temp_saved
        elif day == 8 and N >= 8:
            inv[1] = temp_saved
        elif day == 12 and N >= 12:
            inv[2] = temp_saved
        elif day == 15 and N >= 15:
            inv[3] = temp_saved

        for i in range(8):
            inv[i] += recipe[i]

T = int(input())
for tc in range(1, T + 1):
    line = input().strip()
    while not line:
        line = input().strip()
    N = int(line)
    
    inv_line = input().strip()
    while not inv_line:
        inv_line = input().strip()
    inv = list(map(int, inv_line.split()))
    
    ans = 999999999
    dfs(1, 0)
    print(f"#{tc} {ans}")