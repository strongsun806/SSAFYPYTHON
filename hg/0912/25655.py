T = int(input())

for _ in range(T):
    x = int(input().strip())
    
    if x == 1:
        print(0)
    elif x % 2 == 0:
        print("8" * (x // 2))
    else:
        print("4" + "8" * ((x - 1) // 2))