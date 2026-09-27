# N, 2N, 3N... 계속 숫자를 늘려가면서
# 각 숫자의 자릿수를 확인해서 0~9를 전부 봤을 때 멈추기

# 내 생각 먼저
# 일단 0~9를 봤는지 확인할 리스트 하나 만들고
# 숫자를 하나씩 볼 때마다 해당 숫자 위치를 1로...?
# 그리고 새로운 숫자를 발견할 때마다 cnt += 1
# cnt가 10이 되면 0~9 다 봤다는 뜻이니까 끝!!!!

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    # 0~9까지 봤는지 체크하는 리스트
    check = [0] * 10

    cnt = 0
    k = 0

    # 0~9를 전부 볼 때까지 반복
    while cnt < 10:
        k += 1
        # 현재 세고 있는 양 번호
        sheep = N * k
        # 숫자의 각 자릿수를 하나씩 확인하기
        temp = sheep


        while temp > 0:
            num = temp % 10

            # 아직 못 본 숫자라면 체크하고 cnt 증가
            if check[num] == 0:
                check[num] = 1
                cnt += 1

            # 확인한 마지막 자릿수 없애기
            temp //= 10

    # 문제에서 원하는건 몇 번째 Xxx
    # 마지막으로 센 양의 번호 = k * N
    print(f'#{tc} {sheep}')