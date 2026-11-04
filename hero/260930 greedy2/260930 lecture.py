name = "ABC"

def abc(level, path):
    if level == 3:
        print(*path)
        return

    abc(level + 1, path)
    abc(level + 1, path + [name[level]])

abc(0, [])



# 16p
# 부분집합들 만드는 과정
arr = ['A', 'B', 'C']
N = len(arr)

def get_sub(target):
    for i in range(N):
        if target & 0x1:
            print(arr[i], end = ' ')
        target >>= 1

for tar in range(2 ** N):
# for tar in range(1 << N):
    print('{', end = ' ')
    get_sub(tar)
    print('}')