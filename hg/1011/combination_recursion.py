# {A, B, C, D, E} 5명 중 3명 뽑을 수 있는 모든 경우의 수
# 3중 for문으로 구현이 가능
# 만약에 5명 중 n명 뽑는 코드는? 몇중 for문? -> N중 for문

# 코드에 start 파라미터 추가해서 조합 소스코드 완성

'''
1. 처음 recur 함수의 start 값은 0이다. 따라서 0~5까지 반복하면서 재귀호출을 한다

2. 만약 i가 3이 선택되는 경우는 재귀 호출할 때 start는 4가 된다. 다음 for문은 4부터 수행


'''

arr = ['A', 'B', 'C', 'D', 'E']

n = 3

path = []

def recur(cnt, start):
    if cnt == n:
        print(*path)
        return

    for i in range(start, len(arr)):
        path.append(arr[i])
        recur(cnt + 1, i+1)
        path.pop()

recur(0,0)
    