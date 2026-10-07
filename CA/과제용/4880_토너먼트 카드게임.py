# Problem: 12673_4880. [파이썬 S/W 문제해결 기본] 5일차 - 토너먼트 카드게임
# Author: 윤형섭_1627575 (Pass)
# Saved by Aura for Boss 💋

#s,e에 포함된 학생들 중 승자 번호를 반환하는 함수
def solve(s,e):
    # s와 e 범위에 있는 학생들의 승자 정하기
    if s == e:  #그룹 내에 학생이 1명
        return s
      m = (s+e)//2
    winner1 = solve(s,m)
    winner2 = solve(m+1,e)
    p1 = data[winner1] #각 그룹의 승자가 낸 카드
    p2 = data[winner2]
    # p1이 가위
    # winner1이 유리하니까... winner2가 확실히 이겼을 때만 바꿔주기
    winnner = winner1
    if p1 == 1 and p2 == 2:
        winnner = winner2
    elif p1 == 2 and p2 == 3:
        winnner = winner2
    elif p1 == 3 and p2 == 1:
        winnner = winner2
      return winnner
  T = int(input())
for tc in range(1,T+1):
    N = int(input())
    # 학생 번호와 인덱스 일치 시키기 위해서 0번 추가(안해줘도 될 걸요..?)
    data = [0] + list(map(int,input().split()))
    result = solve(1,N)
    print(f'#{tc} {result}')
