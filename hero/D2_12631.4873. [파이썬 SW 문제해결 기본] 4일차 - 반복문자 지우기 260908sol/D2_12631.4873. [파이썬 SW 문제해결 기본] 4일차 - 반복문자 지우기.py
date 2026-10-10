import sys
sys.stdin = open("input.txt", "r")

T = int(input())  # 테스트 케이스 input 받기

for test_case in range(1, T + 1):
    # 일단 input 받기
    # 사실 리스트가 아니라 str로 그대로 input 받아도 아무 문제 없음 ㅇㅇ
    # 아마 그대로 받는게 정배일거임 ㅇㅇ
    list_string = []
    list_string.extend(input())

    # stack 생성하기 오오....
    # 사실 stack을 생성한다해도 이름만 stack이고 리스트임 ㅇㅇ
    # 그냥 사용하기에 따라서 stack이 되기도 하고 queue가 되기도 함 ㅇㅇ
    stack_string = []

    # input 받은 list_string을 가지고 stack에 후입선출의 원리를 통해서
    # 넣으려는 값이 이전에 들어간 값과 같다면 이전 값도 pop으로 쳐내고 다음으로 자연스럽게 넘어가는거임 ㅇㅇ
    # 만약에 다르다면 그 값을 stack에 그대로 쌓아야하므로 else에 append를 통해서 stack 쌓기
    # 이 방법을 통하면 반복문자가 사이에 끼어서 지우지 못했던 짝도 지울 수 있음
    # 이걸 stack의 원리가 아닌 방법으로 풀려면 좀 복잡함 ㅇㅇ
    for i in list_string:
        if stack_string and stack_string[-1] == i:
            stack_string.pop(-1)
        else:
            stack_string.append(i)

    # 쨘~
    print(f'#{test_case} {len(stack_string)}')

#-----------------------------------
#-------- 다른 방법으로 풀이 ---------
#-----------------------------------


T = int(input())  # 테스트 케이스 input 받기

for test_case in range(1, T + 1):
    # 일단 input 받기
    # 사실 리스트가 아니라 str로 그대로 input 받아도 큰 문제 없음 ㅇㅇ
    # 근데 이번에 쓰려는 방법은 str로 받는게 맞는듯 ㅇㅇ
    string = input()
    
    # 이번엔 stack없이 반복분과 인덱싱으로 풀어보고자 함
    # 내가 생각한 원리를 말해보겠음
    # 종료조건이 들어가기 때문에 for문이 아닌 while문이 필수임
    # 특히 i값에 대해서 변동이 계속해서 일어나기 때문에
    # 무조건 순서대로 진행되는 for문은 사용하기 어렵다고 판단했음 ㅇㅇ
    # 암튼 밑에 코드에 설명해봄

    # 이건 while문의 종료조건을 위한 i값
    # 초기값을 0으로 시작함(for문의 range(n)쓰면 0부터 시작하는거처럼 ㅇㅇ)
    i = 0

    # len(string) - 1 인 이유는 2개씩 검사해야하기 때문에 마지막에서 두번째까지만
    # 검사를 하면 되는거고 부등호에 =가 안들어가는 이유는
    # while i < (len(string) - 1):에서 =이 없는 이유는 string[i + 1]까지 보기 때문임
    # 만약에 문자열 길이가 5라면 인덱스는 0, 1, 2, 3, 4인데,
    # string[i] == string[i + 1]에서 이 비교는 i = 3까지만 가능함.
    # string[3] == string[4]  # 가능
    # string[4] == string[5]  # 오류 -> 불가능
    # 그래서 마지막 인덱스 len(string) - 1 바로 전까지만 돌아야 해서 부등호에 =가 안들어감 ㅇㅇ
    while i < (len(string) - 1):
        if string[i] == string[i + 1]:
            string = string[:i] + string[i+2:]

            # 이놈이 생각보다 핵심 기능인데, 지워지고도 그 이전 놈이랑 다시 들어갈 놈이랑
            # 짝이 맞는지 확인해야하기 때문에, 이전 index 값으로 돌리는거임
            # 근데 0이었으면 문제가 생기기 때문에 if로 조건을 준거임 ㅇㅇ
            if i > 0:
                i -= 1

        # 짝이 아니면 다음 index로 넘기기
        else:
            i += 1

    # 쨘~
    print(f'#{test_case} {len(string)}')