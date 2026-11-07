# 정사각형 판정

def is_square(array, N):
    row_min, col_min, row_max, col_max =  N, N, -1, -1
 
    for row in range(N):
        for col in range(N):
            if array[row][col] == '#':
                row_min = min(row_min, row)
                col_min = min(col_min, col)
                row_max = max(row_max, row)
                col_max = max(col_max, col)
 
    height = row_max - row_min + 1
    weight = col_max - col_min + 1
 
    if weight != height:
        return 'no'
     
    for row in range(row_min, row_max + 1):
        for col in range(col_min, col_max + 1):
            if array[row][col] != '#':
                return 'no'
    else:
        return 'yes'
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    array = []
    for i in range(N):
        array.append(input())
 
    print(f'#{tc} {is_square(array, N)}')