import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    scores = list(map(int, input().split()))
    arr = [0]
    for score in scores:
        final_score = []
        for i in arr:
            final_score.append(i+score)
        for j in final_score:
            if j not in arr:
                arr.append(j)
    print(f'#{tc} {len(arr)}')




