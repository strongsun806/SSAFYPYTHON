import sys
sys.stdin = open("sample_input.txt","r")

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    ans = 0
    for ch1 in str1:
        cnt = 0
        for ch2 in str2 :
            if ch2 == ch1:
                cnt += 1
        if cnt > ans:
            ans = cnt
    print(f"#{tc} {ans}")