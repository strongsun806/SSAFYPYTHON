import sys
sys.stdin = open("input.txt", "r")

T = int(input())  # 테스트 케이스 input

for test_case in range(1, T + 1):
    # 문제에서는 마치 가로로 주고, 세로로 읽으라는 식으로 아주 악랄하게 말했지만
    # 사실 애초에 세로로 받으면 그만인 문제라고 생각했음 ㅇㅇ..
    # 

    # input 받아야하는 5줄의 값을 한 번에 할당하기.
    a, b, c, d, e= map(list, [input(), input(), input(), input(), input()])

    # 가장 긴 길이만큼 순회할것이기 때문에 미리 구해두기.
    list_1 = [a, b, c, d, e]
    max_length = 0
    for i in list_1:
        if len(i) >= max_length:
            max_length = len(i)

    # 좀 꼼수같긴한데, try except를 이용해서 세로로 받으면서 문제생기면 그냥 넘기라고 오더 내렸음 ㅋㅋ
    result = []
    for i in range(max_length):
        for j in list_1:
            try:
                result.append(j[i])
            except:
                continue

    print(f'#{test_case} {"".join(result)}')