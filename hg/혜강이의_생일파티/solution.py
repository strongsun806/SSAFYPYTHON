import sys
from itertools import combinations

def solve():
    # 파일 리다이렉션 또는 표준 입력 모두 처리 가능
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    T = int(input_data[0])
    idx = 1
    out = []
    
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
        
        K = len(zeros)
        C = len(ones)
        
        # 초를 꽂을 빈 칸(0)이 7개 미만이면 조건을 만족할 수 없음
        if K < 7:
            out.append(f"#{tc} -1")
            continue
            
        target_zeros = (1 << K) - 1
        
        # 전처리: 각 빈 칸에 긴 초/짧은 초를 꽂을 때
        # 커버되는 0들의 위치와 닿게 되는 1(초콜릿)들의 위치를 비트마스킹
        l_zero = [0] * K
        l_one = [0] * K
        s_zero = [0] * K
        s_one = [0] * K
        
        for i, (r, c) in enumerate(zeros):
            for j, (zr, zc) in enumerate(zeros):
                dist = abs(r - zr) + abs(c - zc)
                if dist <= M:
                    l_zero[i] |= (1 << j)
                if dist <= 1:
                    s_zero[i] |= (1 << j)
            for j, (or_, oc) in enumerate(ones):
                dist = abs(r - or_) + abs(c - oc)
                if dist <= M:
                    l_one[i] |= (1 << j)
                if dist <= 1:
                    s_one[i] |= (1 << j)
                    
        min_melt = float('inf')
        all_indices = list(range(K))
        
        # 1. 긴 초 2개 선택 (조합)
        for l1, l2 in combinations(all_indices, 2):
            base_z = l_zero[l1] | l_zero[l2]
            base_o = l_one[l1] | l_one[l2]
            
            # 남은 후보 자리들
            rem_candidates = [x for x in all_indices if x != l1 and x != l2]
            
            # 2. 짧은 초 5개 선택 (조합)
            for s_comb in combinations(rem_candidates, 5):
                cur_z = base_z
                for s in s_comb:
                    cur_z |= s_zero[s]
                
                # 모든 빈 칸(0)이 최소 한 번 이상 밝혀진 경우에만 체크
                if cur_z == target_zeros:
                    cur_o = base_o
                    for s in s_comb:
                        cur_o |= s_one[s]
                    
                    # 닿은 초콜릿(1) 개수 카운트
                    melt_cnt = bin(cur_o).count('1')
                    if melt_cnt < min_melt:
                        min_melt = melt_cnt
                        if min_melt == 0:  # 0개면 이미 최솟값이므로 더 볼 필요 없음
                            break
            if min_melt == 0:
                break
                
        ans = min_melt if min_melt != float('inf') else -1
        out.append(f"#{tc} {ans}")
        
    print('\n'.join(out))

if __name__ == '__main__':
    solve()