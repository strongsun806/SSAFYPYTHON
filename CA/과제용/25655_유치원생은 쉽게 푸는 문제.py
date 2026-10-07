# Problem: 25655_유치원생은 쉽게 푸는 문제
# Author: 윤형섭_1627575 (Pass)
# Saved by Aura for Boss 💋

t = int(input())
for tc in range(1,t+1):
    N=int(input())
    result=[]
    if N==1:
        result.append("0")
    elif N==0:
        result.append('1')
    else:
        number_of_eight=N//2
        one_or_zero=N%2
        if one_or_zero==0:
            for i in range(number_of_eight):
                result.append('8')
        else:
            result.append('4')
            for i in range(number_of_eight):
                result.append('8')
    print("".join(result))
