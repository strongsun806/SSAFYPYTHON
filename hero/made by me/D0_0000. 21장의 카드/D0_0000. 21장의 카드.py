import random
import sys

list_trumpcard = []
list_number = []
for i in range(1, 13 + 1):
    if i == 11:
        list_number.append('J')
    elif i == 12:
        list_number.append('Q')
    elif i == 13:
        list_number.append('K')
    elif i == 1:
        list_number.append('A')
    else:
        list_number.append(str(i))
list_shape = ['♠ ', '◆ ', '♥ ', '♣ ']
for i in list_shape:
    for j in list_number:
        list_trumpcard.append(i+j)
# print(list_trumpcard)

# 랜덤으로 21장 카드 뽑기
choice_random = random.sample(list_trumpcard, 21)

# 플레이어가 마음에 들면 다음으로

# 7x3 배열로 만들어주기
matrix_7x3 = []
list_a = choice_random[:7]
list_b = choice_random[7:14]
list_c = choice_random[14:21]
matrix_7x3 = [list_a, list_b, list_c]

# 게임 시작 안내문구
print("""이 게임은 21장의 트럼프 카드로 하는 게임입니다.
랜덤으로 제시된 21장의 카드 중 당신이 생각한 카드를 맞춰보겠습니다.
게임이 시작되면 제시된 카드 21장 중 한 장을 마음 속으로 생각해두고 답해주시면 됩니다.
답은 1 ~ 3의 자연수로만 입력해주세요.
단 세 번의 질문을 통해 맞춰보겠습니다!
y를 입력하면 카드 셔플 후 게임을 시작합니다.
""")

print()
while True:
    wanna_game = input('게임을 시작하시겠습니까? [y/n]: ')

    if wanna_game in ['y', 'Y', 'ㅇㅇ', 'ㅇ', 'ㅛ', 'n', 'N', 'ㄴㄴ', 'ㄴ']:
        break
    else:
        print('님아 시작부터 이러면 안됨.. ㅠㅡㅠ 다시 입력해줘요..')

if wanna_game in ['y', 'Y', 'ㅇㅇ', 'ㅇ', 'ㅛ']:
    print()
    list_123 = ['첫', '두', '세']
    for i, row in zip(list_123, matrix_7x3):
        print(i+'번째줄' ,*row, sep='  ')

    # 몇 번째 줄에 카드가 있는지 고르기 - 첫번째
    while True:
        choice_1 = input('첫 번째 질문. 1 ~ 3 중 몇 번째 줄에 생각한 카드가 있나요?: ')

        if choice_1 in ['1', '2', '3']:
            break
        else:
            print('님 숫자 모름? 다시 입력하셈 ㅡㅡ')

else:
    print(f'아니 안할거면 왜 눌러본거임 ㅡㅡ\n하고싶으면 다시 시작하셈 ㅡㅡ')
    sys.exit()

next_list_1 = []

if int(choice_1) - 1 == 0: # 첫 번째 줄일 때
    next_list_1.extend(matrix_7x3[1])
    next_list_1.extend(matrix_7x3[0])
    next_list_1.extend(matrix_7x3[2])
elif int(choice_1) - 1 == 1: # 두 번째 줄일 때
    next_list_1.extend(matrix_7x3[0])
    next_list_1.extend(matrix_7x3[1])
    next_list_1.extend(matrix_7x3[2])
elif int(choice_1) - 1 == 2: # 세 번째 줄일 때
    next_list_1.extend(matrix_7x3[0])
    next_list_1.extend(matrix_7x3[2])
    next_list_1.extend(matrix_7x3[1])


# print(next_list_1)

list_a.clear()
list_b.clear()
list_c.clear()

for i in range(len(next_list_1)):
    if i % 3 == 0: # 첫줄에 배치할것들
        list_a.append(next_list_1[i])
    elif i % 3 == 1: # 둘째줄에 배치할것들
        list_b.append(next_list_1[i])
    elif i % 3 == 2: # 셋째줄에 배치할것들
        list_c.append(next_list_1[i])

matrix_7x3 = [list_a, list_b, list_c]

print()

list_123 = ['첫', '두', '세']
for i, row in zip(list_123, matrix_7x3):
    print(i+'번째줄' ,*row, sep='  ')

# ############################################################################

# 몇 번째 줄에 카드가 있는지 고르기 - 두번째
while True:
    choice_2 = input('두 번째 질문. 1 ~ 3 중 몇 번째 줄에 생각한 카드가 있나요?: ')

    if choice_2 in ['1', '2', '3']:
        break
    else:
        print('님 숫자 모름? 다시 입력하셈 ㅡㅡ')

next_list_2 = []

if int(choice_2) - 1 == 0: # 첫 번째 줄일 때
    next_list_2.extend(matrix_7x3[1])
    next_list_2.extend(matrix_7x3[0])
    next_list_2.extend(matrix_7x3[2])
elif int(choice_2) - 1 == 1: # 두 번째 줄일 때
    next_list_2.extend(matrix_7x3[0])
    next_list_2.extend(matrix_7x3[1])
    next_list_2.extend(matrix_7x3[2])
elif int(choice_2) - 1 == 2: # 세 번째 줄일 때
    next_list_2.extend(matrix_7x3[0])
    next_list_2.extend(matrix_7x3[2])
    next_list_2.extend(matrix_7x3[1])


# print(next_list_2)

list_a.clear()
list_b.clear()
list_c.clear()

for i in range(len(next_list_2)):
    if i % 3 == 0: # 첫줄에 배치할것들
        list_a.append(next_list_2[i])
    elif i % 3 == 1: # 둘째줄에 배치할것들
        list_b.append(next_list_2[i])
    elif i % 3 == 2: # 셋째줄에 배치할것들
        list_c.append(next_list_2[i])

matrix_7x3 = [list_a, list_b, list_c]

print()

list_123 = ['첫', '두', '세']
for i, row in zip(list_123, matrix_7x3):
    print(i+'번째줄' ,*row, sep='  ')

# ############################################################################

# 몇 번째 줄에 카드가 있는지 고르기 - 세번째
while True:
    choice_3 = input('마지막 질문. 1 ~ 3 중 몇 번째 줄에 생각한 카드가 있나요?: ')

    if choice_3 in ['1', '2', '3']:
        break
    else:
        print('님 숫자 모름? 다시 입력하셈 ㅡㅡ')

next_list_3 = []

if int(choice_3) - 1 == 0: # 첫 번째 줄일 때
    next_list_3.extend(matrix_7x3[1])
    next_list_3.extend(matrix_7x3[0])
    next_list_3.extend(matrix_7x3[2])
elif int(choice_3) - 1 == 1: # 두 번째 줄일 때
    next_list_3.extend(matrix_7x3[0])
    next_list_3.extend(matrix_7x3[1])
    next_list_3.extend(matrix_7x3[2])
elif int(choice_3) - 1 == 2: # 세 번째 줄일 때
    next_list_3.extend(matrix_7x3[0])
    next_list_3.extend(matrix_7x3[2])
    next_list_3.extend(matrix_7x3[1])


# print(next_list_3)

list_a.clear()
list_b.clear()
list_c.clear()

for i in range(len(next_list_3)):
    if i % 3 == 0: # 첫줄에 배치할것들
        list_a.append(next_list_3[i])
    elif i % 3 == 1: # 둘째줄에 배치할것들
        list_b.append(next_list_3[i])
    elif i % 3 == 2: # 셋째줄에 배치할것들
        list_c.append(next_list_3[i])

print()

print(f'당신이 생각했던 카드는 {matrix_7x3[1][3]} 입니다. 맞췄쥬? ㅋ')