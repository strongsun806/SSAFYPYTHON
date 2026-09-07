from pprint import pprint
import sys
sys.stdin = open("input1.txt", "r")

def get_val(matrix, r, c, N, M):
    try:
        # 음수면 강제로 IndexError 발생
        if r < 0 or c < 0:
            raise IndexError
        return matrix[r][c]
    except IndexError:
        return 0
T = int(input())

for test_case in range(1, T + 1):
    N , M = list(map(int,input().split()))
    matrix=[]
    count=0
    for i in range(N):
        matrix.append(list(map(int,input().split())))
    count = 0
    for r in range(N):
        for c in range(M):
            pang = matrix[r][c]
            compare = pang
            
            for k in range(1, pang + 1):
                compare += get_val(matrix, r - k, c, N, M)  # 상
                compare += get_val(matrix, r + k, c, N, M)  # 하
                compare += get_val(matrix, r, c - k, N, M)  # 좌
                compare += get_val(matrix, r, c + k, N, M)  # 우
            
            if compare > count:
                count = compare
    print(f'#{test_case}',count)