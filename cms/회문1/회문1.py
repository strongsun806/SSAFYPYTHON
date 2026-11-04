import sys
sys.stdin = open("input.txt","r")

def solve(data):
    cnt = 0
    for i in range(8):
        for j in range(8-M+1):
            is_find = True
            for k in range(M//2):
                if data[i][j+k] != data[i][j+M-1-k]:
                    is_find = False
                    break
            if is_find:
                cnt +=1

    for i in range(8):
        for j in range(8-M+1):  
            is_find = True
            for k in range(M//2):
                if data[j+k][i] != data[j+M-1-k][i]:
                    is_find = False
                    break
            if is_find:
                cnt += 1
    return cnt

for tc in range(1, 11):
    M = int(input())
    data = [input().strip() for _ in range(8)]
    result = solve(data)
    print(f"#{tc} {result}")