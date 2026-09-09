import sys
sys.stdin = open("sample_input.txt","r")

def search(p,t):
    N = len(t)
    M = len(p)
    for i in range(N-M+1):
        for j in range(M):
            if t[i+j] != p[j] :
                break
        else:
            return 1
T = int(input())
for tc in range(1, T+1):
    p = list(input())
    t = list(input())

    ans = 0
    if search(p,t) == 1:
        ans = 1

    print(f"{tc} {ans}")




    
    