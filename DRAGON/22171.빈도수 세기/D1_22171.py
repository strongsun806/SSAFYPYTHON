
test_data = [8, [1, 2, 3, 2, 1, 3, 2, 1]]
N = test_data[0] 
numbers = test_data[1] 

max_num = numbers[0] #최대값 초기화
for i in range(1, len(numbers)):
    if numbers[i] > max_num: #지금 숫자가 최대값보다 크다면
        max_num = numbers[i] #최대값 갱신

count = [] #빈도수를 저장할 빈 리스트 생성
for i in range(max_num + 1): #0부터 최대값까지의 크기로 반복
    count.append(0) #빈도수 초기화


for i in range(len(numbers)):
    val = numbers[i]
    count[val] = count[val] + 1


for i in range(len(count)):
    if count[i] > 0:
        print(f"{i} {count[i]}")