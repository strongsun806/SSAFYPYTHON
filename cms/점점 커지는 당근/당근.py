import sys
sys.stdin = open("carrot_sample_in.txt","r")

T = int(input())
for tc in range(1,T+1):
    N= int(input())
    carrots = list(map(int,input().split()))
    length = 1
    max_length =1

    for i in range(1,N):
        # 현재 당근의 크기가 이전 당근보다 작거나 같으면
        # 증가하는 구간이 끝난거니 구간의 길이가 몇인지 확인
        if carrots[i]>carrots[i-1]:
            length+=1
        else:
            if length>max_length:
                max_length=length
            # 최장구간 여부와 관계없이 구간의 길이는 초기화
            length=1
    # data가 끝나면 작아지는 당근이없어서 계산이 안될 수 있음
    if length> max_length:
        max_length=length

    print(f"#{tc} {max_length}")