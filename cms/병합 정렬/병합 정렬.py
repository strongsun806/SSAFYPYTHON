import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    L = list(map(int, input().split()))

    cnt = 0

    def merge_sort(arr):
        global cnt

        # 원소가 하나라면 이미 정렬된 상태
        if len(arr) == 1:
            return arr

        mid = len(arr) // 2

        # 분할 + 정복
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        # 문제에서 요구하는 조건
        if left[-1] > right[-1]:
            cnt += 1

        # 병합
        result = []

        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # 남은 원소 붙이기
        result.extend(left[i:])
        result.extend(right[j:])

        return result

    L = merge_sort(L)

    print(f"#{tc} {L[N//2]} {cnt}")