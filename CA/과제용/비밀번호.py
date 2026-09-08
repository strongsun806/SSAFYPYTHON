import sys
sys.stdin = open("input10.txt","r")
T = 10

for tc in range(1, T + 1):
    N_str, numbers = input().split()
    N = int(N_str)
    
    stack = [0] * N
    top = -1
    
    i = 0
    while i < len(numbers):
        char = numbers[i]
        
        if top >= 0 and stack[top] == char:
            top -= 1
        else:
            top += 1
            stack[top] = char
            
        i += 1
        
    result = "".join(stack[:top + 1])
    print(f"#{tc} {result}")