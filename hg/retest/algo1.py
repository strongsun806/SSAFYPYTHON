# 내리막 def 쓰지 않고 이중 for문이랑 리스트 큐 만으로 푸는거
#마주보는 자리 더하기 : 인덱스 두개 다루기

# 양쪽 끝에서 가운데로 좁혀오면서 합 비교하는거 
# 1) 짝긔 인덱스 : 앞쪽은 i, 반대편은 N-1-i
# 2) 짝의 개수 : N을 2로 나눈 몫(N//2) 만큼만 돈다(홀수면 가운데 하나는 알아서 제외됨)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    
    # 바깥쪽부터 안쪽으로 들어가면서 짝의 합을 구해서 리스트에 모은다
    pair_sums = []
    for i in range(N//2):
        pair_sum = arr[i] + arr[N-1-i]
        pair_sums.append(pair_sum)
        
    #짝의 합이 계속 증가하는지 검사해야함
    # 기본 값을 1(성공)로 두고, 한 번이라도 증가하지 않으면 0으로 바꾸고 중단
    ans = 1
    #pair_sums의 길이가 1개면 아래 for문이 아예 실행되지 않고 그대로 1이 출력됨(조건만족)
    for i in range(len(pair_sums) - 1):
        #다음 합이 현재 합보다 크지 않으면 (같거나 작으면) 증가가 아님
        if pair_sums[i + 1]< pair_sum[i]:
            ans = 0
            break
    
    # 정답 출력
    print(f"#{tc} {ans}")