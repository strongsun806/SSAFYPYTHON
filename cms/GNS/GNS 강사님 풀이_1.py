import sys
sys.stdin = open("GNS_test_input.txt","r")

num_dict = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4,'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}

# 인자로 대상 배열 받아서 정렬한 다음 반환하기
def bubble_sort(numbers):
    # ㅇ펴에 있는거 끼리 비교해서 큰거 뒤로 보내기 * N-1번
    for  i in range(N-1):
        for j in range(N-1):
            # j번과 j+1번이랑 비교
            # numbers[j]와 numbers[j+1]은 둘다 문자열이라서 비교안됨
            # num_dict를 활용해서 비교
            if num_dict[numbers[j]] > num_dict[numbers[j+1]]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

T = int(input())
for _ in range(T):
    tc, N = input().split()
    N = int(N)
    numbers = input().split()
    bubble_sort(numbers)
    print(f"{tc}\n{numbers}")
    