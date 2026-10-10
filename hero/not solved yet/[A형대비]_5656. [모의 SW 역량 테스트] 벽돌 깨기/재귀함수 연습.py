# def dfs(depth):
#     print("들어감:", depth)

#     if depth == 3:
#         print("종료")
#         return

#     dfs(depth + 1)

#     print("돌아옴:", depth)


# dfs(1)

numbers = [1, 2, 3]
path = []
visited = [False, False, False]


def dfs(depth):
    # 숫자 3개를 모두 선택했다면 결과 출력
    if depth == 3:
        print(path)
        return

    for i in range(3):
        # 이미 사용한 숫자는 건너뜀
        if visited[i]:
            continue

        # ① 숫자 선택 — 들어가면서 실행
        visited[i] = True
        path.append(numbers[i])

        # ② 다음 숫자를 선택하러 들어감
        dfs(depth + 1)

        # ③ 선택 취소 — 돌아오면서 실행
        path.pop()
        visited[i] = False

dfs(0)