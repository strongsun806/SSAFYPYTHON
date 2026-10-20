import sys
sys.stdin = open('sample_input.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    arr = []
    # 다음번 피자
    idx = 0
    while True:
        # 화덕이 비어있고, 다음번 피자가 있을때
        if not len(arr) == N and idx < M:
            arr.append([data[idx], idx])
            idx += 1
            continue
        # 화덕에 피자가 한판 남았을 때
        if len(arr) == 1:
            print(f'#{tc} {arr[0][1]+1}')
            break
        # 화덕이 가득 차 있을때 맨 앞의 피자를 확인
        tmp = arr.pop(0)
        # 치즈를 절반 줄임, 다 녹았으면 뺀 후 다음 반복으로 아니면 다시 넣어줌
        tmp[0] //= 2
        if tmp[0] == 0:
            continue
        else:
            arr.append(tmp)
        
        
        


        