import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    def make_list(number):
        listed = []
        for numbers in number:
            listed.append(int(numbers))
        return listed


    bin_num_list=make_list(input())#[1,0,1,0]
    
    tri_num_list=make_list(input())#[2,1,2]


   

    # print(bin_num,tri_num)
    def to_dec(number_list,jinbeob):#십진법 만들기 함수!
        
        listed=number_list[::-1]#0101
        dec_num=0        
        for j in range(len(listed)):
            dec_num += listed[j]*(jinbeob**j)
        return dec_num
    # print(to_dec(tri_num_list,3))
    #진법 가능수 리스트 만들기
    def can_num(number_list, jinbeob):
        can_be = []
        for i in range(len(number_list)):
            original = number_list[i]
            # 해당 진법에서 가능한 모든 숫자(0 ~ jinbeob-1) 대입
            for j in range(jinbeob):
                if original != j:  # 원래 숫자와 다를 때만 교체
                    temp_list = list(number_list)  # 복사본 생성
                    temp_list[i] = j
                    can_be.append(to_dec(temp_list, jinbeob))
        return can_be
    answer_list=set(can_num(bin_num_list,2))&set(can_num(tri_num_list,3))#교집합
    for i in answer_list:
        print(f'#{test_case} {i}')