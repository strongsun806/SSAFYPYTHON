# GNS

# 단어의 순서를 정의한 리스트
num_strs = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

T = int(input())

for test_case in range(1, T+1):
    tc, tclen = input().split()
    text = list(input().split())

    # 각 단어가 몇 번씩 나왔는지 세기
    counts = {num: 0 for num in num_strs}
    for word in text:
        counts[word] += 1

    # 정해진 순서대로 개수만큼 출력 결과 생성
    result = []
    for num in num_strs:
        result.extend([num] * counts[num])

    print(f"{tc}")
    print(' '.join(result))