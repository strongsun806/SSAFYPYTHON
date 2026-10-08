# [문제] 의석이의 세로로 말해요 (SWEA 5356)
# 총 5줄의 단어가 주어지며, 각 단어의 길이는 1글자에서 최대 15글자까지 서로 다를 수 있습니다.
# 이 단어들을 위에서 아래로(세로 방향으로) 읽어서 차례대로 출력하는 문제입니다.
# 각 단어의 길이가 다르므로 빈 칸이 발생하면 건너뛰고 읽어야 합니다.

import sys
sys.stdin = open("input3.txt","r")

# 테스트 케이스 개수 t 입력
t = int(input())
for tc in range(1,t+1):
    # 5줄의 문자열을 담을 2차원 리스트
    listed=[]
    for i in range(5):
        listed+=[list(map(list,input()))]
        
    # 세로로 읽은 글자들을 순서대로 담을 결과 리스트
    result=[]
    
    # [열 우선 순회 (세로 읽기)]
    # 단어의 최대 길이가 15이므로 열 인덱스 i는 0부터 14까지
    for i in range(15):
        # 행 인덱스 j는 0부터 4까지 (총 5개 행)
        for j in range(5):
            try:
                # j행의 i번째 글자가 존재하면 result 리스트에 추가
                result += listed[j][i]
            except:
                # 해당 단어의 길이가 i보다 짧아 IndexError가 발생하면 빈 칸이므로 건너뜀
                continue
                
    # 문자 리스트를 하나의 문자열로 합쳐서 출력
    print(f'#{tc}',"".join(result))