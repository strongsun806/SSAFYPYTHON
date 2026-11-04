# practice 1 (is_palin=True 사용)
# 전체 길이가 M인 문장으로 회문 검사하기
target = 'ABCBA'
M = len(target)
# 앞쪽 인덱스와 뒤쪽 인덱스 비교
# 절반만 비교
is_palin = True
for i in range(M//2):
    if target[i]!=target[M-1-i]:
        is_palin = False
        break

if is_palin:
    print('회문입니다!')
else :
    print('회문이 아닙니다')


# practice 2 (for-else 구문 사용)
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