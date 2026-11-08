import sys
sys.stdin = open("sample_input.txt")

# 쇠막대기 시작점을 만나면 생기는 쇠막대기 개수를 1증가
# 쇠막대기 종료점을 만나면 생기는 쇠막대기 개수를 1감소
#           **쇠막대기 종료점은 레이저가 없더라도 막대기 개수 1증가
# 레이저를 만나면 생기는 개수만큼 누적합 구하기



def solve(data):
    # 쇠막대기 시작점은 (
    # 쇠막대기 종료점은 )
    # 레이저는 ()
    total_cnt = 0
    cnt = 0     # 레이저에 의해 생기는 쇠막대기 개수
    for i in range(len(data)):
        if data[i] =='(' and data[i+1] != ')':   # 쇠막대기 시작
            cnt += 1    # 나중에 생길 쇠막대기 개수 증가
        elif data[i] ==')':     # 쇠막대기 끝 or 레이저
            if data[i-1] == '(':     # 레이저
                total_cnt += cnt
            else :
                cnt -= 1
                total_cnt += cnt
    return total_cnt

T=int(input())
for tc in range(1, T+1):
    data = input()
    result = solve(data)
    print(result)