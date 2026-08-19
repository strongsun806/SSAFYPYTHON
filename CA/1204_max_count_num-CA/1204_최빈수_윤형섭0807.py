T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.



for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
   
    line_num=int(input())
    data = sorted(list(map(int, input().split())))
    # print(f"[{line_num}번째 숫자 리스트]: {data}")
    max_num_list=[]
    for score in range(1,101)[::-1]:#(1,2,3,....100)
        max_num_list.append(data.count(score))
    # print(max_num_list, len(max_num_list)) #[100점 10개, 99점 8개...]
    max_score = 100 - max_num_list.index(max(max_num_list))#최고점수
    print(f"#{test_case}",max_score)
 
