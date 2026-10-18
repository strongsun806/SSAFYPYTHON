import sys
sys.stdin = open("D2_12592.4865. [파이썬 SW 문제해결 기본] 3일차 - 글자수/input.txt", "r")

T = int(input())  # 테스트 케이스 수 input

for test_case in range(1, T + 1):
    # 문제가 악질인게, str1 str2 이러면서 list로 받을 생각을 못하게 함 ㅇㅇ
    # 이거 그대로 input 받지말고 list에 담아서 관리하면 훨씬 편함 ㅇㅇ
    list_str1 = list(map(str,input()))
    list_str2 = list(map(str,input()))

    # 문제에서는 가장 많은 글자의 셈을 한 결과를 출력하라고 했음
    # 따라서 정답이 되는 max_count를 만들고 임시로 쓸 카운트인 count_1을 for문 사이에 둠
    max_count = 0
    for i in list_str1:
        count_1 = 0
        for j in list_str2:
            if i == j:
                count_1 += 1
                if count_1 >= max_count:
                    max_count = count_1

    print(f'#{test_case} {max_count}')