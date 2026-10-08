
# [문제] 가장 빠른 문자열 타이핑
# 문자열 A를 타이핑할 때, 특정 단어 B를 단축키처럼 1번만 눌러서 입력할 수 있다면
# 전체 문자열 A를 완성하기 위해 키를 눌러야 하는 '최소 타이핑 횟수'를 구하는 알고리즘입니다.

import sys
sys.stdin = open("input1.txt", "r")

def answer(listed):
    # 단축키 B가 전체 문자열 A 안에서 몇 번이나 온전히 쓰일 수 있는지 세는 변수
    answer=0
    
    # 전체 문자열 A(listed[0])를 처음부터 끝까지 한 글자씩 확인합니다.
    for i in range(len(listed[0])):
            # 현재 글자가 단축키 B(listed[1])의 첫 글자와 같다면, 단어 B가 시작되는지 검사합니다.
            if listed[0][i]== listed[1][0]:
                result =0  # B의 글자들과 연속해서 몇 개나 일치하는지 세는 카운터
                
                # 단축키 B의 길이만큼 한 글자씩 비교합니다.
                for j in range(len(listed[1])):
                    # A의 (i + j)번째 글자와 B의 j번째 글자가 같으면 result를 1 증가
                    if listed[0][i+j]==listed[1][j]:
                        result += 1
                
                # B의 모든 글자가 일치한다면 단축키 1번 사용 가능!
                if result == len(listed[1]):
                    answer += 1
                    
    # [최소 타이핑 수 계산]
    # - 기본적으로 한 글자당 1타이핑이므로 전체 길이는 len(listed[0])
    # - 단축키 B를 1번 누르면 B의 길이(len(listed[1]))만큼 칠 것을 1타로 줄이므로,
    #   단축키 1회당 (len(listed[1]) - 1) 만큼의 타이핑 횟수가 절약됩니다.
    # - 따라서: (전체 문자열 길이) - (단축키 사용 횟수 * 절약된 타수)
    return len(listed[0])-(answer*(len(listed[1])-1))        

# 테스트 케이스의 개수 T 입력
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # 공백으로 구분된 두 문자열(A와 B)을 각각 글자 리스트로 변환하여 저장
    # 예: "banana bana" -> listed = [['b','a','n','a','n','a'], ['b','a','n','a']]
    # listed[0] = 전체 문자열 A, listed[1] = 단축키 문자열 B
    listed=list(map(list,input().split()))
    #print(listed)
    print(f'#{test_case}',answer(listed))
    
    