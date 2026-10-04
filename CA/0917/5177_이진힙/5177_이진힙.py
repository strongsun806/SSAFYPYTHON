T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    listed = list(map(int, input().split()))
    heap = [0]
    for i in range(len(listed)):
        heap.append(listed[i])
        cur = len(heap) - 1
        bumo = cur // 2
        while bumo > 0 and heap[bumo] > heap[cur]:
            heap[bumo], heap[cur] = heap[cur], heap[bumo]
            cur = bumo
            bumo = cur // 2
    chonghap = 0
    cur = N // 2
    while cur > 0:
        chonghap += heap[cur]
        cur = cur // 2
    print(f"#{test_case} {chonghap}")
