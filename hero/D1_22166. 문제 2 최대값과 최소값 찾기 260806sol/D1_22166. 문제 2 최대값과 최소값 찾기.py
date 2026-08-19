T = int(input())
list_num_str = input().split()  
list_num = []
for i in range(T):
    list_num.append(int(list_num_str[i]))
print(f'{max(list_num)} {min(list_num)}')