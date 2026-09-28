T = int(input())
for tc in range (1, T+1):

    X, Y = list(map(int,input().split()))
    a = (X + Y)//2
    b = (X - Y)//2

    print(a, b)

    # D3라고 되어있는데 실질적으로는 D1 수준인듯