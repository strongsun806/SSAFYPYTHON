# 시간 복잡도!!!
# 기본연산 수행횟수 + 입력받는 데이터를 종합적으로 고려해서 계산하는 점근적 표기법

import sys
sys.stdin = open("input.txt","r")

for _ in range(10):
    tc=int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    ans=0

    print(f"#{tc} {ans}")