
test_data = [7, [8, 3, 12, 7, 5, 11, 2]]
N = test_data[0]
numbers = test_data[1]

max_val = numbers[0] # 최대값 초기설정
min_val = numbers[0] # 최소값을 초기설정

for i in range(1, len(numbers)): #최대값
    if numbers[i] > max_val:
        max_val = numbers[i]
        
    if numbers[i] < min_val: #최소값
        min_val = numbers[i]


print(f"{max_val} {min_val}")