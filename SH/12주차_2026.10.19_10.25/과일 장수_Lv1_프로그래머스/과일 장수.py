"""
문제 구상
사과를 팔기 위해 사과 상자를 포장하고 있음
사과는 1점부터 k점까지의 점수가 메겨짐
사과 상자의 가격은 가장 낮은 점수 x 개수로 정해짐
과일 장수가 가장 많은 사과를 판다면 얻을 수 있는 최대 이익은 얼마인가

로직 구상
score의 개수가 m보다 크다면 사과 상자를 하나 포장할 수 있음
가장 높은 점수부터 차례대로 m개만큼 빼옴
그 중 가장 낮은 점수 x m을 answer += 함
이걸 반복
"""

def solution(k, m, score):
    answer = 0
    
    score = sorted(score, reverse=True)
    
    for i in range(m-1, len(score), m):
        answer += score[i] * m
        
    return answer