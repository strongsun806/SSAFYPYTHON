make_prime=[]

for i in range(1,1000001):
    is_valid=1
    for j in range(2,1001):
        if i<j**2:
            break
        if i>=j**2:
            if i%j==0:
                is_valid=0
                break
    if is_valid==1:
        make_prime.append(i)
make_prime.pop(0)


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    n,m= map(int,input().split())
    print(n,m)
    for i in 
