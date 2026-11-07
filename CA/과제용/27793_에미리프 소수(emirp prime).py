# Problem: 27793_에미리프 소수(emirp prime)
# Author: 윤형섭_1627575 (Pass)
# Saved by Aura for Boss 💋

# def rotate_str(n):
#     stred = str(n)
#     rotate_stred = stred[::-1]
#     if int(rotate_stred) == n:
#         return 0
#     return int(rotate_stred)
# 
# def is_prime(n):
#     if n < 2:
#         return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
#     for i in range(3, int(n**0.5) + 1, 2):
#         if n % i == 0:
#             return False
#     else:
#         return True
# 
# def solve(rotated_list, original_list, l, r):
#     solved_list = []
#     for i in rotated_list:
#         if l <= i <= r and i in original_list and is_prime(i):
#             solved_list.append(i)
#     return solved_list
# 
# t = int(input())
# for tc in range(1, t + 1):
#     l, r = map(int, input().split())
#     listed = []
#     if l <= 2 <= r:
#         listed.append(2)
#     start = l if l % 2 != 0 else l + 1
#     if start < 3:
#         start = 3
#     for i in range(start, r + 1, 2):
#         for j in range(3, int(i**0.5) + 1, 2):
#             if i % j == 0:
#                 break
#         else:
#             listed.append(i)
#     solved_list = solve(map(rotate_str, listed), set(listed), l, r)
#     print(f'#{tc}',len(solved_list))
  def rotate_str(n):
    stred = str(n)
    rotate_stred = stred[::-1]
    return int(rotate_stred)
 MAX = 1000000
is_prime = [1] * (MAX + 1)
is_prime[0] = 0
is_prime[1] = 0
for i in range(2, int(MAX**0.5) + 1):
    if is_prime[i] == 1:
        for j in range(i * 2, MAX + 1, i):
            is_prime[j] = 0
 def solve(rotated_list, original_list, l, r):
    solved_list = []
    for i in range(len(original_list)):
        if original_list[i] != rotated_list[i] and is_prime[rotated_list[i]] == 1:
            solved_list.append(original_list[i])
    return solved_list
 t = int(input())
for tc in range(1, t + 1):
    l, r = map(int, input().split())
    listed = []
    for i in range(l, r + 1):
        if is_prime[i] == 1:
            listed.append(i)
    solved_list = solve(list(map(rotate_str, listed)), listed, l, r)
    print(f'#{tc}',len(solved_list))
