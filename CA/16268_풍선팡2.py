# ========================================================
# 문제: 16268_풍선팡2
# 난이도: D2
# 작성자: 윤형섭 (1627575)
# 제출 결과: Pass
# 저장 일시: 2026-10-07 11:45:52
# ========================================================

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
    print (f'#{test_case}',count)
