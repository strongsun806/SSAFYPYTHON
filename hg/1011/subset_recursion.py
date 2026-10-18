# 민철이에게는 세 명의 친구가 있다
# {MIN, CO, TIM}
#함께 영화관에 갈 수 있는 멤버 구성할거임
# 모든 경우의 수
# 완전 탐색을 이용해서 구현 -> 데려간다/만다
# 코드 구현 - 브랜치 2개 레벨 3개

arr = ['O', 'X']
path = []
name = ['MIN', 'CO', 'TIM']


def print_name():
    print('{', end='')
    for i in range(3):
        if path[i] == '0':
            print(name[i], end=' ')
    print('}')

def run(lev):
    # 3개를 뽑았을 때 출력
    if lev == 3:
        print_name()
        return
    
    for i in range(2):
        path.append(arr[i])
        run(lev+1)
        path.pop()
        

run(0)