T= int(input())
for tc in range(1, T+1):

    def enq(n):
        global last
        last +=1    # 마지막 정점 추가
        heap[last] = n  #마지막 정점에 저장

        #최소힙 : 부모 < 자식
        c = last
        p = c//2
        # 부모가 있고, 부모 > 자식 이면 교환
        while p and heap[p] > heap[c]:
            heap[p], heap[c] = heap[c], heap[p]
            c = p   # 부모와 부모의 부모를 비교
            p = c//2



    N = int(input())
    arr = list(map(int,input().split()))

    heap= [0]*(N+1)   # N개의 정점, 완전이진트리
    last = 0    #마지막 정점 번호

    for x in arr:
        enq(x)

    print(heap)

