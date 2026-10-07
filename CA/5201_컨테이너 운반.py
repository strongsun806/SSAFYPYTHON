# ========================================================
# 문제: 13066_5201. [파이썬 S/W 문제해결 구현] 3일차 - 컨테이너 운반
# 난이도: D3
# 작성자: 윤형섭 (1627575)
# 제출 결과: Pass
# 저장 일시: 2026-10-07 11:28:34
# ========================================================

t = int(input())
 def load(weight_list,truck_list):
    count=0
    w_idx = len(weight_list) - 1
    t_idx = len(truck_list) - 1
         while w_idx >= 0 and t_idx >= 0:
        if weight_list[w_idx] > truck_list[t_idx]:
            w_idx -= 1
        else:
            count += weight_list[w_idx]
            w_idx -= 1
            t_idx -= 1
    return count
 for tc in range(1,t+1):
    n,m = map(int,input().split())
    weight_list=(sorted((map(int,input().split()))))
    truck_list=(sorted((map(int,input().split()))))
         print(f"#{tc}",load(weight_list,truck_list))
