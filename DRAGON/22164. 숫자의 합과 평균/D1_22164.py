
test_data = [5, [1, 2, 3, 4, 5]]
N = test_data[0]
numbers = test_data[1]

total_sum = 0 #초기화

for i in range(len(numbers)):
    total_sum = total_sum + numbers[i] # 숫자를 하나씩 꺼내서 합계에 누적

average = total_sum // N #전체 합 / 갯수 (평균)

print(f"{total_sum} {average}")