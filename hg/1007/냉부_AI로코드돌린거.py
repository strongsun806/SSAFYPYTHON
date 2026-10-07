# 6가지 요리별 소모 재료: [MILK, TOMATO, EGG, ONION, CARROT, KIMCHI, RICE, PASTA]
RECIPES = [
    (0, 1, 2, 1, 0, 0, 2, 0),  # 0: 오므라이스
    (2, 0, 0, 1, 0, 0, 0, 2),  # 1: 크림파스타
    (1, 2, 0, 0, 0, 0, 0, 2),  # 2: 토마토크림파스타
    (0, 0, 2, 1, 1, 0, 2, 0),  # 3: 계란볶음밥
    (0, 0, 1, 0, 0, 2, 2, 0),  # 4: 김치볶음밥
    (0, 0, 0, 1, 1, 1, 0, 2),  # 5: 김치파스타
]

# 각 길이(0~5)에 대해 6가지 요리의 사용 횟수 조합과 총 재료 소모량을 사전 계산
COMBOS = {}
for length in range(6):
    comb_list = []
    
    def gen_comb(r_idx, remaining, cur_counts):
        if r_idx == 5:
            cur_counts.append(remaining)
            # 총 소모량 계산
            cost = [0] * 8
            for i in range(6):
                cnt = cur_counts[i]
                if cnt > 0:
                    for k in range(8):
                        cost[k] += RECIPES[i][k] * cnt
            comb_list.append(cost)
            cur_counts.pop()
            return
        
        for c in range(remaining + 1):
            cur_counts.append(c)
            gen_comb(r_idx + 1, remaining - c, cur_counts)
            cur_counts.pop()

    gen_comb(0, length, [])
    COMBOS[length] = comb_list

def solve():
    try:
        raw = input()
        while not raw.strip():
            raw = input()
        T = int(raw.strip())
    except:
        return

    for tc in range(1, T + 1):
        line = input().strip()
        while not line:
            line = input().strip()
        N = int(line)

        inv_line = input().strip()
        while not inv_line:
            inv_line = input().strip()
        init_inv = list(map(int, inv_line.split()))

        # N에 맞춰 구간 정의: (구간 일수, 만료되는 재료 인덱스, 폐기 여부)
        # MILK: 0, TOMATO: 1, EGG: 2, ONION: 3
        intervals = []
        
        # 1구간: 1~5일 (MILK 만료)
        len1 = min(5, N)
        intervals.append((len1, 0, N >= 5))
        
        # 2구간: 6~8일 (TOMATO 만료)
        if N > 5:
            len2 = min(3, N - 5)
            intervals.append((len2, 1, N >= 8))
            
        # 3구간: 9~12일 (EGG 만료)
        if N > 8:
            len3 = min(4, N - 8)
            intervals.append((len3, 2, N >= 12))
            
        # 4구간: 13~15일 (ONION 만료)
        if N > 12:
            len4 = min(3, N - 12)
            intervals.append((len4, 3, N >= 15))

        ans = float('inf')
        num_intervals = len(intervals)

        def search(stage, cur_waste, inv):
            nonlocal ans
            if cur_waste >= ans:
                return

            if stage == num_intervals:
                ans = min(ans, cur_waste)
                return

            length, exp_item, will_expire = intervals[stage]
            comb_list = COMBOS[length]

            for cost in comb_list:
                # 재료 소모 가능 여부 확인
                if (inv[0] < cost[0] or inv[1] < cost[1] or inv[2] < cost[2] or 
                    inv[3] < cost[3] or inv[4] < cost[4] or inv[5] < cost[5] or 
                    inv[6] < cost[6] or inv[7] < cost[7]):
                    continue

                # 차감 후 폐기 계산
                next_inv = [inv[k] - cost[k] for k in range(8)]
                waste = 0
                if will_expire:
                    waste = next_inv[exp_item]
                    next_inv[exp_item] = 0

                search(stage + 1, cur_waste + waste, next_inv)

        search(0, 0, init_inv)
        print(f"#{tc} {ans}")

if __name__ == '__main__':
    solve()