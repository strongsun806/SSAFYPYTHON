import sys
sys.stdin = open("D2_4866. [SW 문제해결 기본] 4일차 - 괄호검사/sample_input.txt", "r")

T = int(input())
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    list_test = list(input())
    cal_condition = 1
    if list_test.count('(') != list_test.count(')'): # stage1: 괄호 개수는 종류에 맞게 짝이 지어지는가
        cal_condition *= 0
    elif list_test.count('{') != list_test.count('}'):
        cal_condition *= 0
    elif list_test.count('[') != list_test.count(']'):
        cal_condition *= 0
    else: # 개수가 서로 딱 맞다면
        cal_condition *= 1 # 사실 else 이 부분은 없어도 될 듯.. 없어도 1 유지일테니
    # 1이라면 stage1 통과
    # 로직 짜고보니 이거 자체가 필요가 없네

    

    list_test.reverse() # 뒤에서 하나씩 꺼내쓰는 pop()을 쓰기 위해서 역순으로 변경
    length_list = range(len(list_test))

    list_only_brackets = []

    num_of_bracket = 0 # 반복문이 돌 때마다 0으로 초기화하면 안 되므로 밖으로 이동

    for i in length_list:
        a = list_test.pop()

        if a in list('(){}[]'):
            
            if a == '(':
                num_of_bracket = 1
                list_only_brackets.append(a)
            elif a == '{':
                num_of_bracket = 2
                list_only_brackets.append(a)
            elif a == '[':
                num_of_bracket = 3
                list_only_brackets.append(a)

                
            elif a == ')':
                if len(list_only_brackets) == 0: # 여는 괄호보다 닫는 괄호가 먼저 나오면
                    cal_condition *= 0
                    break

                num_of_bracket += -1

                if num_of_bracket == 0:
                    list_only_brackets.pop()
                    # 연산해서 0이 되면 삭제 후 남아있는 최근의 여는 괄호로 값을 갱신
                    if len(list_only_brackets) != 0:
                        if list_only_brackets[-1] == '(':
                            num_of_bracket = 1
                        if list_only_brackets[-1] == '{':
                            num_of_bracket = 2                           
                        if list_only_brackets[-1] == '[':
                            num_of_bracket = 3                                     
                    else:
                        num_of_bracket = 0 # 만약에 아직 순회 안끝났는데 리스트가 비는 순간이 오면 다시 0으로 두기
                else: # num_of_bracket != 0
                    cal_condition *= 0 # 괄호 여닫는 순서가 잘못된 경우일듯
                    break
                    
                           
            elif a == '}':
                if len(list_only_brackets) == 0: # 여는 괄호보다 닫는 괄호가 먼저 나오면
                    cal_condition *= 0
                    break

                num_of_bracket += -2

                if num_of_bracket == 0:
                    list_only_brackets.pop()
                    # 연산해서 0이 되면 삭제 후 남아있는 최근의 여는 괄호로 값을 갱신
                    if len(list_only_brackets) != 0:
                        if list_only_brackets[-1] == '(':
                            num_of_bracket = 1
                        if list_only_brackets[-1] == '{':
                            num_of_bracket = 2                           
                        if list_only_brackets[-1] == '[':
                            num_of_bracket = 3                                     
                    else:
                        num_of_bracket = 0 # 만약에 아직 순회 안끝났는데 리스트가 비는 순간이 오면 다시 0으로 두기
                else: # num_of_bracket != 0
                    cal_condition *= 0 # 괄호 여닫는 순서가 잘못된 경우일듯
                    break


            elif a == ']':
                if len(list_only_brackets) == 0: # 여는 괄호보다 닫는 괄호가 먼저 나오면
                    cal_condition *= 0
                    break

                num_of_bracket += -3

                if num_of_bracket == 0:
                    list_only_brackets.pop()
                    # 연산해서 0이 되면 삭제 후 남아있는 최근의 여는 괄호로 값을 갱신
                    if len(list_only_brackets) != 0:
                        if list_only_brackets[-1] == '(':
                            num_of_bracket = 1
                        if list_only_brackets[-1] == '{':
                            num_of_bracket = 2                           
                        if list_only_brackets[-1] == '[':
                            num_of_bracket = 3                                     
                    else:
                        num_of_bracket = 0 # 만약에 아직 순회 안끝났는데 리스트가 비는 순간이 오면 다시 0으로 두기
                else: # num_of_bracket != 0
                    cal_condition *= 0 # 괄호 여닫는 순서가 잘못된 경우일듯
                    break


    if len(list_only_brackets) != 0: # for문을 다 돌았는데 여는 괄호가 남아있다면 잘못된거임
        cal_condition *= 0

    print(f'#{test_case} {cal_condition}')


# ---------------------------------  GPT 풀이  --------------------------------------
    stack = [] # stack이라는 리스트를 만들건데, 후입선출하는 stack의 성질을 이용할거임
    cal_condition = 1

    value = {
        '(': 1, '{': 2, '[': 3,
        ')': -1, '}': -2, ']': -3
    }                               # 일단 dict에 값들 스근하게 넣어주고

    for a in list_test:
        if a in '({[': # 
            stack.append(value[a])

        elif a in ')}]':
            if not stack or stack[-1] + value[a] != 0:
                cal_condition = 0
                break

            stack.pop()

    if stack:
        cal_condition = 0

    print(f'#{test_case} {cal_condition}')