import sys
sys.stdin = open("sample_input.txt")


def cut(mapping):
    total = 0
    base = 0
    for x in range(len(mapping)):
        if mapping[x] == '(':
            base += 1
        elif mapping[x] ==')' and mapping[x-1]=='(':
            base -=1
            total += base
        else :
            base -=1
            total += 1
    return total

T=int(input())
for tc in range(1, T+1):
    arr=input()
    print(f"#{tc} {cut(arr)}")