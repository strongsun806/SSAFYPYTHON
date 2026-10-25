import socket
import heapq

HOST = '127.0.0.1'
PORT = 8747

sock = socket.socket()

def init(nickname):
    try:
        print(f'[STATUS] Trying to connect to {HOST}:{PORT}')
        sock.connect((HOST, PORT))
        print('[STATUS] Connected')
        init_command = f'INIT {nickname}' 

        return submit(init_command)

    except Exception as e:
        print('[ERROR] Failed to connect. Please check if Battle SSAFY is waiting for connection.')
        print(e)
        return None

def submit(string_to_send):
    try:
        sock.send((string_to_send + ' ').encode('utf-8'))
        return receive()
        
    except Exception as e:
        print('[ERROR] Failed to connect. Please check if Battle SSAFY is waiting for connection.')

    return None

def receive():
    try:
        game_data = (sock.recv(1024)).decode()
        if int(game_data[0]) > 0:
            return game_data
        close()
    except Exception as e:
        print('[ERROR] Failed to connect. Please check if Battle SSAFY is waiting for connection.')

    return None

def close():
    try:
        if sock is not None: sock.close()
        print('[STATUS] Connection closed')
    
    except Exception as e:
        print('[ERROR] Network connection has been corrupted.')

# 전역 데이터 변수
map_data = [[]]
allies = {}
enemies = {}
codes = []

# 입력 데이터를 파싱하여 변수에 저장
def parse_data(game_data):
    game_data_rows = game_data.strip().split('\n')
    row_index = 0

    header = game_data_rows[row_index].split(' ')
    map_height = int(header[0])
    map_width = int(header[1])
    num_of_allies = int(header[2])
    num_of_enemies = int(header[3])
    num_of_codes = int(header[4])
    row_index += 1

    map_data.clear()
    map_data.extend([['' for _ in range(map_width)] for _ in range(map_height)])
    for i in range(map_height):
        col = game_data_rows[row_index + i].strip().split(' ')
        for j in range(map_width):
            map_data[i][j] = col[j]
    row_index += map_height

    allies.clear()
    for i in range(row_index, row_index + num_of_allies):
        ally = game_data_rows[i].strip().split(' ')
        ally_name = ally.pop(0)
        allies[ally_name] = ally
    row_index += num_of_allies

    enemies.clear()
    for i in range(row_index, row_index + num_of_enemies):
        enemy = game_data_rows[i].strip().split(' ')
        enemy_name = enemy.pop(0)
        enemies[enemy_name] = enemy
    row_index += num_of_enemies

    codes.clear()
    for i in range(row_index, row_index + num_of_codes):
        codes.append(game_data_rows[i].strip())

# 카이사르 암호 해독 (보급시설 F 에서 메가포탄 획득용)
def decode_cipher(cipher_text):
    # 배틀싸피 기본 시프트(+9) 우선 적용: R->A, S->B ...
    decoded_9 = ''.join(chr((ord(c) - ord('A') + 9) % 26 + ord('A')) for c in cipher_text)
    return decoded_9

