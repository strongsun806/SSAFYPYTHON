import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    def solve(i, j):
        if i == j:
            return i

        cut = (i+j)//2
        group1=solve(i, cut)
        group2=solve(cut+1,j)
        card1 = nums[group1]
        card2 = nums[group2]

        win = group1
        if card1 == 1 and card2 ==2:
            win = group2
        elif card1==2 and card2==3:
            win = group2
        elif card1==3 and card2==1:
            win = group2

        return win

    result = solve(0,N-1)
    print(f"#{tc} {result+1}")