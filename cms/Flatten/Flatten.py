import sys
sys.stdin = open("input.txt", "r")

# 테스트 케이스 10개 만큼 반복
for test_case in range(1,11):
    # 옮기는 작업 횟수 = dump
    dump = int(input())
    # 박스의 높이 리스트 box_list
    box_list = list(map(int, input().split()))
    # 박스 높이 별 갯수를 할당할 count리스트 생성, 편의를 위해 0~101까지의 인덱스를 가짐
    count = [0]*101
    # 가로길이 = 100 만큼 반복
    for i in range(100):
        # 박스 높이를 인덱스로하여 count리스트의 값 + 1
        count[box_list[i]] += 1

    # 박스의 최소 높이 = 1이므로 min_idx = 1로 초기화
    min_idx = 1
    # count 리스트에서 min_idx 인덱스의 값이 0이면 그 높이를 가진 열이 없다는 뜻이므로, 진짜 가장 낮은 높이의 인덱스를 찾을 때 까지 min_idx를 +1 하도록 반복
    while count[min_idx] == 0 :
        min_idx += 1

    # count 리스트에서 max_idx 값이 0이면 그 높이를 가진 열이 없다는 뜻이므로, 진짜 가장 높은 높이의 인덱스를 찾을 때 까지 max_idx를 -1 하도록 반복
    max_idx = 100
    while count[max_idx] == 0 :
        max_idx -= 1

    # dump 횟수 만큼 반복
    for do in range(dump):
        # 만약 가장 높은 열과 가장 낮은 열의 차이가 1이 되면 반복문 종료
        if min_idx + 1 == max_idx:
            break

        # 가장 낮은 높이의 갯수를 count에서 찾아서 -1 (상자를 쌓으면 더이상 가장 낮은 열이 아니게 되므로)
        count[min_idx] -= 1
        # 가장 낮은 높이의 열의 높이가 1 늘어남으로 min_idx + 1 의 갯수가 1 늘어남
        count[min_idx+1] += 1
        # 가장 높은 높이의 갯수를 count에서 찾아서 -1 (상자를 옮기면 더이상 가장 높은 열이 아니게 되므로)
        count[max_idx] -= 1
        # 가장 높은 높이의 열의 높이가 1 줄어듦으로 max_idx - 1 의 갯수가 1 늘어남
        count[max_idx-1] += 1

        # 상자 옮기기가 끝난 후, min_idx와 max_idx의 값이 0이면 더이상 min_idx, max_idx가 아니므로 재할당
        if count[min_idx] == 0 :
            min_idx += 1
        if count[max_idx] == 0 :
            max_idx -= 1
            
    print(f"#{test_case} {max_idx - min_idx}")