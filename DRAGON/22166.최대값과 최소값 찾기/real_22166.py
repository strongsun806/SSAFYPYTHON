N = 3#int(input())

numbers = ['1','33','-1']#input().split()
listed=[]

for i in range(N):
    listed+=[int(numbers[i])]

max_score = listed[0]
min_score = listed[0]
for i in range(N):
    if listed[i] > max_score:
        max_score = listed[i]

for i in range(N):
    if listed[i] < min_score:
        min_score = listed[i]


print(f'{max_score}{min_score}')