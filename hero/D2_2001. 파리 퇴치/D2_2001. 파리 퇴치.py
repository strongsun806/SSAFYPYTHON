# 문제를 풀 때 하지 말아야할 것
# SWEA의 목적 >> 파이썬이 아니라 알고리즘 학습
#            >> 파이썬에만 있는 문법 사용을 지양
#            >> 반복문, 조건문... set, list 당연히 이런건 사용하는거고
#            >> len()도 써야만 하는 것들인데.. 써도 되는데...
#            익숙해지기 전까지는 연습하자!
# 압수 : sum, min, max, set도 웬만하면 압수, index 압수
# arr = [1, 2, 3, 4, 5]
# for num in arr:  <<< 금지, 1차 목적: 인덱싱을 잘하자!
# for i in range(len(arr)):
#     arr[i]

# 문제보고 풀어보기 전에 코드 작성 절대 금지! 어차피 개꼬임 ㅋ
# 코딩 > 머릿 속 정리된 로직을 코드로 옮기는 과정

# 1번 아이디어: 모든 칸 때려보기 -> how?
# 명확한것: MxM을 돌아야한다(반복문)
#

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    # NxN 행렬이 만들어짐 >> 요소가 리스트인 리스트

    # arr = []
    # for _ in range(n):
    #     arr.append(list(map(int, input().split())))
    # 이걸 바로 밑에처럼 list comprehension으로 쓸 줄 알아야함!!! 꼭임!
    # 알고리즘에서 무조건 쓰는거니까 제발 연습하래 ㅠㅡㅠ
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_sum = 0
    for i in range(n-(m-1)):
        for j in range(n-(m-1)):
            sum_v = 0
            for a in range(i,i+m):
                for b in range(j,j+m):
                    sum_v += arr[a][b]
                    # 이제 파리채 영역 다 돌았음. 이제 몇마린지 확인
                    # 현재 잡은 파리수가 제일 많으면 저장
            if sum_v > max_sum:
                max_sum = sum_v
    print(f'#{test_case} {max_sum}')


    # max_sum = 0
    # #파리채 시작점 바꿔주기
    # for i in range(n-(m-1)):
    #     for j in range(n-(m-1)):
    #         # i,j가 시작점이고, 여기에서 시작하면 MxM짜리 파리채
    #         sum_v = 0
    #         for k in range(i, i+m):
    #             for l in range(j, j+m):
    #                 # print(arr[k][l],end=' ')
    #                 sum_v += arr[k][l]
    #             # print()
    #         if sum_v > max_sum:
    #             max_sum = sum_v
    # print(max_sum)

# -------------------위는 강사님 버전-------------------------------

