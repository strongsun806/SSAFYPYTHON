for tc in range(1, 11):
    test_case = int(input())
    # 암호 길이: 8
    queue = list(map(int, input().split()))
    # 암호 생성
    minus = 1
    # 첫 번째 숫자 index
    num_idx = 0
 
    while True:
        # 숫자 감소
        change_number = max(0, (queue[num_idx] - minus))
        minus += 1
        # 한 사이클 후 초기화
        if minus > 5:
            minus = 1
        # 맨 뒤로 보내기
        queue[num_idx] = change_number
        num_idx = (num_idx + 1) % 8
        # 0일시 암호 도출 - 반복 종료
        if change_number == 0:
            break
 
    print(f'#{test_case}', end=" ")
 
    for i in range(len(queue)):
        print(queue[(num_idx + i) % 8], end=' ')
 
    print()