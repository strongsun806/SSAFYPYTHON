o_b = {
    '0':'000', '1':'001', '2':'010', '3':'011', 
    '4':'100', '5':'101', '6':'110', '7':'111', 
}

T = int(input())
for tc in range(1, T+1):
    N, oct_str = input().split()
    
    ans = ""
    
    for char in o_b:
        ans += o_b[char]
        
    print(f"#{tc} {ans}")
    
    