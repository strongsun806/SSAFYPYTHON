import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    A, B, C = map(int, input().split())
    eat_count = 0
    
    # B는 C보다 작아야 함
    if B >= C:
        diff = B - (C - 1)
        eat_count += diff
        B = C - 1
        
    # A는 B보다 작아야 함
    if A >= B:
        diff = A - (B - 1)
        eat_count += diff
        A = B - 1
        
    # 사탕 개수는 자연수(1 이상)이어야 함
    if A <= 0 or B <= 0 or C <= 0:
        print(f"#{test_case} -1")
    else:
        print(f"#{test_case} {eat_count}")
