# ========================================================
# 문제: 25655_유치원생은 쉽게 푸는 문제
# 난이도: D3
# 작성자: 윤형섭 (1627575)
# 제출 결과: Pass
# 저장 일시: 2026-10-07 11:37:19
# ========================================================

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
