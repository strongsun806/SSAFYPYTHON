# ========================================================
# 문제: 2805_농작물 수확하기
# 난이도: D3
# 작성자: 윤형섭 (1627575)
# 제출 결과: Pass
# 저장 일시: 2026-10-07 11:47:26
# ========================================================

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    all_crop =[]
         for i in range(N):
        all_crop_line=[]
        for char in input():
            all_crop_line.append(int(char))
        all_crop.append(all_crop_line)
    # pprint(all_crop)
    K = N // 2
    count = 0
         for i in range(N): 
        # 중심행으로부터 현재 행이 얼마나 떨어져 있는지 절댓값 계산
        dist = abs(K - i) 
                 #현재 행에서 중심열(K)을 기준으로 좌우로 뻗어나갈 범위
        spread = K - dist 
                 #중심 열의 농작물 더하기
        count += all_crop[i][K]
                 #중심을 기준으로 좌우 대칭 농작물 더하기
        for j in range(1, spread + 1):
            count += (all_crop[i][K - j]+all_crop[i][K + j])
                              print(f"#{test_case} {count}")
