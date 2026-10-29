"""
문제 구상
게시판 불량 이용자 신고하고
처리 결과를 메일로 발송하는 시스템 개발
[조건]
1. 한 번에 한 명의 유저만 신고
2. 서로 다른 유저를 신고 가능 / 횟수 제한 없음
3. 한 유저를 여러 번 신고할 경우, 횟수는 1회로 처리
4. k번 이상 신고된 유저는 정지 / 해당 유저를 신고한 유저에게 정지 사실 메일로 발송됨


문제 로직
1. id_list를 바탕으로 메일 수를 저장할 answer 리스트 생성
2. report를 딕셔너리 형태로 변형
 - key : 신고당한 유저
 - value : 해당 유저를 신고한 사람들 (중복 제거)
3. 딕셔너리를 순회하면서 신고자 수가 k 이상인지 확인
4. k 이상이라면 해당 유저를 신고한 사람들을 순회
5. 신고한 사람의 id_list 인덱스를 찾아 answer에 1씩 더함
6. answer 반환
"""

def solution(id_list, report, k):
    # 1. id_list를 바탕으로 메일 수를 저장할 answer 리스트 생성
    answer = [0] * len(id_list)
    # 2. report를 딕셔너리 형태로 변형
    report_dict = {}
    # 2-1. report를 하나씩 꺼내와 user, target 변수로 지정
    for i in report:
        user, target = i.split()
        # 2-2. 딕셔너리 안에 타겟이 없다면 user 집합 만들기
        if target not in report_dict:
            report_dict[target] = {user}
        # 2-3. 있다면 이미 있는 집합에 user 추가
        else:
            report_dict[target].add(user)
    # 3. 딕셔너리를 순회하면서 신고자 수가 k이상인지 확인
    for target in report_dict:
        if len(report_dict[target]) >= k:
            # 4. 신고한 사람들을 하나씩 불러옴
            for user in report_dict[target]:
                # 5. 신고한 사람의 id_list 인덱스를 찾아 answer에 1씩 더함
                idx = id_list.index(user)
                answer[idx] += 1
    # 6. answer 반환
    return answer
