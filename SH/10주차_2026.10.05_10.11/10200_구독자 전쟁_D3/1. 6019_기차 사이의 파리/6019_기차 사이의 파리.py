import sys
import os
sys.stdin = open(os.path.join(os.path.dirname(__file__), "s_input.txt"), "r")

"""
<문제>
소녀가 존 폰 노이만에게 질문함
두 기차 A, B가 서로를 향해 달려옴
두 기차는 250마일 떨어져 있고, A: 시속 10마일, B: 시속 15마일
파리(시속 20마일)가 기차 A → B → A로 날아감
기차가 서로 충돌했을 때 파리는 몇 마일을 이동했을까

풀이 구상
파리는 기차마다 부딪하면서 계속 이동하기 때문에
기차 A와 B가 충돌할 때까지 걸리는 시간을 구하고
파리의 속도를 이용해 거리를 구하면 됨

로직 구상
1. 기차 A와 B가 충돌할 때까지의 걸리는 시간 구하기
2. 시간과 파리의 속도를 곱해 파리의 거리 구하기
3. 결과를 테스트케이스와 함께 출력
"""

T = int(input())
for test_case in range(1, T+1):
    D, A, B, F = map(int, input().split())

    result = D / (A + B) * F

    print(f"#{test_case} {result}")