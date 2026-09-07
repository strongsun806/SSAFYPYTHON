
n, m = map(int, input().split())
a = list(map(int, input().split()))

for _ in range(m):
    i, j = map(int, input().split())
    print(sum(a[i-1:j]))
 
