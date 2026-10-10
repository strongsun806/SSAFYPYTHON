# 부분집합(sub set)

# 부분집합의 모든 모양 구하기
arr = ['A', 'B', 'C']
N = len(arr)

bit = [0] * N  # 숫자의 비트 모양이랑 똑같음 == 부분집합의 모양
# bit의 모든 인덱스에 넣을 수 있는거 다 넣어보기

# bit[0] < 0, 1
# bit[1] < 0, 1
# bit[2] < 0, 1
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
# -> 3개로 정해져있어서 3중 for문으로 나왔기 때문에 풀만한거임(숫자 자체도 큰건 아님)
# 만약 정해져있지 않은 개수거나, 그 값 자체가 크다면? -> 재귀 사용하기

# index번 자리에 0 또는 1을 넣기를 해야함
# 이후에 index + 1자리에 넣기
# -> 이걸 반복해야함

# index번째에 0 또는 1넣기
def zero_one(idx):
    # idx N-1번까지는 동작하는데 N번되면 에러가 남
    # -> 기저조건 넣기
    if idx == N:
        # print(bit)
        # 부분집합의 모양을 구했으니까 이걸 가지고 이 모양대로 부분집합 출력하면 됨 ㅇㅇ
        print('[', end = ' ')
        for i in range(N):
            if bit[i]:
                print(arr[i], end = ' ')
        print(']')
        return

    for i in range(2):
        bit[idx] = i
        zero_one(idx + 1)

zero_one(0)

# [ ]
# [ C ]
# [ B ]
# [ B C ]
# [ A ]
# [ A C ]
# [ A B ]
# [ A B C ]

