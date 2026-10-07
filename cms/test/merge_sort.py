# arr=[2,3,5,7,1,2,5,9]
# start=0
# end=7
# mid=(start+end)//2
#
# a=start
# b=mid+1
# result=[]
# print(f"a:{a}, b:{b}, result:{result}")
#
# while 1:
#     if a>mid and b>end:
#         break
#
#     if a>mid:
#         result.append(arr[b])
#         b+=1
#         print("a>mid")
#     elif b>end:
#         result.append(arr[a])
#         a+=1
#         print("b>end")
#     elif arr[a]<=arr[b]:
#         result.append(arr[a])
#         a+=1
#         print("arr[a]<=arr[b]")
#     else:
#         result.append((arr[b]))
#         b+=1
#         print("arr[a]>arr[b]")
#     print(f"a:{a}, b:{b}, result:{result}")
#
# print(*result)


arr=[2,7,5,3,1,6,9,2,1]

def merge(start,end):
    print(f"start:{start}, end:{end}")
    if start==end:
        return
    mid=(start+end)//2
    print(f"mid:{mid}")

    merge(start,mid)
    merge(mid+1,end)
    print(f"start:{start}, end:{end}")
    print(f"mid:{mid}")
    a = start
    print(f"a:{a}")
    b = mid + 1
    print(f"b:{b}")
    result = []

    while 1:
        if a > mid and b > end:
            break

        if a > mid:
            result.append(arr[b])
            b += 1
            print("a>mid")
        elif b > end:
            result.append(arr[a])
            a += 1
            print("b>end")
        elif arr[a] <= arr[b]:
            result.append(arr[a])
            a += 1
            print("arr[a]<=arr[b]")
        else:
            result.append((arr[b]))
            b += 1
            print("arr[a]>arr[b]")

    for i in range(len(result)):
        arr[start+i]=result[i]

merge(0,8)
print(*arr)