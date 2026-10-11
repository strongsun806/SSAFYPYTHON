def binary_search(target, arr, n):
    left = 0
    right = n - 1
    direction = 0  # 0: 시작(방향 없음), 1: 왼쪽, 2: 오른쪽

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            # 값을 찾았고, 연속 같은 방향 조건도 위반하지 않음
            return True

        elif arr[mid] > target:
            # 왼쪽 구간 선택 (left ~ mid - 1)
            # 직전에도 왼쪽(1)을 선택했었다면 조건 불만족
            if direction == 1:
                return False
            direction = 1
            right = mid - 1

        else:
            # 오른쪽 구간 선택 (mid + 1 ~ right)
            # 직전에도 오른쪽(2)을 선택했었다면 조건 불만족
            if direction == 2:
                return False
            direction = 2
            left = mid + 1

    return False


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # 1. A 리스트 오름차순 정렬
    A.sort()

    # 2. B의 각 원소에 대해 조건 만족 여부 확인
    ans = 0
    for target in B:
        if binary_search(target, A, N):
            ans += 1

    print(f"#{tc} {ans}")