import sys
sys.stdin = open("sample_input.txt", "r")

# 테스트 케이스 갯수 = T
T = int(input())
for test_case in range(1, T+1):
    # 0~9까지 숫자를 인덱스로, 갯수를 값으로 가지는 counts 리스트
    counts = [0]*10
    # 카드 갯수 = N
    N = int(input())
    # 숫자카드가 붙어있는 숫자 = nums
    nums = int(input())

    # 붙어있는 숫자의 길이 N만큼 반복
    for i in range(N):
        # 각 1의 자리 값을 counts 리스트의 인덱스로 하여 그 값을 +1
        counts[nums % 10] += 1
        # 그 후 1의 자리 값을 제거
        nums //= 10

    # 가장 많은 숫자 h_num을 0, 0의 갯수를 h_count로 할당하여 초기화
    h_num = 0
    h_count = counts[0]

    # 숫자 1~9까지를 반복하여 counts 리스트에서 그 숫자의 갯수를 확인하고 그 값이 가장 크면 h_num을 그 숫자로, h_count를 그 숫자의 갯수로 재할당
    for j in range(1,10):
        if counts[j] >= h_count :
            h_num = j
            h_count = counts[j]

    print(f"#{test_case} {h_num} {h_count}")