# [문제] 문자열 비교 (SWEA 4864)
# 두 개의 문자열 str1과 str2가 주어졌을 때,
# 문자열 str2 안에 패턴 문자열 str1이 포함되어 있는지 확인하는 문제입니다.
# 일치하는 문자열이 있으면 1을, 없으면 0을 출력합니다.

import sys
sys.stdin=open("input7.txt","r")

# 테스트 케이스의 개수 t 입력
t = int(input())
for tc in range(1,t+1):
    # first: 찾고자 하는 패턴 문자열 (문자 리스트)
    first= list(input())
    # second: 검색 대상이 되는 전체 본문 문자열 (문자 리스트)
    second= list(input())
    
    # can (candidates): 패턴이 시작될 가능성이 있는 second의 인덱스 번호들을 모아둘 리스트
    can=[]
    
    # 패턴이 완전히 포함되려면 최소한 패턴 길이만큼의 여유 공간이 있어야 하므로
    # 탐색 범위는 0부터 (len(second) - len(first))까지입니다.
    for j in range(len(second)-len(first)+1):
        # 패턴의 첫 글자(first[0])와 일치하는 본문의 시작 위치(j)를 후보로 추가
        if first[0]==second[j]:
            can+=[j]
    # print(can)
    
    # 패턴 일치 여부를 저장할 변수 (존재하면 1, 없으면 0)
    answer=0
    
    # 후보 인덱스들을 하나씩 검사하기 위한 인덱스 변수
    k=0
    while k<len(can):
        result=0  # 일치하는 글자 수를 카운트하는 변수
        
        # 후보 위치 can[k]부터 패턴 길이(len(first))만큼 글자들을 하나씩 비교
        for i in range(can[k],can[k]+len(first)):
            # second의 글자와 first의 대응되는 글자(i - can[k])가 같은지 확인
            if second[i]==first[i-can[k]]:
                result+=1
            else:
                continue
        
            
        k+=1
        # 만약 패턴 길이 전체가 일치했다면 완전히 포함된 것이므로
        if result == len(first):
            answer = 1  # 1로 표시하고
            break       # 더 이상 다른 후보를 검사할 필요 없이 반복 종료
            
    # 테스트 케이스 번호와 결과(1 또는 0) 출력
    print(f"#{tc}",answer)