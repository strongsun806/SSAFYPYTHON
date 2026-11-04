import sys
sys.stdin = open("D3_1221. [SW 문제해결 기본] 5일차 - GNS/input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    # "ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"
    #   0      1      2      3      4      5      6      7      8      9

    # tc랑 N에 각각 #n이랑 문자열의 개수 N을 input받기
    # N은 int로 써야하므로 일단 str로 같이 받아오고 N만 int() 사용.
    tc, N = map(str, input().split())
    N = int(N)

    # 처리해야하는 값들 리스트에 받아오기.
    list_str_num = list(map(str, input().split()))
    # print(list_str_num)

    # 정렬을 위해서 비교해야하는 값들을 리스트에 담기.
    list_zro_to_nin = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

    # ZRO는 0이므로 인덱스 값과 같게 매칭될 수 있도록 dict에 담기.
    dict_zro_to_nin = {}
    for i, word in enumerate(list_zro_to_nin):
        dict_zro_to_nin[word] = i

    # print(list(dict_zro_to_nin.values())[:10])
    # print(list(dict_zro_to_nin.keys())[:10])
    # print(dict_zro_to_nin)

    # dict_zro_to_nin.get('ZRO')  # 0 이고,
    # list_str_num.sort(key= 는 위의 값 순서대로 아예 정렬을 해버리는거임.
    list_str_num.sort(key=dict_zro_to_nin.get)

    # 그래서 밑에처럼 쓰면 이미 정렬이 되어 리스트 내부 순서가 바뀐채로 정답이 나옴.
    print(f'{tc}\n{" ".join(list_str_num)}')