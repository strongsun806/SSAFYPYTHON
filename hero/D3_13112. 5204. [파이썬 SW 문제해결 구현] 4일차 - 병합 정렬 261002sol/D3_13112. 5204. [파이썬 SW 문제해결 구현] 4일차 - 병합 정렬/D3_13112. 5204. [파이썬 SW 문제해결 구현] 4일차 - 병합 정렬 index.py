import sys
sys.stdin = open("D3_13112. 5204. [파이썬 SW 문제해결 구현] 4일차 - 병합 정렬/input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    list1 = list(map(int, input().split()))

    # 병합할 때 사용할 임시 리스트
    # 매번 새로운 merged_list를 만들지 않고
    # 처음에 N 크기로 하나만 만들어 계속 재사용
    temp = [0] * N

    # 문제에서 요구하는 경우의 수
    count_bigger_left_last = 0


    # list1의
    # [start ~ mid-1] 부분과
    # [mid ~ end-1] 부분을 병합하는 함수
    def merging_sorted_list(start, mid, end):
        global count_bigger_left_last

        # 여기까지 왔다는 것은
        # 왼쪽 부분과 오른쪽 부분이 각각 이미 정렬된 상태

        # 왼쪽 부분의 마지막 값
        # list1[mid - 1]

        # 오른쪽 부분의 마지막 값
        # list1[end - 1]

        # 문제에서 요구한 카운트 조건
        if list1[mid - 1] > list1[end - 1]:
            count_bigger_left_last += 1


        # x : 왼쪽 부분에서 현재 보고 있는 위치
        # y : 오른쪽 부분에서 현재 보고 있는 위치
        # k : temp에 값을 넣을 위치
        x = start
        y = mid
        k = start


        # 왼쪽과 오른쪽 모두 값이 남아있다면
        # 현재 값끼리 비교
        while x < mid and y < end:

            if list1[x] < list1[y]:
                temp[k] = list1[x]
                x += 1

            else:
                temp[k] = list1[y]
                y += 1

            k += 1


        # 오른쪽은 다 썼는데
        # 왼쪽 값이 남아있는 경우
        while x < mid:
            temp[k] = list1[x]
            x += 1
            k += 1


        # 왼쪽은 다 썼는데
        # 오른쪽 값이 남아있는 경우
        while y < end:
            temp[k] = list1[y]
            y += 1
            k += 1


        # temp에 만들어놓은 정렬 결과를
        # 원본 list1에 다시 반영
        for i in range(start, end):
            list1[i] = temp[i]


    # 병합 정렬
    # start 이상 end 미만 범위를 정렬
    def sorting_by_recursion(start, end):

        # 원소가 1개 이하라면
        # 이미 정렬되어 있으므로 종료
        if end - start <= 1:
            return

        # 현재 범위를 절반으로 나눔
        mid = (start + end) // 2


        # 왼쪽 절반 정렬
        sorting_by_recursion(start, mid)

        # 오른쪽 절반 정렬
        sorting_by_recursion(mid, end)


        # 정렬된 왼쪽과 오른쪽을 병합
        merging_sorted_list(start, mid, end)


    # 전체 리스트 정렬
    # 0 이상 N 미만
    sorting_by_recursion(0, N)


    # 정렬된 리스트의 N//2 번째 값과
    # 문제에서 요구한 경우의 수 출력
    print(f'#{tc} {list1[N // 2]} {count_bigger_left_last}')