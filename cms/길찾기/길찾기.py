import sys
sys.stdin = open("input.txt","r")

for _ in range(1,11):
    tc, E= map(int,input().split())
    nums = list(map(int,input().split()))

    ls = list([[],[]] for _ in range(100))
    for i in range(0,E*2,2):
        if ls[nums[i]][0]:
            ls[nums[i]][1]=nums[i+1]
        else:
            ls[nums[i]][0]=nums[i+1]

    stack =[]
    stack.append(0)
    visited=[0 for _ in range(100)]
    visited[0]=1
    result = 0
    while stack:
        current = stack[-1]
        for j in range(2):
            if ls[current][j] and visited[ls[current][j]]==0:
                stack.append(ls[current][j])
                visited[ls[current][j]]=1
                break
        else :
            stack.pop()
        if visited[99]==1:
            result = 1
            break
            
    print(f"#{tc} {result}")
            
        
