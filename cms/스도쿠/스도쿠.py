import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
def row_test(data) :
    for i in range(9):
        if len(num_group- set(data[i]) ) > 0:
            return False
    return True

def column_group(data):
    new_list=[]
    for i in range(9):
        new_list.append([])
        for j in range(9):
            new_list[i].append(data[j][i])
    return new_list

def _3x3(data) :
    new_list=[]
    for i in range(0,9,3):
        for j in range(0,9,3):
            box =[]
            for k in range(i, i+3):
                for l in range(j,j+3):
                    box.append(data[k][l])
            new_list.append(box)
    return new_list

case_num = 0        
for test_case in range(1, T + 1):
    group =[]
    num_group = {1,2,3,4,5,6,7,8,9}
    for i in range(9):
        group.append(list(map(int,input().split())))
    if row_test(group) and row_test(column_group(group)) and row_test(_3x3(group))== True:
        print(f"#{test_case} 1")
    else :
        print(f"#{test_case} 0")
                    
                





        





