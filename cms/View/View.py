import sys
sys.stdin = open("sample_input.txt", "r")

for test_case in range(1, 11):
    building_count = int(input())
    height = list(map(int,input().split()))
    count = 0
    for sel in range(2,len(height)-2) :
        num_max = 0
        for check in [-2,-1,1,2]:
            if height[sel+check] > num_max :
                num_max = height[sel+check]
        if height[sel] > num_max :
            count += height[sel] - num_max

    print(f"#{test_case} {count}")
