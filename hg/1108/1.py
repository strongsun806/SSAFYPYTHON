# 29948 자연수의 합

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    total_sum = sum(range(1, N + 1))
    print(f"#{tc} {total_sum}")

'''

1부터 M까지 누적합을 구하는 문제
그러면 M이 될 때 까지 
합에다가 1부터 M까지 더해주면 되겠지요?

 T = int(input()) 인풋을 받아왔음
for test_case in range(1, T+1): 테스트케이스를 도는 동안
    M = int(input()) 일단 숫자를 하나 받아와 자연수 M이 될 떄까지 더해야한다했으니까?
 
    S = 0 #합을 저장할 변수를 일단 먼저 정해주고
    N = 0 #1부터 더해야되니까 일단 0으로 시작하는 애 하나를 지정해주기
    while S < M: #합이 M보다 작을 동안
        N += 1 #1부터 더해야되니까 1씩 증가시키면서
        S += N #합에다가 N을 더해주고

    print(f"#{test_case} {N}") 다 더해진 값을 출력하기
'''