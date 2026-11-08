import sys
sys.stdin = open("sample_input.txt","r")

T=int(input())
for tc in range(1,T+1):
    N = int(input())
    heap=[0]*(N+1)
    last=0
    arr = list(map(int,input().split()))

    def enq(n):
        global last
        last +=1
        heap[last]=n
        c = last
        p = c//2
        while p and heap[p]>heap[c]:
            heap[p],heap[c] = heap[c], heap[p]
            c = p
            p = c//2

    for x in arr:
        enq(x)

    result=0
    p=last//2
    while p>=1:
        result += heap[p]
        p//=2


    print(f"#{tc} {result}")