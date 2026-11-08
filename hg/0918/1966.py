# 1966. 숫자를 정렬하자

# import sys

# sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    
    # 선택 정렬: i번째 자리에 들어갈 최솟값을 찾아 swap
    for i in range(N - 1):
        min_idx = i
        for j in range(i + 1, N):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
        
    print(f"#{tc}", *nums)