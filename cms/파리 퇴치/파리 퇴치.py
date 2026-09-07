import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    fly_list = []
    for i in range(n):
        fly_list.append(list(map(int,input().split())))
    result = 0
    for i in range(n):
        for j in range(n):
            if i+m <= n and n-i >= m and j+m <= n and n-j >= m :
                catch = 0
                for k in range(m):
                    for l in range(m):
                        catch += fly_list[i+k][j+l]
                if catch > result:
                    result = catch


    print(f"#{test_case} {result}")
