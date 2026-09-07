import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    string = []  # 입력 값을 받을 리스트
    result = 1  # 기본 값 = 정상
    for i in str(input()):  # 문자열을 하나씩 판별하는 for문
        if i in '{([':  # 여는 괄호 일 때,
            string.append(i)  #string에 추가
        elif i in '})]':  #닫는 괄호 일 때,
            if not string :  # string에 여는 괄호가 없으면 제대로 된 짝을 이룰 수 없으므로 result = 0
                result = 0
                break  # 여기서 result = 0 이면 뒤에는 확인할 필요가 없으므로 break
            elif i == '}' and string[-1]=='{':  # 닫는 괄호의 종류 별로, string의 가장 마지막 index의 열린 괄호와 짝이 맞는 지 판별,
                string.pop()  # 짝이 맞으면 pop하고 진행
            elif i == ']' and string[-1]=='[':
                string.pop()
            elif i == ')' and string[-1]=='(':
                string.pop()
            else :
                result = 0  # 짝이 안 맞으면 result = 0
                break   
    if len(string) > 0:  #최종적으로 여는 괄호와 닫는 괄호의 갯수가 다르면 result = 0
        result = 0   
    print(f'#{test_case} {result}')





