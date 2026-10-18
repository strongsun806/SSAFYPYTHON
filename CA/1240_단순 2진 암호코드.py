# ========================================================
# 문제: 1240_[S/W 문제해결 응용] 1일차 - 단순 2진 암호코드
# 난이도: D3
# 작성자: 윤형섭 (1627575)
# 제출 결과: Pass
# 저장 일시: 2026-10-07 11:28:49
# ========================================================

code_dict = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}
 T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = []
    for i in range(N):
        arr.append(input().strip())
     target_r = -1
    target_c = -1
     for i in range(N):
        for j in range(M - 1, -1, -1):
            if arr[i][j] == '1':
                target_r = i
                target_c = j
                break
        if target_r != -1:
            break
     code_str = arr[target_r][target_c - 55:target_c + 1]
    numbers = []
    for i in range(0, len(code_str), 7):
        piece = code_str[i:i + 7]
        numbers.append(code_dict[piece])
     odd_sum = 0
    even_sum = 0
    for i in range(len(numbers)):
        if (i + 1) % 2 == 1:
            odd_sum += numbers[i]
        else:
            even_sum += numbers[i]
     check = odd_sum * 3 + even_sum
    if check % 10 == 0:
        ans = sum(numbers)
    else:
        ans = 0
     print(f"#{tc} {ans}")
