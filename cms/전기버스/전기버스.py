import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for test_case in range(1, T+1):
    K,N,M= map(int,input().split())
    station = [0]*N
    char_st = list(map(int, input().split()))
    
    for i in char_st:
        station[i] = 1
    now = 0
    char_count = 0

    while now+K < N :
        can_pass = False
        for char in range(now+K,now,-1):
            if station[char] == 1 :
                now = char
                char_count += 1
                can_pass = True
                break
        if can_pass == False:
            char_count = 0
            break
        
        

    print(f"#{test_case} {char_count}")

        