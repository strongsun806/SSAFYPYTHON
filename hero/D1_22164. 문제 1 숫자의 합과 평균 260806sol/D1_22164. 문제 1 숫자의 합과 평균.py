T = int(input())
for test_case in range(1, T + 1):
    try:
        list_num_str = input().split()
        list_num = []
        for i in list_num_str:
            list_num.append(int(i))
        total_num = 0
        for i in list_num:
            total_num += i
        avg_num = int(total_num / T)
        print(f'{total_num} {avg_num}')
    except Exception:
        pass