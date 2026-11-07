import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())          # 한 단어의 글자 수
    S = input().strip()      # 해독해야 하는 암호문

    result = ""

    # 암호문을 앞에서부터 한 글자씩 확인
    for i in range(len(S)):

        # 알파벳을 숫자로 변환
        # A = 0, B = 1, C = 2, Z = 25
        num = ord(S[i]) - ord('A')

        # 리스트의 인덱스는 0부터 시작하지만
        # 문제에서 문자의 위치는 1부터 시작한다.
        # 따라서 현재 문자의 위치는 i + 1이다.
        position = i + 1

        # 홀수 번째 문자는 오른쪽으로 이동
        # 1번째는 1칸
        # 3번째는 3칸
        # 5번째는 5칸
        if position % 2 == 1:
            num = (num + position) % 26

        # 짝수 번째 문자는 왼쪽으로 이동
        # 2번째는 2칸
        # 4번째는 4칸
        # 6번째는 6칸
        else:
            num = (num - position) % 26

        # 나머지를 이용하면 알파벳 범위를 넘어가도
        # 다시 A부터 Z 사이의 값으로 돌아오게 할 수 있다.
        #
        # 계산이 끝난 숫자를 다시 알파벳으로 변환한다.
        result += chr(num + ord('A'))

    # result에는 공백이 없는 원래 문장이 저장되어 있다.
    # 예를 들어 YOUCANWIN과 같은 형태이다.

    answer = ""

    # 해독된 문자열을 N글자씩 자른다.
    # N이 3이라면 0, 3, 6과 같은 위치에서 시작한다.
    for i in range(0, len(result), N):

        # 첫 번째 단어가 아니라면 앞에 공백을 추가한다.
        if answer:
            answer += " "

        # 현재 위치부터 N글자를 잘라서 추가한다.
        # 예를 들어 N이 3이고 YOUCANWIN이라면
        # YOU, CAN, WIN으로 나누어진다.
        answer += result[i:i + N]

    # 테스트 케이스 번호와 해독된 문장을 출력
    print(f"#{test_case} {answer}")
