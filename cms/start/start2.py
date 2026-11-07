a=13
trans=""
while a!=0:
    rest=a%3
    trans+=str(rest)
    a//=3
answer=trans[::-1]
print(answer)

result=int(answer,3)
print(result)


arr =[1,2,3]
for i in range(1<<3):
    result=[]
    for index in range(3):
        if i&(1<<index)!=0:
            result.append(arr[index])
    print(result)

from decimal import Decimal
a=Decimal('1.2')-Decimal("1.1")
print(a)

a=1.2-1.1
print(a)

a=1.25
print(f"{a:.1f}")

a=1.35
print(f"{a:.1f}")