# [문제] 쇠막대기 자르기 (SWEA 5432)
# 괄호 표현으로 쇠막대기와 레이저가 주어집니다.
# 1) 레이저는 여는 괄호와 닫는 괄호의 연속 '()'로 표현됩니다.
# 2) 쇠막대기의 시작은 '(', 끝은 ')'로 표현됩니다.
# 레이저로 잘려진 모든 쇠막대기 조각들의 총 개수를 구하는 알고리즘입니다.

import sys , pprint
sys.stdin=open("input4.txt","r")

# 테스트 케이스 개수 t 입력
t = int(input())
for tc in range(1,t+1):
    # 괄호 문자열을 문자 단위 리스트로 변환
    listed= list(input())
    # print(listed)
    count=0
    i=0
    real=[]
    
    # [1단계: 괄호 문자열을 의미별 숫자 코드로 변환]
    # 0: 쇠막대기 시작 '('
    # 1: 쇠막대기 끝 ')'
    # 2: 레이저 '()'
    while i!=len(listed):
        # 바로 다음 괄호와 합쳐져 '()' 형태인 경우 -> 레이저
        if listed[i] =='('and listed[i+1]==')':
            i+=1         # 닫는 괄호까지 함께 처리하기 위해 인덱스 1 추가 이동
            real+=[2]    # 2는 레이저
        # 단독으로 나오는 여는 괄호 '(' -> 쇠막대기의 시작
        elif listed[i]=='(': # 열기는 0
            real+=[0]
        # 단독으로 나오는 닫는 괄호 ')' -> 쇠막대기의 끝
        else:
            real+=[1]    # 닫기는 1
        i+=1
    # print(real)
    
    # [2단계: 토큰화된 리스트를 순회하며 잘린 조각 개수 계산]
    result = 0  # 총 쇠막대기 조각 수
    count = 0   # 현재 겹쳐져 있는(열려 있는) 쇠막대기의 개수
    i = 0
    end = True
    while end:
        try:
            # 쇠막대기 시작(0)인 경우: 현재 겹친 막대기 수 1 증가
            if real[i] == 0:
                count += 1
            # 쇠막대기 끝(1)인 경우: 막대기가 끝나므로 count 1 감소, 마지막 남은 꼬리 조각 1개 추가
            elif real[i] == 1:
                count -= 1
                result += 1
            # 레이저(2)인 경우: 레이저가 발사되면 현재 겹쳐있는 막대기들이 모두 잘리므로 count만큼 조각 추가
            else:
                result += count
        # 리스트의 모든 요소를 검사하여 인덱스를 벗어나면 종료
        except IndexError:
            end = False
        i += 1
    # 테스트 케이스 번호와 총 조각 수 출력
    print(f'#{tc}',result)

