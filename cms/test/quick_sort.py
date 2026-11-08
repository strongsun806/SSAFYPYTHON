# arr=[4,7,1,6,2,8,5,3,9]
# start=0
# end=8
# pivot=start
# a=start+1
# b=end
# print(f"a:{a}, b:{b}")
# while 1:
#     while a<=end and arr[a]<=arr[pivot]:    #배열범위안 이고 a의값이 pivot보다 작으면
#         print(f"a<=end, {arr[a]}<={arr[pivot]}")
#         a+=1
#         print(f"a:{a}")
#     while b>=start and arr[b]>arr[pivot]:   #배열범위 안 + b의 값이 pivot보다 크다면
#         print(f"b>start, {arr[b]}>{arr[pivot]}")
#         b-=1
#         print(f"b:{b}")
#     if a>b:
#         print("a>b")
#         break
#     print(f"{arr[a]},{arr[b]}")
#     arr[a],arr[b]=arr[b],arr[a]
#     print(f"change arr[a],arr[b] {arr[a]},{arr[b]}")

# print(f"change arr[b],arr[pivot] {arr[b]},{arr[pivot]}")
# arr[b],arr[pivot] = arr[pivot], arr[b]
# print(f"change arr[b],arr[pivot] {arr[b]},{arr[pivot]}")
# print(*arr)


# 기준점(피봇)보다 작은 값, 큰 값으로 나누기
# 나누다 보면 정렬이 된다...
arr = [6,8,1,3,4,5,9,2,7]

def quick_sort(target):
    l = len(target)
    if l<1:     # 요소가 1개 보다 작으면 그대로 반환
        return target
    #임의의 값 하나 잡고, 작은애들 큰애들 모으기
    left=[]     # 피벗보다 작은 값 들어갈 리스트
    right=[]    # 피벗보다 큰 값 들어갈 리스트
    # 큰 값 작은 값 나누기
    pivot =target[0]
    for i in range(1,l):
        if target[i]<pivot:  # 작으면 left에 붙이고
            left.append(target[i])
        else:   # 크거나 같으면 right에 붙이기
            right.append(target[i])
    #근데 left랑 right가 여전히 정렬이 안 된 상태!
    left=quick_sort(left)
    right=quick_sort(right)
    return left+[pivot]+ right

print(quick_sort(arr))