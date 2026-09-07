
test_data = [3, 4, [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
N = test_data[0] # 행의 수 N 
M = test_data[1] # 열의 수 M

total_sum = 0

for i in range(N):
    row = test_data[2 + i] #2더하는 이유는 1행에서는 행 설정하는곳, 2행은 열 설정하는곳, 3행부터 숫자 쓰는거니깐  2+해야됨
    for j in range(M): 
        total_sum = total_sum + row[j] #누적 합


print(f"{total_sum}")