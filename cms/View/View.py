import sys
sys.stdin = open("sample_input.txt", "r")

# 테스트 케이스 10개
for test_case in range(1, 11):

    # 빌딩 개수 = building_count
    building_count = int(input())
    # 각 빌딩 높이 리스트 = height
    height = list(map(int,input().split()))
    # 조망권 개수 = count
    count = 0

    # 맨 양옆 두 건물을 제외하고 순서대로 건물 선택
    for sel in range(2,len(height)-2) :

        # 가장 높은 건물의 높이 = num_max
        num_max = 0

        # 반복문 : 선택한 건물의 좌우 2개 건물 높이 비교 -> num_max 갱신
        for check in [-2,-1,1,2]:
            if height[sel+check] > num_max :
                num_max = height[sel+check]

        # 주변 가장 높은 건물보다 크면 선택한 건물의 높이와 비교하여 그 차이만큼 조망권 개수 추가
        if height[sel] > num_max :
            count += height[sel] - num_max

    print(f"#{test_case} {count}")
