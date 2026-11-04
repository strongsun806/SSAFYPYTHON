import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    lines = []
    for _ in range(N):
        A, B = map(int, input().split())
        lines.append((A, B))
        
    count = 0
    # 두 전선이 교차하는 조건: (A1 < A2 and B1 > B2) 또는 (A1 > A2 and B1 < B2)
    for i in range(N):
        for j in range(i + 1, N):
            if (lines[i][0] - lines[j][0]) * (lines[i][1] - lines[j][1]) < 0:
                count += 1
                
    print(f"#{test_case} {count}")
