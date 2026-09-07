import sys
sys.stdin = open("sample_input.txt", "r")

# 테스트 케이스 갯수 할당
T= int(input())
for test_case in range(1,T+1):
    # 각 자리의 숫자를 수정하기 쉽도록 문자열 리스트로 변환    
    bin_lst = []
    ter_lst = []
    for i in str(input()) :
        bin_lst.append(i)
    for i in str(input()) :
        ter_lst.append(i)

    # 2진수 값과 3진수 값에서 한 자리가 바뀐 값을 10진수로 저장할 세트 할당
    bin_value = set()
    ter_value = set()

    # 2진수 값에서 한 자리씩 바꿔보기
    for i in range(len(bin_lst)) :
        bin_lst[i] = str((int(bin_lst[i])+1) % 2)
        # 첫 번째 자리가 0인 경우는 제외
        if bin_lst[0] != "0":
            bin_value.add(int(''.join(map(str, bin_lst)), 2))
        # 바꾼 자리 숫자 원상복구
        bin_lst[i] = str((int(bin_lst[i])-1) % 2)

    # 3진수 값에서 한 자리씩 바꿔보기
    for j in range(len(ter_lst)):
        # 3진수는 자리 당 0,1,2 로 바뀔 수 있으므로 2번 바꾸기
        for k in range(1,3):
            ter_lst[j] = str((int(ter_lst[j])+k) % 3)
            # 첫 번째 자리가 0인 경우는 제외
            if ter_lst[0] != "0":
                ter_value.add(int(''.join(map(str, ter_lst)), 3))
            # 바꾼 자리 숫자 원상복구
            ter_lst[j] = str((int(ter_lst[j])-k) % 3)

    # bin_value와 ter_value 세트에서 공통인 부분을 찾고, 리스트로 바꾼 후, 그 값을 pop()으로 result에 할당
    result = list(bin_value & ter_value).pop()

    print(f"#{test_case} {result}")