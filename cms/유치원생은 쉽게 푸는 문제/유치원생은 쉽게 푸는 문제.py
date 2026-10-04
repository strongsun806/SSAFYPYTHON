import sys
sys.stdin = open("1_sample_input.txt","r")

T = int(input())
for tc  in range(1,T+1):
    X = int(input())
    eight = X//2
    v_1 = X%2
    result = None
    if eight ==0 and v_1 ==1:
        result = '0'
    else :
        result = '4'*v_1+'8'*eight
    print(int(result))