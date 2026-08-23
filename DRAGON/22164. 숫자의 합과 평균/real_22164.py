N = int(input()) #이렇게만 써도 여러값넣을 수 있는건가
#두번쨰줄 input() 넣는거. 
#근데 어떤 input에는 하나의 값만, 다른input에는 여러개의 값 넣는게 가능한가?
numbers=int(input().split())
# 5 //3 7 1 3 6
count=0
CHECK=[]
while CHECK == numbers:
    CHECK.append(numbers[count])
    count += 1
print (count)
num_sum = 0 # N값에 넣은 숫자들을 합하는걸 어떻게 적지..아니지 
#만약 str정수형으로 바꾸고 리스트? 그안에 위치 
#if [a,b,c,d,e] 라면 a+b+c+d+e 이렇게 적어야할듯

for i in range(N):#0 1 2 3 4
    num_sum += numbers[i]


num_average = num_sum/N #len 쓰면 끝인디 흠..
#그렇다면 num_sum / N에 몇개있는지 세는걸 적어야함
#두번째줄 input에 몇개 적었는지 바로 count해주는 걸 적어줘야하나??

print(f'{num_sum} {num_average}')
