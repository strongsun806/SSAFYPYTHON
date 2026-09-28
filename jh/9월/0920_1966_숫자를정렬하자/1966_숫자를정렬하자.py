import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    nums = list(map(str, nums))
    num = ' '.join(nums)
    print(f'#{tc} {num}')