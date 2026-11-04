import sys
sys.stdin = open("GNS_test_input.txt","r")

num_dict = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4,'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}

def counting_sort(numbers):
    # 카운팅정렬 : 내 자리찾기(내앞에 몇개 있냐?)
    # 1. 각 숫자가 몇번 나왔는지 센다
    cnt = [0]*10
    for i in range(N):
        # numbers[i]   ZRO, SIX....
        # cnt[num_dict[numbers[i]]] +=1
        str_num = numbers[i]
        num = num_dict[str_num]
        cnt[num] += 1
    # 2. 누적합 구하기 : 각 숫자 앞에 몇개 있는지 자리 찾기
    for i in range(1,10):
        # cnt[i] = cnt[i-1] + cnt[i]
        cnt[i] += cnt[i-1] 
    # 3. 자리에 맞게 새로운 배열에 넣어주기
    sorted_arr = [None]*N
    # 원본 배열에 있는 숫자 보면서자기 자리 찾아서 넣어주기
    for i in range(N):
        cnt[num_dict[numbers[i]]] -=1  # 내 순번이니까 인덱스는 -1
        sorted_arr[cnt[num_dict[numbers[i]]]] = numbers[i]
    return sorted_arr

T = int(input())
for _ in range(T):
    tc, N = input().split()
    N = int(N)
    numbers = input().split()
    numbers = counting_sort(numbers)
    print(f"{tc}\n{numbers}")
    