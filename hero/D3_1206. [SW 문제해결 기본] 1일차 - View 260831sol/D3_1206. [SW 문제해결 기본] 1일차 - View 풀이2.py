import sys
sys.stdin = open("input.txt", "r")

T = 10 # 문제에서 테스트 케이스 10개라고 주어짐

for test_case in range(1, T + 1):
    N = int(input()) # 건물개수 input받기

    # 건물 높이에 대한 input값을 받아서 리스트에 넣기
    list_building_height = []
    list_building_height.extend(map(int, input().split()))
    # print(list_building_height)

    # 인덱스 양 끝 2개를 뗀 범위에서 주변 2칸 내에서 본인이 가장 크다면,
    # 2번째로 큰놈보다 얼마나 큰지가 곧 몇칸이 확보되는지와 같다.
    count_result = 0
    for i in range(2, len(list_building_height)-2):
        list_for_compare = [list_building_height[i-2], list_building_height[i-1], list_building_height[i], list_building_height[i+1], list_building_height[i+2]]
        list_for_compare.sort(reverse=True)
        if list_for_compare[0] == list_building_height[i]:
            count_result += list_building_height[i] - list_for_compare[1]
    print(f'#{test_case} {count_result}')

