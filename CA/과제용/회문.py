# [문제] 회문 (SWEA 4861)
# N x N 크기의 문자열 판에서 가로 또는 세로 방향으로 놓인
# '길이가 M인 회문(앞뒤가 똑같은 단어)'을 찾아 출력하는 알고리즘입니다.

import sys, pprint
sys.stdin=open("input5.txt","r")

def garo(listed, n, m):
    # [가로 방향 회문 탐색]
    # n개의 모든 행(i)을 검사합니다.
    for i in range(n):
        # 길이가 m인 회문이 들어갈 수 있는 시작 열(j)은 0부터 (n - m)까지입니다.
        for j in range(n - m + 1):
            count = 0  # 대칭되는 글자가 일치하는 쌍의 수를 세는 변수 (위치마다 초기화)
            
            # 단어의 절반(m // 2)만큼 앞과 뒤를 짝지어 비교합니다.
            for k in range(m // 2):
                # j부터 시작하는 부분 문자열의 앞(j + k)과 뒤(j + m - 1 - k) 문자 비교
                if listed[i][j + k] == listed[i][j + m - 1 - k]:
                    count += 1
                    
            # 모든 대칭 쌍이 일치한다면 회문이 맞으므로 해당 구간의 문자열을 합쳐 반환
            if count == m // 2:
                return "".join(listed[i][j:j+m])
    # 가로에서 회문을 찾지 못한 경우 None 반환
    return None

def sero(listed, n, m):
    # [세로 방향 회문 탐색]
    # n개의 모든 열(j)을 검사합니다.
    for j in range(n):
        # 길이가 m인 회문이 들어갈 수 있는 시작 행(i)은 0부터 (n - m)까지입니다.
        for i in range(n - m + 1):
            count = 0  # 대칭되는 글자가 일치하는 쌍의 수
            
            # 단어의 절반(m // 2)만큼 위와 아래를 짝지어 비교합니다.
            for k in range(m // 2):
                # i부터 시작하는 세로 문자열의 위(i + k)와 아래(i + m - 1 - k) 문자 비교
                if listed[i + k][j] == listed[i + m - 1 - k][j]:
                    count += 1
                    
            # 모든 대칭 쌍이 일치한다면 세로 회문이므로 문자들을 모아 문자열로 반환
            if count == m // 2:
                return "".join([listed[i + k][j] for k in range(m)])
    # 세로에서도 회문을 찾지 못한 경우 None 반환
    return None

# 테스트 케이스 개수 t 입력
t = int(input())
for tc in range(1, t + 1):
    # n: 글자판 크기(N x N), m: 찾으려는 회문의 길이
    n, m = map(int, input().split())
    # N개의 줄을 읽어 글자 단위의 2차원 리스트로 구성
    listed = [list(input().strip()) for _ in range(n)]
    
    # 1. 먼저 가로 방향에서 길이가 m인 회문을 찾습니다.
    ans = garo(listed, n, m)
    # 2. 만약 가로에 없다면(None) 세로 방향에서 회문을 찾습니다.
    if ans is None:
        ans = sero(listed, n, m)
        
    # 테스트 케이스 번호와 찾은 회문 출력
    print(f"#{tc} {ans}")
    