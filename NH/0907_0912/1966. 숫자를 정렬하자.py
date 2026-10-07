# N개의 숫자를 오름차순으로 정렬

# 내 생각 먼저
# 앞에서부터 숫자 두개씩 비교해서
# 앞 숫자가 뒤 숫자보다 크면 둘이 자리 바꾸기
# 이걸 계속 반복하면 큰 숫자가 뒤로
# 그리고 이걸 N번 정도 반복하면 결국 전체가 정렬됨
# 버블정렬!!!

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 일단 처음부터 끝까지 계속 돌기
    for i in range(N - 1):

        # 바로 옆에 있는 숫자끼리 비교
        # 뒤쪽은 이미 큰 숫자들이 정리됐으니까 N-1-i까지만 봐도 됨
        for j in range(N - 1 - i):

            # 앞 숫자가 더 크면?
            if arr[j] > arr[j + 1]:

                # 둘이 자리 바꾸기
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    print(f'#{tc} {" ".join(map(str, arr))}')