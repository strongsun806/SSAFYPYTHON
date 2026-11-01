"""
문제 구상
성격 유형 검사지
성격 유형은 16 (2x2x2x2) 가지로 MBTI 같음
검사지는 n개의 질문이 있고 각 질문에는 7가지의 선택지가 있음 (매우 비동의, 비동의, 약간 비동의, 모르겠음, 약간 동의, 동의, 매우 동의)
[각 선택지 별 점수]
3점 : 매우 동의, 매우 비동의
2점 : 동의, 비동의
1점 : 약간 동의, 약간 비동의
0점 : 모르겠음

로직 구상
1. 8개의 성격 유형의 점수 딕셔너리 만들기
2. for문을 활용해 survey와 choices를 하나씩 불러옴
3. 각 질문 별로 점수 더하기
4. 합산된 점수를 각 지표 별로 비교하여 성격 유형 지정하기
5. 유형을 비교해서 점수가 큰 유형을 answer에 추가
6. answer 반환
"""

def solution(survey, choices):
    answer = ''
    # 1. 8개의 성격 유형의 점수 딕셔너리 만들기
    score = {
        'R' : 0, 'T' : 0,
        'C' : 0, 'F' : 0,
        'J' : 0, 'M' : 0,
        'A' : 0, 'N' : 0,
    }
    # 2. for문을 활용해 survey와 choices를 하나씩 불러옴
    for i in range(len(survey)):
        # 2-1. 각 질문 별로 하나씩 지정
        type1 = survey[i][0]
        type2 = survey[i][1]
        # 2-2. 각 질문에 해당하는 점수를 지정
        choice = choices[i]

        # 3. 각 질문 별로 점수 더하기
        if choice < 4:
            score[type1] += 4 - choice
        elif choice > 4:
            score[type2] += choice - 4

    # 4. 합산된 점수를 각 지표 별로 비교하여 성격 유형 지정하기        
    pairs = ['RT', 'CF', 'JM', 'AN']
    for pair in pairs:
        type1 = pair[0]
        type2 = pair[1]
        # 5. 유형을 비교해서 점수가 큰 유형을 answer에 추가
        if score[type1] >= score[type2]:
            answer += type1
        else:
            answer += type2

    # 5. answer 반환
    return answer
