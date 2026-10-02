import sys
sys.stdin = open("input.txt","r")

def dec(x):
    
    pass

T= int(input())
for tc in range(1,T+1):
    s,e= map(int,input())
    cnt=0
    for x in range(s,e+1):
        if 