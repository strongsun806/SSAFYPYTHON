# 입력
# 1       // Test Case 수
# 1010    // Test Case 1, 2진수
# 212 	  // Test Case 1, 3진수

# 출력
#  #1 14  // Test case 1의 정답


import sys
sys.stdin = open("D4_4366. 정식이의 은행업무/sample_input.txt", "r")

T = int(input()) # 1 총 테스트 개수
# # 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1): # input은 2번 받아야함
    binary_input = list(map(int, (input())))
    ternary_input = list(map(int, (input())))
    binary_input.reverse() # list의 index값을 역순으로 바꿔서 index값 자체를 지수로 쓰기 위함
    ternary_input.reverse()

    # print(binary_input)
    # print(ternary_input)

    set_bi = set()
    for a in range(len(binary_input)):
        if binary_input[a] == 0:
            binary_input[a] = 1
            decimal_bi = 0
            for index in range(len(binary_input)):
                decimal_bi += binary_input[index] * (2 ** index)
            set_bi.add(decimal_bi)
            binary_input[a] = 0 # 다시 되돌려놓기

        elif binary_input[a] == 1:
            binary_input[a] = 0
            decimal_bi = 0
            for index in range(len(binary_input)):
                decimal_bi += binary_input[index] * (2 ** index)
            set_bi.add(decimal_bi)
            binary_input[a] = 1 # 다시 되돌려놓기

    # print(set_bi)

    set_ter = set()
    for a in range(len(ternary_input)):
        if ternary_input[a] == 0:
            ternary_input[a] = 1
            decimal_ter = 0
            for index in range(len(ternary_input)):
                decimal_ter += ternary_input[index] * (3 ** index)
            set_ter.add(decimal_ter)
            ternary_input[a] = 0 # 다시 되돌려놓기, 여기선 필요없을듯

            ternary_input[a] = 2
            decimal_ter = 0
            for index in range(len(ternary_input)):
                decimal_ter += ternary_input[index] * (3 ** index)
            set_ter.add(decimal_ter)
            ternary_input[a] = 0 # 다시 되돌려놓기, 여기선 필요없을듯           


        elif ternary_input[a] == 1:
            ternary_input[a] = 2
            decimal_ter = 0
            for index in range(len(ternary_input)):
                decimal_ter += ternary_input[index] * (3 ** index)
            set_ter.add(decimal_ter)
            ternary_input[a] = 1 # 다시 되돌려놓기, 여기선 필요없을듯

            ternary_input[a] = 0
            decimal_ter = 0
            for index in range(len(ternary_input)):
                decimal_ter += ternary_input[index] * (3 ** index)
            set_ter.add(decimal_ter)
            ternary_input[a] = 1 # 다시 되돌려놓기, 여기선 필요없을듯     


        elif ternary_input[a] == 2:
            ternary_input[a] = 0
            decimal_ter = 0
            for index in range(len(ternary_input)):
                decimal_ter += ternary_input[index] * (3 ** index)
            set_ter.add(decimal_ter)
            ternary_input[a] = 2 # 다시 되돌려놓기, 여기선 필요없을듯

            ternary_input[a] = 1
            decimal_ter = 0
            for index in range(len(ternary_input)):
                decimal_ter += ternary_input[index] * (3 ** index)
            set_ter.add(decimal_ter)
            ternary_input[a] = 2 # 다시 되돌려놓기, 여기선 필요없을듯     

    # print(set_ter)

    if set_bi & set_ter:
        print(f'#{test_case} {(set_bi & set_ter).pop()}')












    # # 2진수를 10진수로
    # decimal_bi = 0
    # for index in range(len(binary_input)):
    #     decimal_bi += binary_input[index] * (2 ** index)
    # # print(decimal_bi)

    # # 3진수를 10진수로
    # decimal_ter = 0
    # for index in range(len(ternary_input)):
    #     decimal_ter += ternary_input[index] * (3 ** index)
    # # print(decimal_ter)

    # # N진수를 10진수로
    # decimal_Nth = 0
    # for index in range(len(Nth_input)):
    #     decimal_Nth += Nth_input[index] * (N ** index)
    # print(decimal_Nth)    

    # # 함수로도 만들어봄 
    # def N_to_decimal(number, N):
    #     decimal_Nth = 0
    #     a = list(str(number))
    #     a.reverse()
    #     for index in range(len(a)):
    #         decimal_Nth += int(a[index]) * (N ** index)
    #     print(decimal_Nth) 

    # N_to_decimal(212, 3)

    # 근데 사실
    # int("1010", 2)  # 10
    # int(문자열, n진법) # 10진수로 표현하는 방법이 있었음


    # for a in range(len(binary_input)):
    #     for b in range(len(ternary_input)):
    #         decimal_bi = 0
    #         decimal_ter = 0            
    #         if binary_input[a] == 0:
    #             binary_input[a] = 1
    #             for index in range(len(binary_input)):
    #                 decimal_bi += binary_input[index] * (2 ** index)
    #             binary_input[a] = 0           
    #         elif binary_input[a] == 1:
    #             binary_input[a] = 0
    #             for index in range(len(binary_input)):
    #                 decimal_bi += binary_input[index] * (2 ** index)
    #             binary_input[a] = 1

    #         if ternary_input[b] == 0:
    #             ternary_input[b] = 1
    #             for index in range(len(ternary_input)):
    #                 decimal_ter += ternary_input[index] * (3 ** index)
    #             ternary_input[b] = 0
    #             if decimal_bi == decimal_ter:
    #                 print(decimal_bi) 
    #             # print(decimal_bi, decimal_ter)

    #             ternary_input[b] = 2
    #             for index in range(len(ternary_input)):
    #                 decimal_ter += ternary_input[index] * (3 ** index)
    #             ternary_input[b] = 0
    #             if decimal_bi == decimal_ter:
    #                 print(decimal_bi) 
    #                 # print(decimal_bi, decimal_ter)

    #         elif ternary_input[b] == 1:
    #             ternary_input[b] = 2
    #             for index in range(len(ternary_input)):
    #                 decimal_ter += ternary_input[index] * (3 ** index)
    #             ternary_input[b] = 1
    #             if decimal_bi == decimal_ter:
    #                 print(decimal_bi) 
    #                 # print(decimal_bi, decimal_ter)

    #             ternary_input[b] = 0
    #             for index in range(len(ternary_input)):
    #                 decimal_ter += ternary_input[index] * (3 ** index)
    #             ternary_input[b] = 1
    #             if decimal_bi == decimal_ter:
    #                 print(decimal_bi) 
    #                 # print(decimal_bi, decimal_ter)

    #         elif ternary_input[b] == 2:
    #             ternary_input[b] = 0
    #             for index in range(len(ternary_input)):
    #                 decimal_ter += ternary_input[index] * (3 ** index)
    #             ternary_input[b] = 2
    #             if decimal_bi == decimal_ter:
    #                 print(decimal_bi) 
    #                 # print(decimal_bi, decimal_ter)                    

    #             ternary_input[b] = 1
    #             for index in range(len(ternary_input)):
    #                 decimal_ter += ternary_input[index] * (3 ** index)
    #             ternary_input[b] = 2
    #             if decimal_bi == decimal_ter:
    #                 print(decimal_bi) 
    #             print(decimal_bi, decimal_ter)

