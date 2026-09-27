T = int(input())
for tc in range(1, T +1):
    n, k = map (int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = 0 # 우리는 단어가 몇개가 들어가야하는지 알아야하니까 결과
 
    # 가로에 단어 들어갈 수 있는거 세기
    for i in range(n):
        sum = 0 # 만약 k개의 1을 세면 끝나게
        for j in range(n):
            if arr[i][j] == 1: # 만약 빈칸이 라면? 
                sum += 1 # 빈칸개수 세기
            if arr [i][j] == 0: # 근데 만약  색칠 될수 있다면?
                if sum == k: # 색칠되는거에 만약 k가 들어갈 수 있다면?     
                    result += 1 #결과에 더해주기
                sum = 0 # 아니면 0
        if sum == k: # 색칠되는거에 만약 k가 들어갈 수 있다면?     
            result += 1 #결과에 더해주기
        sum = 0 # 아니면 0
                 
 
    # 세로에 들어갈 수 있는거 세기(가로랑 똑같은데 인덱스만 i,j에서 j,i로 바뀜)
    for i in range(n):
            sum = 0 # 만약 k개의 1을 세면 끝나게
            for j in range(n):
                if arr[j][i] == 1: # 만약 빈칸이 라면? 
                    sum += 1 # 빈칸개수 세기
                if arr [j][i] == 0: # 근데 만약  색칠 될수 있다면?
                    if sum == k: # 색칠되는거에 만약 k가 들어갈 수 있다면?
                        result += 1 #결과에 더해주기
                    sum = 0 # 아니면 0
            if sum == k: # 색칠되는거에 만약 k가 들어갈 수 있다면?     
                result += 1 #결과에 더해주기
            sum = 0 # 아니면 0
         
    print(f'#{tc} {result}')


    # solving club에 들어가있긴 했는데,... 이해를 하고 직접 설계하고 푼건 최근이라 (._.)