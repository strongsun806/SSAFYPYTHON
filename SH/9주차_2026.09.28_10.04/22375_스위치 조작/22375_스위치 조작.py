import sys
sys.stdin = open("switch_sample_in.txt", "r")

"""
문제 구상
1번부터 N번까지 번호가 붙어있는 전등이 일렬로 설치되어있음
i번 스위치를 조작하면 i부터 N까지의 전등의 상태가 반대가 됨
초기 상태의 전등을 몇번 조작하면 결과 상태가 되는지 확인

로직 구상
1. T받음
2. 전등 개수 N개 받음
3. 초기 전등 상태 받음
4. 최종 결과 전등 상태 받음

각각 첫번쨰 인덱스부터 확인하면서
같으면 두번쨰로 넘어가고
다르면 현재위치에서 N번까지 변경
이걸 반복
"""

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))

    count = 0
    for i in range(N):
        if start[i] != end[i]:
            for j in range(i, N):
                start[j] = 1 - start[j]
            count += 1


    print(f"#{test_case} {count}")