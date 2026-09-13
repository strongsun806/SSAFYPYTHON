# [문제] 글자수 (SWEA 4865)
# 두 개의 문자열 str1과 str2가 주어질 때,
# str1에 포함된 글자들이 str2에 각각 몇 번씩 들어있는지 세고,
# 그중 가장 많이 나타나는 글자의 '등장 횟수'를 출력하는 문제입니다.

import sys
sys.stdin=open("input6.txt","r")

# 테스트 케이스의 개수 t 입력
t= int(input())
for tc in range(1,t+1):
    # 첫 번째 문자열을 입력받아 중복을 제거(set)한 뒤 리스트로 변환합니다.
    # 중복 문자를 미리 제거하면 불필요하게 같은 글자를 여러 번 세는 것을 방지할 수 있습니다.
    first= list(set(input()))
    # 두 번째 문자열(글자 수를 셀 대상)을 한 글자씩 리스트로 변환합니다.
    second= list(input())
    
    # 각 글자의 등장 횟수를 기록할 딕셔너리 (예: {'A': 3, 'B': 5})
    result={}
    
    # first의 각 글자가 second 안에 몇 번 나오는지 비교합니다.
    for i in range(len(first)):
        for j in range(len(second)):
            # 글자가 일치하는 경우
            if first[i]==second[j]:
                try:
                    # 딕셔너리에 이미 등록되어 있다면 카운트를 1 증가
                    result[first[i]]+=1
                except:
                    # 아직 딕셔너리에 없다면(KeyError 발생 시) 새로 1로 등록
                    result.update({first[i]:1})
    # print(result)
    
    # 등장 횟수 중 최댓값을 구합니다.
    count = 0
    for k,v in result.items():
        # 기존 최댓값보다 더 많이 등장한 글자가 있다면 갱신
        if v>count:
            count=v
            
    # 테스트 케이스 번호와 최다 등장 횟수 출력
    print(f'#{tc}',count)