# [문제] 회문1 (SWEA 1215)
# 8x8 크기의 글자판에서 제시된 길이 N을 갖는 모든 회문의 '총 개수'를 찾는 문제입니다.
# 가로 방향과 세로 방향을 모두 검사하며,
# 길이가 짝수(even)일 때와 홀수(odd)일 때 중심 대칭 계산 방식이 다르므로 나누어 처리합니다.

import sys
sys.stdin = open("input.txt", "r")

# [1] 짝수 길이(N)의 가로 회문 개수를 세는 함수
def even_garo(matrix, N):
    result = 0
    half = N // 2  # 단어 절반의 길이
    for i in range(8):  # 8개 행 순회
        for j in range(8 - N + 1):  # 회문이 시작 가능한 열 인덱스 범위
            can = 0
            # 중심의 두 글자 사이를 기점으로 k만큼 좌우로 벌어지며 대칭 여부 검사
            # 왼쪽 글자: j + (half - 1) - k
            # 오른쪽 글자: j + half + k
            for k in range(half):
                if matrix[i][j + (half - 1) - k] == matrix[i][j + half + k]:
                    can += 1
            # half개의 글자 쌍이 모두 일치하면 회문 1개 발견
            if can == half:
                result += 1
    return result


# [2] 짝수 길이(N)의 세로 회문 개수를 세는 함수
def even_sero(matrix, N):
    result = 0
    half = N // 2
    for j in range(8):  # 8개 열 순회
        for i in range(8 - N + 1):  # 회문이 시작 가능한 행 인덱스 범위
            can = 0
            # 중심 두 글자를 기점으로 k만큼 위아래로 벌어지며 대칭 검사
            # 위쪽 글자: i + (half - 1) - k
            # 아래쪽 글자: i + half + k
            for k in range(half):
                if matrix[i + (half - 1) - k][j] == matrix[i + half + k][j]:
                    can += 1
            if can == half:
                result += 1
    return result


# [3] 홀수 길이(N)의 가로 회문 개수를 세는 함수
def odd_garo(matrix, N):
    result = 0
    half = N // 2
    for i in range(8):  # 8개 행 순회
        for j in range(8 - N + 1):  # 회문이 시작 가능한 열 인덱스 범위
            can = 0
            # 정중앙의 한 글자(j + half)를 기준으로 좌우 대칭 검사
            # 왼쪽 글자: j + half - k
            # 오른쪽 글자: j + half + k
            # (k=0일 때는 중앙 자기 자신이므로 항상 일치)
            for k in range(half + 1):
                if matrix[i][j + half - k] == matrix[i][j + half + k]:
                    can += 1
            # 중심을 포함한 (half + 1)개가 모두 일치하면 회문
            if can == half + 1:
                result += 1
    return result


# [4] 홀수 길이(N)의 세로 회문 개수를 세는 함수
def odd_sero(matrix, N):
    result = 0
    half = N // 2
    for j in range(8):  # 8개 열 순회
        for i in range(8 - N + 1):  # 회문이 시작 가능한 행 인덱스 범위
            can = 0
            # 정중앙 글자(i + half)를 기준으로 상하 대칭 검사
            # 위쪽 글자: i + half - k
            # 아래쪽 글자: i + half + k
            for k in range(half + 1):
                if matrix[i + half - k][j] == matrix[i + half + k][j]:
                    can += 1
            if can == half + 1:
                result += 1
    return result


# SWEA 1215 문제는 총 10개의 테스트 케이스가 고정으로 주어집니다.
T = 10
for test_case in range(1, T + 1):
    # 찾아야 하는 회문의 길이 N 입력
    N = int(input())
    # 8x8 크기의 글자판 입력
    matrix = []
    for _ in range(8):
        matrix.append(list(input()))

    # 회문의 길이 N이 짝수인지 홀수인지에 따라 적절한 함수를 호출하여 가로 + 세로 합산
    if N % 2 == 0:
        total = even_garo(matrix, N) + even_sero(matrix, N)
    else:
        total = odd_garo(matrix, N) + odd_sero(matrix, N)

    # 테스트 케이스 번호와 회문의 총 개수 출력
    print(f"#{test_case} {total}")