def my_func(game_data):
    try:
        # 🔁 방향 벡터: [우, 상, 좌, 하] 순서로 이동 시 사용할 델타
        dr = [0, -1, 0, 1]
        dc = [1, 0, -1, 0]
        direction_map = ['R', 'U', 'L', 'D']

        # 입력된 게임 데이터를 파싱하여 map_data, codes, allies, enemies 초기화
        parse_data(game_data)

        R = len(map_data)
        C = len(map_data[0])
        start_pos = (-1, -1)
        target_pos = (-1, -1)

        # 내 탱크('M' 또는 'A')와 목표 포탑('X') 위치 탐색
        for i in range(R):
            for j in range(C):
                if map_data[i][j] in ('M', 'A', 'M1'):
                    start_pos = (i, j)
                elif map_data[i][j] == 'X':
                    target_pos = (i, j)

        # 내 탱크 포탄 정보 확인 (일반 포탄, 메가 포탄)
        my_info = allies.get('M') or allies.get('A') or allies.get('M1') or ['100', 'R', '1', '0']
        normal_missiles = int(my_info[2]) if len(my_info) > 2 else 1
        mega_missiles = int(my_info[3]) if len(my_info) > 3 else 0
        total_ammo = normal_missiles + mega_missiles

        def fire_cmd(d_idx):
            # 메가 포탄이 있으면 '방향 F M', 없으면 일반 포탄 '방향 F'
            if mega_missiles > 0:
                return f"{direction_map[d_idx]} F M"
            return f"{direction_map[d_idx]} F"

        # 다익스트라 탐색: (소요 턴수, 현재 행, 현재 열, 남은 포탄 수, 첫 번째 행동 커맨드)
        # - 빈 땅('G'): 이동 시 1턴 소요
        # - 나무('T') 또는 적 탱크('E1'~'E3'): 포탄 1발 소모하여 파괴(1턴) + 전진(1턴) = 2턴 소요
        # - 보급소('F') 인접 시: 암호 해독('G <해독문>')으로 1턴에 메가포탄 +1 보급 가능
        pq = [(0, start_pos[0], start_pos[1], total_ammo, None)]
        visited = {}

        while pq:
            turns, r, c, ammo, first_cmd = heapq.heappop(pq)

            if (r, c, ammo) in visited and visited[(r, c, ammo)] <= turns:
                continue
            visited[(r, c, ammo)] = turns

            # 1) 현재 위치에서 포탑('X') 사격 가능 여부 확인 (사거리 1~3칸)
            if ammo >= 1:
                for d in range(4):
                    for s in range(1, 4):
                        nr, nc = r + dr[d] * s, c + dc[d] * s
                        if not (0 <= nr < R and 0 <= nc < C):
                            break
                        cell = map_data[nr][nc]
                        # 바위('R'), 보급소('F'), 나무('T'), 적 탱크('E*')에 막히면 포탑 타격 불가
                        if cell in ('R', 'F', 'T') or cell.startswith('E'):
                            break
                        if (nr, nc) == target_pos:
                            shoot_action = fire_cmd(d)
                            return first_cmd if first_cmd is not None else shoot_action

            # 2) 보급소('F') 인접 시 암호가 주어졌다면 해독하여 포탄 보급 고려 (최대 5발까지)
            if ammo < 5:
                adj_facility = False
                for d in range(4):
                    nr, nc = r + dr[d], c + dc[d]
                    if 0 <= nr < R and 0 <= nc < C and map_data[nr][nc] == 'F':
                        adj_facility = True
                        break
                if adj_facility:
                    if r == start_pos[0] and c == start_pos[1] and codes:
                        dec = decode_cipher(codes[0])
                        cmd = f"G {dec}"
                    else:
                        cmd = first_cmd
                    if cmd is not None:
                        next_state = (r, c, ammo + 1)
                        if next_state not in visited or visited[next_state] > turns + 1:
                            heapq.heappush(pq, (turns + 1, r, c, ammo + 1, cmd))

            # 3) 4방향 이동 및 장애물(나무 'T') 파괴 탐색
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if not (0 <= nr < R and 0 <= nc < C):
                    continue
                cell = map_data[nr][nc]

                # 평지('G')로 이동 (1턴)
                if cell in ('G', 'G1', 'G2'):
                    cmd = first_cmd if first_cmd is not None else f"{direction_map[d]} A"
                    next_state = (nr, nc, ammo)
                    if next_state not in visited or visited[next_state] > turns + 1:
                        heapq.heappush(pq, (turns + 1, nr, nc, ammo, cmd))

                # 나무('T') 또는 체력 10 적('E*') 파괴 후 이동 (사격 1턴 + 이동 1턴 = 2턴, 포탄 1소모)
                elif (cell == 'T' or cell.startswith('E')) and ammo >= 1:
                    cmd = first_cmd if first_cmd is not None else fire_cmd(d)
                    next_state = (nr, nc, ammo - 1)
                    if next_state not in visited or visited[next_state] > turns + 2:
                        heapq.heappush(pq, (turns + 2, nr, nc, ammo - 1, cmd))

        return 'S'

    except Exception as e:
        return 'S'

NICKNAME = '기본코드'
game_data = init(NICKNAME)

# while 반복문: 배틀싸피 메인 프로그램과 클라이언트(이 코드)가 데이터를 계속해서 주고받는 부분
while game_data is not None:

    # 수신 데이터 출력
    print(f'{game_data}\n')

    # 커맨드 지정
    output = my_func(game_data)

    # 커맨드 전송
    game_data = submit(output)

# 반복문을 빠져나왔을 때 배틀싸피 메인 프로그램과의 연결을 완전히 해제하기 위해 close 함수 호출
close()