# Problem: 27668_소피 제르멩 소수
# Author: 윤형섭_1627575 (Pass)
# Saved by Aura for Boss 💋

make_prime = []
 for i in range(1, 1000001):
    is_valid = 1
    for j in range(2, 1001):
        if i < j**2:
            break
        if i >= j**2:
            if i % j == 0:
                is_valid = 0
                break
    if is_valid == 1:
        make_prime.append(i)
make_prime.pop(0)
 T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    ans = 0
     for p in make_prime:
        if p < n:
            continue
        if p > m:
            break
         target = 2 * p + 1
        is_target_prime = 1
         for k in range(2, int(target**0.5) + 1):
            if target % k == 0:
                is_target_prime = 0
                break
         if is_target_prime == 1:
            ans += 1
     print(f"#{test_case} {ans}")
