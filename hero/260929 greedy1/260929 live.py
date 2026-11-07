# 재귀 이용해서 출력해보기

# 0 1 2 3 2 1 0

# 0 1 2 3 4 5 5 4 3 2 1 0

def abc1(level):
    print(level, end = ' ')
    if level == 3:
        return

    abc1(level + 1)
    print(level, end = ' ')

abc1(0)

# 누적합 구하기 - 재귀 DFS 구현 시 변수를 global 선언하는가? 매개변수에 선언하는가?에 따른 차이
arr = [1, 3, 5, 7]

sum1 = arr[0]

def abc2(level):
    global sum1

    if level == 3:
        print(sum1, end = ' ')
        return

    sum1 += arr[level + 1]
    abc2(level + 1)
    sum1 = arr[level + 1]
    print(sum1, end = ' ')

abc2(0)
# 아직 덜한거임 이어서 하셈 미래의 웅아