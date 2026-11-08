# 파스칼의 삼각형
# import sys

# sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    print(f"#{tc}")

    triangle = []

    for i in range(N):
        # i번째 줄은 길이가 (i + 1)이고 모든 원소를 1로 초기화
        # 이렇게 두면 양 끝(인덱스 0과 i)은 자연스럽게 1로 유지됨
        row = [1] * (i + 1)

        # 양 끝을 제외한 내부 원소(인덱스 1 ~ i-1)만 윗줄 두 값의 합으로 계산
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        triangle.append(row)
        # 리스트 요소를 공백으로 구분해 출력
        print(*row)