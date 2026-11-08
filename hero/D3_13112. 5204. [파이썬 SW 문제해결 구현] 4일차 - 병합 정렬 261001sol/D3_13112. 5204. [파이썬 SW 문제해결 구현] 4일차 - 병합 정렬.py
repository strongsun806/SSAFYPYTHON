import sys
sys.stdin = open("D3_13112. 5204. [파이썬 SW 문제해결 구현] 4일차 - 병합 정렬/input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    list1 = list(map(int, input().split()))

    # 병합 과정에서
    # 왼쪽 리스트의 마지막 값이 오른쪽 리스트의 마지막 값보다 큰 경우의 수
    count_bigger_left_last = 0


    # 정렬된 두 리스트 left, right를
    # 하나의 정렬된 리스트로 합치는 함수
    def merging_sorted_list(left, right):
        merged_list = []

        global count_bigger_left_last

        # 문제에서 요구한 카운트 조건
        # 병합 시작 전에 왼쪽의 마지막 값과 오른쪽의 마지막 값을 비교
        if left[-1] > right[-1]:
            count_bigger_left_last += 1

        # x: left에서 현재 보고 있는 위치
        # y: right에서 현재 보고 있는 위치
        x, y = 0, 0

        # left 또는 right에 아직 확인하지 않은 값이 남아있는 동안 반복
        while len(left) > x or len(right) > y:

            # left와 right 둘 다 아직 값이 남아있는 경우
            if len(left) > x and len(right) > y:

                # 현재 위치의 두 값을 비교해서
                # 더 작은 값을 merged_list에 넣음
                if left[x] < right[y]:
                    merged_list.append(left[x])
                    x += 1

                else:  # left[x] >= right[y]
                    merged_list.append(right[y])
                    y += 1

            # right는 다 썼고 left만 남은 경우
            elif len(left) > x:
                merged_list.append(left[x])
                x += 1

            # left는 다 썼고 right만 남은 경우
            else:
                merged_list.append(right[y])
                y += 1

        # 두 리스트를 합쳐 만든 정렬된 리스트 반환
        return merged_list


    # 병합 정렬 함수
    # 리스트를 계속 절반씩 나눈 뒤
    # 다시 올라오면서 정렬하여 합침
    def sorting_by_recursion(array):

        # 원소가 1개라면 이미 정렬된 상태
        # 재귀 종료 조건
        if len(array) == 1:
            return array

        # 리스트를 반으로 나누기 위한 중간 인덱스
        mid = len(array) // 2

        # 왼쪽 절반을 다시 재귀적으로 분할하고 정렬
        left = sorting_by_recursion(array[:mid])

        # 오른쪽 절반을 다시 재귀적으로 분할하고 정렬
        right = sorting_by_recursion(array[mid:])

        # 정렬된 left와 right를 합친 결과를
        # 다시 위의 재귀 호출로 반환
        return merging_sorted_list(left, right)


    # 병합 정렬을 수행하고
    # 정렬된 리스트의 가운데 값과
    # 조건을 만족한 병합 횟수를 출력
    print(f'#{tc} {sorting_by_recursion(list1)[N // 2]} {count_bigger_left_last}')