import sys
sys.stdin = open("input.txt","r")
 
for tc in range(1, 11):
    N, nums = input().split()
    stack =[0]*int(N)
    top = -1
    for num in nums:
        # 스택의 마지막 번호와 현재 번호가 같으면 쌍을 소거
        if top>=0 and stack[top] == num:
            top -= 1
        else:
            top += 1
            stack[top] = num
 
    pw = ''.join(stack[:top+1])
 
    print(f"#{tc} {pw}")