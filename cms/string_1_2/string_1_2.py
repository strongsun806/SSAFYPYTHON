import sys
sys.stdin = open("sample_input.txt","r")

T= int(input())
for tc in range(1,T+1):
    A, B = input().split()
    length = len(A)
    i = 0
    cnt = 0
    while length > i :
        if i + len(B) <= length:
            for j in range(len(B)):
                if A[i+j] != B[j]:
                    i += 1
                    break
            else : 
                i+= len(B)
        else :
            i+=1
        cnt +=1


    print(f"#{tc} {cnt}")
