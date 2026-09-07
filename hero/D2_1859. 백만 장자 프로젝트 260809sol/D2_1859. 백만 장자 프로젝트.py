import sys
from io import StringIO

sys.stdin = StringIO("""3
3
10 7 6
3
3 5 9
5
1 1 3 1 2
""")

#import sys
#sys.stdin = open("input.txt", "r")

T = int(input())  # T = 3
for test_case in range(1, T+1):
    days = int(input()) # 결국 안썼지만, input은 받아야해서 적음
    list_price = list(map(int, input().split()))
    # 이전에 산 가격보다 나중 가격이 비싸야함 -> 근데 이건 만약에 억지 계산식을 만들면 최댓값찾기로 걸러낼 수 있음
    # 리스트 순회하면서 (인덱스 값이 더 큰 데이터) - (상대적으로 인덱스 값이 더 작은 데이터)

    # 일단 최댓값찾고 해당 데이터의 인덱스 찾기
    # -> 그 인덱스보다 작은 인덱스들의 데이터를 최댓값에서 빼서 담기(데이터 뺄셈 후 += 하면 될 듯)
    # -> List.pop(index)를 이용해보고싶음
    # -> 남은 애들은 다시 0번부터 시작되는 리스트로 남을테니까 이걸 리스트가 empty될 때까지 반복
    # -> empty 상태가 되면 종료(이거 boolean값으로 해보고싶음)
    # -> 담아둔 값 출력 print(f'#{test_case} {빼기 후 더한 데이터}')
  
    # income = 0
    # while list_price: # list_price에 pop을 적용해서 리스트가 empty할때까지 계속 하겠다는거임

    #     max_price_1 = 0
    #     for i in list_price:
    #         if i >= max_price_1:
    #             max_price_1 = i  # max값 찾기
    #     index_max_price_1 = list_price.index(max_price_1) # max데이터의 index값 찾기
        
    #     for i in range(index_max_price_1): # max데이터의 index만큼의 길이를 반복할거임
    #         income += max_price_1 - list_price.pop(0)
    #         # max값 직전까지 pop(0)을 하면서 리스트 내용 삭제와 동시에 남은 값들 가지고 이어서 할 수 있도록 조치했음
    #         # income에는 최댓값에서 pop한 값을 뺀 값을 더해주면서 누적으로 저장했음
    
    #     list_price.remove(max_price_1)
    #     # 위의 동작을 하면 10 7 6 과 같이 제일 큰 숫자가 맨 앞에 남게되는데, 다음 반복을 위해서 삭제하는거임
    #     # 이때는 인덱스가 아닌, 처음 나온 x값을 지우는 List.remove(x)를 사용했음. 나 좀 잘 생각한듯 ㅋ

    # print(f'#{test_case} {income}')

    # --> 이렇게하니까 시간초과로 10개중 7개만 통과됐다고 뜸 하;;


    # 리스트를 줄일 때마다 최댓값을 다시 찾고 앞 원소를 제거해서, 같은 원소들을 계속 순회/이동한 것이 문제
    # 조금 더 구체적으로 보면,
    # for i in list_price : 최댓값을 구할 때마다 남은 리스트 '전체'응 다시 확인함.
    # list_price.pop(0) : 첫 원소를 지운 후 나머지 원소들을 한 칸씩 앞으로 옮김.
    # list_price.remove(max_price_1) : 최댓값의 위치를 처음부터 다시 찾은 후 해당 원소를 삭제함.
    # 이 작업들이 while 구문 안에서 반복되어 전체 실행 시간이 O(N^2)까지 증가했음
    # 리스트 전체를 한 번 보는 작업을 원소를 하나씩 지울 때마다 또 반복해서 결국 N번 확인 × N번 반복 = N²
    # -> 한 번만 하도록 순회하도록 로직짜기
    # How?
    # 뒤에서부터 역순으로 판단하기
    # 1. 맨 뒤의 값을 일단 최대치로 두기
    # 2. 최대치로 일단 둔 값보다 더 큰 값이 나오기 전까지는 빼준값을 누적으로 더하기
    # 3. 최대치보다 큰 값이 나오면 최대치를 갱신하고 이를 반복하기

    income = 0
    max_price = list_price[-1] # list[-1] == list[len(list_price)-1]
    for i in range(len(list_price)):
        if list_price[-1-i] <= max_price:
            income += max_price - list_price[-1-i]
        else: # list_price[-1-i] > max_price:
            max_price = list_price[-1-i]
    print(f'#{test_case} {income}')