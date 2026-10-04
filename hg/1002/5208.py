# 전기 버스 2
# 충전이 아니고 교환
# 모든 경우의 수 수행해보기
# 특정 시점에서 가능한 경우의 수 모두 수행 해보기

# idx번 정류장에서 충전지를 갈아 끼우는 경우,
# 갈아 끼우지 않는 경우를 모두 수행
# 배터리 잔량과, 교환횟수를 인자로 받아서 처리

def solve(idx, remain, cnt):
    global min_cnt

    # 이미 찾은 최소 교환 횟수보다 크거나 같으면 중단
    if cnt >= min_cnt:
        return

    # 종점(N번 정류장) 도착
    if idx == data[0]:
        min_cnt = min(min_cnt, cnt)
        return

    #idx번 정류장에서 배터리를 교환하고 다음 정류장으로 이동
    solve(idx + 1, data[idx] - 1, cnt + 1)

    #idx번 정류장에서 배터리를 교환하지 않고 지나가는 경우
    if remain > 0:
        solve(idx + 1, remain - 1, cnt)


T = int(input())
for tc in range(1, T + 1):
    data = list(map(int, input().split()))
    min_cnt = float('inf')

    solve(2, data[1] - 1, 0)
    print(f'#{tc} {min_cnt}')