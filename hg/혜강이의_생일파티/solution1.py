import sys
from itertools import combinations

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    idx = 1
    
    for tc in range(1, T + 1):
        N = int(input_data[idx])
        M = int(input_data[idx + 1])
        idx += 2
        
        zeros = []
        ones = []
        for r in range(N):
            for c in range(N):
                val = int(input_data[idx])
                idx += 1
                if val == 0:
                    zeros.append((r, c))
                else:
                    ones.append((r, c))
                    
        # 초를 꽂을 빈 칸이 7개 미만이면 바로 불가능
        if len(zeros) < 7:
            print(f"#{tc} -1")
            continue
            
        all_zeros = set(zeros)
        all_ones = set(ones)
        
        # 각 빈 칸에 초를 꽂았을 때 도달하는 칸들의 좌표 모음 (set)
        long_cover = []
        short_cover = []
        for r, c in zeros:
            # 긴 초 (거리 M 이하)
            l_set = {(zr, zc) for zr in range(N) for zc in range(N) if abs(r - zr) + abs(c - zc) <= M}
            # 짧은 초 (거리 1 이하)
            s_set = {(zr, zc) for zr in range(N) for zc in range(N) if abs(r - zr) + abs(c - zc) <= 1}
            long_cover.append(l_set)
            short_cover.append(s_set)
            
        min_melt = float('inf')
        cand_indices = list(range(len(zeros)))
        
        # 1. 긴 초 2개 고르기
        for l1, l2 in combinations(cand_indices, 2):
            base_reach = long_cover[l1] | long_cover[l2]
            
            # 남은 자리 중 짧은 초 5개 고르기
            rem = [x for x in cand_indices if x != l1 and x != l2]
            for s_comb in combinations(rem, 5):
                # 7개 초의 도달 범위 모두 합치기
                total_reach = base_reach.copy()
                for s in s_comb:
                    total_reach |= short_cover[s]
                    
                # 케이크의 모든 빈 칸(0)이 밝혀졌는지 확인
                if all_zeros.issubset(total_reach):
                    # 닿아서 녹은 초콜릿(1) 개수 카운트
                    melt_cnt = len(all_ones & total_reach)
                    if melt_cnt < min_melt:
                        min_melt = melt_cnt
                        if min_melt == 0:
                            break
            if min_melt == 0:
                break
                
        ans = min_melt if min_melt != float('inf') else -1
        print(f"#{tc} {ans}")

if __name__ == '__main__':
    solve()