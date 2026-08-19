import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    test_case=int(input())
    arr = list(map(int, input().split()))
    arr_dict ={}
    for num in arr :
        arr_dict[num] = arr_dict.get(num, 0) + 1
    first_key = next(iter(arr_dict))
    max_value = arr_dict[first_key]
    for key, value in arr_dict.items():
        if value > max_value:
            max_key = key
            max_value = value

    result = max_key


    print(f"#{test_case} {result}")

    # ///////////////////////////////////////////////////////////////////////////////////
