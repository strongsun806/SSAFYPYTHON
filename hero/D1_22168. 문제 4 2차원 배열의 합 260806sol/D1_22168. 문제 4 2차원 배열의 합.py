list_nm = list(map(int, input().split()))
n = list_nm[0]
m = list_nm[1]
total = 0
for a in range(n):
    list_row_num = list(map(int, input().split()))
    for b in range(m):
        total += list_row_num[b]
print(total)