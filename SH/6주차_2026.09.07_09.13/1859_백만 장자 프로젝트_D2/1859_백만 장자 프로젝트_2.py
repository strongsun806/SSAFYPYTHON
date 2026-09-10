import sys
sys.stdin = open("input.txt", "r")

"""
문제 구상
원재는 미래를 보는 능력을 이용해 사재기를 하려고 함
단, 조건이 있음
1. 연속된 N일 동안의 매매가를 알고 있음
2. 하루에 1개만 구입 가능
3. 판매는 언제든 할 수 있음
위 조건을 만족해서 최대 이익을 구하기

로직 구상
1. 볼 수 있는 미래 일수를 인풋하기
2. 매매가를 인풋하기
3. 하나씩 불러오면서 이전 것보다 크다면 차이를 더하고 count += 1
4. 그 다음 것도 이전 것보다 크다면 차이를 더함 단, 가격차이에 count를 곱한 것을 더함 그리고 count += 1
5. 만약 이전 것보다 작다면 지금까지의 가격을 max_income에 저장하고 0으로 초기화하고 count도 1로 초기화
6. 반복
"""
T = int(input())
for test_case in range(1, T+1):
    # 1. 볼 수 있는 미래 일수를 인풋하기
    N = int(input())
    # 2. 매매가를 인풋하기
    days_price = list(map(int, input().split()))

    # 3. 하나씩 불러오면서 이전 것보다 크다면 차이를 더하고 count += 1
    # 3-1. 최대 이익(max_income), 현재까지의 이익(income), 개수(count)의 초기값 세팅
    max_income = 0
    income = 0
    count = 1
    # 3-2. 하나씩 불러오기
    for price in days_price:
        # 3-3. 이전 것보다 크다면 차이를 더하고 count += 1
        if price >= income:
            income = income + (price - income)*count  # 4. 가격차이에 count를 곱함
            count += 1
        # 5. 만약 이전 것보다 작다면 지금까지의 가격을 max_income에 저장하고 0으로 초기화, count도 1로 초기화
        else:
            max_income += income
            income = 0
            count = 1


    print(f"#{test_case} {max_income}")

# 522 4575 -> 4053
# 6426 9445 8772 81 3447 -> 6385