import sys
sys.stdin = open("sample_input.txt", "r")

# 테스트 갯수 = T
T = int(input())
for test_case in range(1, T+1):
    # 최대 이동 거리 = K, 종점 거리 = N, 충전기가 설치된 정류소 갯수 = M 
    K,N,M= map(int,input().split())
    # 출발지로 부터의 거리를 인덱스로 가지는 station 리스트 생성
    station = [0]*N
    # 충전소가 있는 정류소의 인덱스를 요소로 하는 char_st 리스트
    char_st = list(map(int, input().split()))

    # 충전소가 있는 정류장의 거리를 인덱스로 하여 station 리스트의 값을 1로 변경
    for i in char_st:
        station[i] = 1

    # 현재 버스가 있는 곳 = now를 0으로 초기화
    now = 0
    # 충전한 횟수 = char_count를 0으로 초기화
    char_count = 0

    # 버스의 현재 위치에서 종점까지 갈 수 있는 상태가 될 때까지 반복
    while now+K < N :
        # 현재 위치에서 K거리 안에 충전가능 정류소가 없을 경우를 판단하기 위한 can_pass를 False로 초기화
        can_pass = False
        # 충전된 버스가 갈 수 있는 최대 거리부터 가까워지면서 반복
        for char in range(now+K,now,-1):
            # 충전소가 있으면
            if station[char] == 1 :
                # 버스 위치를 그곳으로 재할당
                now = char
                # 충전횟수 + 1
                char_count += 1
                # 충전이 가능했기 때문에 can_pass를 True로 변경
                can_pass = True
                # 충전된 버스가 갈 수 있는 가장 먼 정류장을 찾았으므로 그보다 가까운 정류장을 찾을 필요가 없다 -> break으로 for 반복문 종료
                break

        # 충전가능 정류소가 없었을 경우(can_pass == False), 결과 값(char_count)을 0으로 재할당하고, While 반복문 종료
        if can_pass == False:
            char_count = 0
            break
        
        

    print(f"#{test_case} {char_count}")

        