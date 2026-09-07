from pprint import pprint
import sys
sys.stdin = open("input1.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N , M = list(map(int,input().split()))
    matrix=[]
    count=0
    for i in range(N):
        matrix.append(list(map(int,input().split())))
    # pprint(matrix)
    for i in range(N*M):
        compare=0
        compare += matrix[i//(M)][i%(M)]#얘로 전체 순환가능
        if i//(M)!=0:#첫째줄이 아닐경우 위에껄 더함
            compare += matrix[(i//(M))-1][i%(M)]
        if i//(M) != N-1:#마지막줄이 아니라면 아래껄 더함
            compare += matrix[i//(M)+1][i%(M)]
        if i%(M) != 0:
            compare += matrix[i//(M)][i%(M)-1]
        if i%(M) != M-1:
            compare += matrix[i//(M)][i%(M)+1]

        if compare>count:
            count = compare
    print (f'#{test_case}',count)#56에서 25 ... 13 이면 matrix[2][1] 13을 6로 나눈 몫, 13을 6으로 나눈 나머지
# 123456
# 789101112
# 13
# 