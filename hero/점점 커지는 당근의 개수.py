# 인덱스 하나씩 살펴보면서 이전 인덱스와 현재 인덱스 비교
# 현재 인덱스 숫자가 크면 구간 길이 증가
# 구간이 끝나면 (data가 끝이 나거나, 숫자가 작아진 경우)
# 구간의 길이가 최대인지 확인하고 교체

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    carrots = list(map(int, input().split()))

    # 당근 하나씩 살펴보면서 앞 당근이랑 크기 비교
    # i번, i-1번을 비교, 0번 비교 불필요

    # 구간의 최소길이가 1이므로 이걸 만듦
    length = 1

    # 증가하는 구간의 최대값을 저장해야하니
    max_length = 1

    for i in range(1, N):
        # 현재 당근의 크기가 이전 당근보다 크면
        if carrots[i] > carrots[i-1]:
            length += 1

        # 작거나 같으면
        # 증가하는 구간이 끝난거임
        # 구간의 길이 계산하면 됨
        else:
            if length > max_length:
                max_length = length

            # 최장구간 여부와 관계없이 구간의 길이는 초기화가 되어야함
            length = 1

    # 데이터가 끝나고 나면 작아지는 구간이 없으니까 한 번 더 계산
    if length > max_length:
        max_length = length

    print(f'#{tc} {max_length}')

# 디버깅도 연습하기
# 프로그램이 내 생각대로 돌아가는지 잠시 멈춰놓고 확인하기