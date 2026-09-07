import sys
sys.stdin = open("sample_input.txt","r")

def binary_search_count(total_page, target):
    left = 1
    right = total_page
    count = 0
 
    while True:
        center = (left + right) // 2
        count += 1
 
        if center == target:
            return count
 
        if target < center:
            right = center
        else:
            left = center
 
 
T = int(input())
 
for test_case in range(1, T + 1):
    P, Pa, Pb = map(int, input().split())
 
    count_a = binary_search_count(P, Pa)
    count_b = binary_search_count(P, Pb)
 
    if count_a < count_b:
        winner = "A"
    elif count_a > count_b:
        winner = "B"
    else:
        winner = "0"
 
    print(f"#{test_case} {winner}")