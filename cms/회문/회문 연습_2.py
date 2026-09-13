# import sys
# sys.stdin = open("sample_input.txt","r")

# T = int(input())

# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     str_list = [list(input()) for _ in range(N)]
#     ans = ""
#     for i in range(N):
#         for j in range(N-M+1):     
#             word = str_list[i][j:j+M]
#             if word == word[::-1]:
#                 ans = "".join(word)
#                 break

#         for j in range(N):
#             for r in range(N-M+1):
#                 word_ex =[]

#                 for i in range(r, r+M):    
#                     word_ex.append(str_list[i][j])

#                 if word_ex == word_ex[::-1]:
#                     ans = "".join(word_ex)
#                     break
#             if ans :
#                 break

#     print(f"#{tc} {ans}")



# 강사님 풀이

# 전체 길이가 M인 문장으로 회문 검사하기
target = 'ABCBA'
M = len(target)
# 앞쪽 인덱스와 뒤쪽 인덱스 비교
# 절반만 비교
for i in range(M//2):
    if target[i]!=target[M-1-i]:
        is_palin = False
        print('회문이 아닙니다')
        break
    
else :  # for문이 도는 동안 break가 한 번도 실행이 안되면 수행되는 코드
    print('회문입니다.')