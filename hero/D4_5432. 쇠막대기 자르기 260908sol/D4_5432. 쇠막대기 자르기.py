import sys
sys.stdin = open("input.txt", "r")

T = int(input())  # 테스트 케이스 input 받기

for test_case in range(1, T + 1):
    # 레이저()가 나왔을 때, 앞에 끝나지 않은 열린 괄호의 개수만큼 조각이 생김.
    # 주의해야할 점은 레이저()에 있는 열린괄호를 잘못 셀 수 있다는 것인데, 이건 내가 볼 때
    # 열린 괄호를 + 1로, 닫힌 괄호를 - 1로 두고 순회하면서 계속 더해주면 레이저가 나왔을 때(레이저 닫힌괄호까지 순회하고 ㅇㅇ)
    # counting 된 숫자를 누적 합을 해주면 될 거 같음 ㅇㅇ
    # 물론 강의에서는 stack을 이용해서 후입선출을 이용했음 ㅇㅇ
    # 그건 했다치고 내 맘대로 해볼거임 ㅇㅇ

    # 일단 input을 받되, 리스트에 extend로 받아서 한번에 쪼개버림 ㅋㅋ
    list_bracket = []
    list_bracket.extend(input())
    
    # 리스트 안에서 여는 괄호를 + 1, 닫는 괄호를 - 1로 두고 순회하면서 계산하기
    # 그리고 닫는 괄호가 나왔을 때, 그 직전에 여는 괄호가 나왔다면 그건 레이저라는 것이므로
    # 닫는 괄호의 - 1 까지 계산을 끝내고 누적된 값을 누적합에 더해주기
    # 이러면 조각 수가 세짐 ㅇㅇ
    
    accumulated_count = 0
    count_1 = 0
    for i in range(len(list_bracket)):
        if list_bracket[i] == '(':
            count_1 += 1
        else:  # list_bracket[i] == ')' 일 때
            count_1 -= 1
            if list_bracket[i-1] == '(':
                accumulated_count += count_1
            else:  # 레이저의 닫힌 괄호가 아니라, 그냥 쇠막대기의 끄트머리 표현일 때
                   # 위쪽에서 한건 쇠막대기 앞쪽을 보고 계산을 한 것이고 자르고 마지막에 남은 조각도 계산을 해줘야한다.
                   # 근데 어차피 남은 조각은 하나씩 카운팅 하면 되기 때문에 아래와 같이 쓰면 됨 ㅇㅇ
                accumulated_count += 1

    print(f'#{test_case} {accumulated_count}')