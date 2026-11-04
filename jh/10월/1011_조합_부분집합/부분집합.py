data = [1,2,3,4]
arr = []
def f(start):
    print(*arr)
    for i in range(start, len(data)):
        arr.append(data[i])
        f(i + 1)
        arr.pop()
f(0)
print('###############################')
def f(idx):
    if idx == len(data):
        print(*arr)
        return
    arr.append(data[idx])
    f(idx + 1)
    arr.pop()
    f(idx + 1)

f(0)