import sys
sys.stdin = open("sample_input.txt", "r")

# 테스트 개수 T개 
T = int(input())

# 테스트 개수 만큼 반복
for test_case in range(1, T + 1) :

    # 양수 개수 = length
    length = int(input())
    # 양수 리스트 = num_list
    num_list = list(map(int, input().split()))
    # 최소값 num_min과 최대값 num_max을 num_list[0]으로 초기화
    num_min = num_list[0]
    num_max = num_list[0]

    # num_min과 num_max를 num_list[0]로 초기화 했으므로 num_list[1]부터 비교
    for i in range(1,len(num_list)) :
        # 인덱스 i의 값 = num
        num = num_list[i]
        # num이 num_max보다 크면 num_max값을 num값으로 재할당
        if num > num_max :
            num_max = num
        # num_max를 재할당하지 않았을 경우 num_min보다 작은지 비교
        elif num < num_min:
            num_min = num

    print(f"#{test_case} {num_max-num_min}")