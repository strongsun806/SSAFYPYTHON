import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    scores = list(map(int, input().split()))

    possible = {0}

    for score in scores:
        new_scores = []

        for x in possible:
            new_scores.append(x + score)

        for x in new_scores:
            possible.add(x)

    print(f'#{tc} {len(possible)}')