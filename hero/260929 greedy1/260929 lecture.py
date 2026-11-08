# SW문제해결 응용 완전탐색

# 8p
# 1, 2, 3으로 만들 수 있는 두 자릿수 코드
for a in range(1, 4):
    for b in range(1, 4):
        print(a, b)

# 10p
# 1, 2, 3을 이용한 네 자릿수를 출력하는 코드
# 완전 오리지널한 코드
for a in range(1, 4):
    for b in range(1, 4):
        for c in range(1, 4):
            for d in range(1, 4):
                print(a, b, c, d)
# -> N개의 for문을 모두 적을 수는 없는 방법임
# -> 재귀호출 사용

# 11p
# 1, 2, 3을 이용한 N자릿수를 출력하는 코드
path = []
N = 3

def run(k):
    if k == N:
        print(" ".join(path))
        return
    for i in range(1, 4):  # 1부터 3까지
        path.append(str(i))
        run(k + 1)
        path.pop()

run(0)

# 13p
# 재귀 연습 전, 알아야 할 함수의 특징 1
# KFC1 함수 호출할 때, int 타입 객체를 전달하면 값만 복사됨
def KFC1(a):
    print(a)  # 4
    a += 1
    print(a)  # 5

x = 3
KFC1(x+1)
print(x)  # 3 (4가 아님!)

# 15p
# 재귀 연습 전, 알아야 할 함수의 특징 2
# BTS1 함수가 끝나면, Main으로 돌아오는 것이 아니라,
# 해당 함수를 호출했던 곳으로 돌아옴
def BTS1(a):
    a += 10
    print(a)  # 19

def KFC2(a):
    print(a)  # 4
    a += 3  # 7
    BTS1(a + 2)  # BTS1(9)
    print(a)  # 7

x = 3
KFC2(x + 1)  # KFC2(4)
print(x)  # 3

# 17p
# 무한 재귀호출(안되는거 확인하기)
def KFC3(a):
    KFC3(a + 1)

# KFC3(0)  # RecursionError: maximum recursion depth exceeded

# 재귀호출 -> 무한 재귀호출 막는것부터 시작 : 기저조건(base case)
def KFC4(a):
    if a == 2:
        return

    print(a)
    KFC4(a + 1)
    print(a)

KFC4(0)
print('이 문구가 출력되었다면, 무한 재귀호출 없이 정상 동작')

# 19p
# 0 1 2 3 4 5 5 4 3 2 1 0 을 재귀호출을 이용하여 구현
N = 5

def recu1(k):
    print(k, end = ' ')
    if k == N:
        print(k, end = ' ')
        return

    recu1(k + 1)
    print(k, end = ' ')

# recu1(0)


# 20p
# KFC5 함수 내부에 KFC5(a + 1) 재귀호출 코드가 하나인 경우
def KFC5(a):
    if a == 2:
        return
    KFC5(a + 1)
    print(a, end = ' ')
    
# KFC5(0)  # 1 0

# 21p
# KFC6 함수 내부에 KFC6(a + 1) 재귀호출 코드가 둘인 경우(이건 복잡해서 교재 그림 보는거 개강추 22p~)
def KFC6(a):
    if a == 2:
        return
    KFC6(a + 1)
    KFC6(a + 1)
    print(a, end = ' ')

# KFC6(0)  # 1 1 0

# 25p
# depth 3, 재귀호출 개수 4개인 경우 그림 그려보기
def KFC7(a):
    if a == 3:
        return

    # KFC7(a + 1)
    # KFC7(a + 1)
    # KFC7(a + 1)
    # KFC7(a + 1)
    for i in range(4):
        KFC7(a + 1)
    print(a, end = ' ')

KFC7(0)
# 그림은 이런식으로 그리면 됨
# depth의 숫자만큼의 층이 있고, 각 층마다 재귀호출 개수만큼의 자식들이 각각 생김
# -> 층의 개수를 a, 재귀호출 개수를 b라고 둔다면
#    맨 밑에 자식들은 b ** (a - 1) 개라고 보면 될듯 ㅇㅇ