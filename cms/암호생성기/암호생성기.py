import sys
sys.stdin = open("input.txt", "r")

for tc in range(1, 11):
    test_case = int(input())
    q = list(map(int, input().split()))

    cnt = 1
    while True:
        num = q.pop(0)
        num -= cnt
        if num <= 0:
            q.append(0)
            break
        q.append(num)
        cnt += 1

        if cnt == 6:
            cnt = 1

    print(f"#{test_case}", *q)