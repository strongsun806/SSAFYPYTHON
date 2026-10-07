import sys
sys.stdin = open("sample_input.txt","r")

T = int(input())
for tc in range(1,T+1):
    N,M=map(int,input().split())
    pizzas=list(map(int,input().split()))

    def solve(N,pizzas):
        hwaduck_in=[0]*N
        pizza_num=1
        hwaduck_in[0]=pizza_num
        hwaduck=[-1]*N
        hwaduck[0]=pizzas.pop(0)
        now=0
        last_num=0
        
        while sum(hwaduck_in)!=0:
            last_num=sum(hwaduck_in)
            now+=1
            now%=N
            if hwaduck_in[now]==0:
                if pizzas :
                    pizza_num+=1
                    hwaduck_in[now]=pizza_num
                    hwaduck[now]=pizzas.pop(0)
            elif hwaduck[now]!=-1:
                hwaduck[now]//=2
                if hwaduck[now]==0:
                    hwaduck_in[now]=0
                    hwaduck[now]=-1
                    if pizzas :
                        pizza_num+=1
                        hwaduck_in[now]=pizza_num
                        hwaduck[now]=pizzas.pop(0)
        return last_num
    print(f"#{tc} {solve(N,pizzas)}")
