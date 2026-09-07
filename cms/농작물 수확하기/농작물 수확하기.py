import sys
sys.stdin = open("input.txt", "r")

T = int(input())  # 케이스 개수
for test_case in range(1, T + 1):
    N = int(input())  # 농장 크기 N 입력
    if N != 1 :  # N의 크기에 따라 중간 행을 찾는 index 값을 ctr_idx에 할당
        ctl_idx = ((N+1) // 2) -1
    else : 
        ctl_idx = 0  #농장 크기가 1 인 경우, ctl_idx = 0 
    harvest = 0  # 수확량 초기값에 0 할당
    for i in range(N) : #농장 크기(행 개수) 만큼 for 반복문 실행
        pre_list = []  # 한 행씩 수익을 요소로 담을 리스트 pre_list 생성
        for num in input():  # input으로 받은 숫자를 for 반복문으로 pre_list에 추가
            pre_list.append(int(num))  
        if i <= ctl_idx:  # 중앙 행의 index 값을 기준으로, 작거나 같으면
            harvest += sum(pre_list[ctl_idx-i:ctl_idx+i+1])  # pre_list에서 [중앙 index - 1 : 중앙 인덱스 + i + 1]로 슬라이스하고, 그 합을 수확량에 더한다.
        else :  # 중앙 행의 index 값보다 크면
            harvest += sum(pre_list[i-ctl_idx:3*ctl_idx-i+1]) # pre_list에서 [i - 중앙 index :3 * 중앙 인덱스 - i + 1)]로 슬라이스하고, 그 합을 수확량에 더한다.
    print(f'#{test_case} {harvest}')






