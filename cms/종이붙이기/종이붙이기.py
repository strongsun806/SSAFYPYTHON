import sys
sys.stdin = open("sample_input.txt","r")

T = int(input())
for tc in range(1,T+1):
    w = int(input())//10
    def find_case(w):
        if w==1:
            return 1
        elif w==2:
            return 3
        else :
            return find_case(w-1)+2*find_case(w-2)
    print(f"#{tc} {find_case(w)}")

