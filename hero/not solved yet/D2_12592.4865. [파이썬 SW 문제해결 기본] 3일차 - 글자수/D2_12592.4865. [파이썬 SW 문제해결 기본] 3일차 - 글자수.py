import sys
sys.stdin = open("D2_12592.4865. [파이썬 SW 문제해결 기본] 3일차 - 글자수/input.txt", "r")

T = int(input())  # 테스트 케이스 수 input

for test_case in range(1, T + 1):
    # input을 두 번 받으면서 str1과 str2에 각각 할당하기.
    # type은 str로 나옴.
    str1 = input()
    str2 = input()

    # set를 만들어서 받은 input값을 쪼개서 한글자씩 넣게되는데, set 특성상 겹치는 글자는 사라짐.
    # -> 어떤 글자가 있는지 종류를 알 수 있음 ㅇㅇ.
    set1 = set(str1)
    set2 = set(str2)

    