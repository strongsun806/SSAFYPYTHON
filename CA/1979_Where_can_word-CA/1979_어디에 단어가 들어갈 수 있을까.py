import sys , pprint
sys.stdin = open("input (3).txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N , K = list(map(int,input().split())) #n=5 k=3
    
    matrix=[list(map(int,input().split()))for _ in range(N)]
    pprint.pprint(matrix)
    #가로 탐색
