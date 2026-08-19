# 고등학교 1000명의 학생들의 수학 성적을 토대
# 최빈수를 이용해 학생들의 평균 수준을 짐작하기 위함
# 최빈수를 출력하는 프로그램 제작
"""
풀이 최초 구상
for 문을 활용해 성적들을 하나씩 출력
딕셔너리에 점수별 갯수를 측정
다시 for문을 사용해 딕셔너리의 개수를 하나씩 출력
가장 높은 개수의 키 값을 출력
"""

import sys
sys.stdin = open("input.txt", "r")


T = int(input())
for test_case in range(1, T + 1):
    num = int(input())
    scores = list(map(int, input().split()))

    score_counts = {}
    for score in scores:
        if score in score_counts:
            score_counts[score] += 1
        else:
            score_counts[score] = 1

    max_score_1 = 0
    max_score_2 = 0

    for score, count in score_counts.items():
        if count > max_score_1:
            max_score_1 = count
            max_score_2 = score
        elif count == max_score_1:
            if score > max_score_2:
                max_score_2 = score

    print(f"#{num} {max_score_2}")

