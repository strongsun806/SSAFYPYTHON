T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    s = input().strip()
    
    # 1. 16진수 한 글자씩 보면서 반전된 2진수 글자를 이어붙이기
    binary = ""
    for x in s:
        if x == '0': binary += "1111"
        elif x == '1': binary += "1110"
        elif x == '2': binary += "1101"
        elif x == '3': binary += "1100"
        elif x == '4': binary += "1011"
        elif x == '5': binary += "1010"
        elif x == '6': binary += "1001"
        elif x == '7': binary += "1000"
        elif x == '8': binary += "0111"
        elif x == '9': binary += "0110"
        elif x == 'A': binary += "0101"
        elif x == 'B': binary += "0100"
        elif x == 'C': binary += "0011"
        elif x == 'D': binary += "0010"
        elif x == 'E': binary += "0001"
        elif x == 'F': binary += "0000"
        
    # 2. 연속된 '1'의 최대 개수 구하기
    max_cnt = 0
    current_cnt = 0
    
    for char in binary:
        if char == '1':
            current_cnt += 1
            # 지금 기록이 최고 기록보다 크면 갈아치우기
            if current_cnt > max_cnt:
                max_cnt = current_cnt
        else:
            # '0'을 만나면 연속이 끊기므로 0으로 초기화
            current_cnt = 0
            
    print(f"#{tc} {max_cnt}")