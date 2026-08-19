T = int(input())
for test_case in range(1, T+1):
    days = int(input())
    list_price = list(map(int, input().split()))
  
    income = 0
    while list_price:

        max_price_1 = 0
        for i in list_price:
            if i >= max_price_1:
                max_price_1 = i
        index_max_price_1 = list_price.index(max_price_1)
        
        for i in range(index_max_price_1):
            income += max_price_1 - list_price.pop(0)

    
        list_price.remove(max_price_1)

    print(f'#{test_case} {income}')