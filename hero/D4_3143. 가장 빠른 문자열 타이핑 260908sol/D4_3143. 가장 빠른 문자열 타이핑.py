import sys
sys.stdin = open("input.txt", "r")

T = int(input())  # 테스트 케이스 input 받기

for test_case in range(1, T + 1):
    # A라는 문자열 안에 B가 몇 번 들어있는지 찾아야함.
    # 단, B가 발견되면 그 문자열 덩어리 전체를 하나의 글자로 바꾼다고 생각하면 됨 ㅇㅇ
    # 그래서 B를 찾은 경우에는 B의 길이만큼 인덱스를 넘겨야,
    # 이미 사용한 B를 다시 세는 일이 없음.
    A, B = map(str, input().split())

    # 현재 A에서 어디를 보고 있는지 나타내는 인덱스
    count_i = 0

    # A 안에서 B를 찾은 횟수
    count_B = 0

    # B 길이만큼 잘라서 비교할 수 있는 마지막 위치까지만 반복하면 됨.
    # 예를 들어 A 길이가 10이고 B 길이가 3이면,
    # 시작 위치가 7일 때까지는 3글자를 잘라서 비교 가능함 ㅇㅇ
    while count_i <= len(A) - len(B):
        # 현재 위치부터 B 길이만큼 잘랐을 때 B와 같다면,
        # 즉 A 안에서 B 하나를 찾았다면
        if A[count_i:count_i + len(B)] == B:
            count_B += 1

            # 찾은 B는 이제 하나의 글자로 바뀔 거니까,
            # 방금 찾은 B의 길이만큼 다음 위치로 바로 넘어감 ㅇㅇ
            count_i += len(B)

        # B가 아니라면 현재 위치에서는 만들 수 없다는 뜻이므로
        # 한 칸만 옆으로 가서 다시 확인하면 됨
        else:
            count_i += 1

    # 원래 A의 전체 길이에서 찾은 B들의 원래 길이를 빼고,
    # B 하나당 최종적으로 글자 하나가 남으므로 찾은 횟수만큼 다시 더해줌.
    result = len(A) - (len(B) * count_B) + count_B
          #  'B를 사용하고 남은 문자열 개수' 'B 사용 횟수'

    # 컷
    print(f'#{test_case} {result}')