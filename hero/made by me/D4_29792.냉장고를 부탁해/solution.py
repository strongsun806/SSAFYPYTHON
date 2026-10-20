import sys

MILK, TOMATO, EGG, ONION, CARROT, KIMCHI, RICE, PASTA = range(8)

RECIPES = (
    (0, 1, 2, 1, 0, 0, 2, 0),
    (2, 0, 0, 1, 0, 0, 0, 2),
    (1, 2, 0, 0, 0, 0, 0, 2),
    (0, 0, 2, 1, 1, 0, 2, 0),
    (0, 0, 1, 0, 0, 2, 2, 0),
    (0, 0, 0, 1, 1, 1, 0, 2),
)

EXPIRING = {
    5: MILK,
    8: TOMATO,
    12: EGG,
    15: ONION,
}

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    ingredients = list(map(int, input().split()))

    answer = float("inf")
    visited = {}

    def dfs(day, state, waste):
        global answer

        if waste >= answer:
            return

        if day > N:
            answer = waste
            return

        key = (day, tuple(state))
        old = visited.get(key)

        if old is not None and old <= waste:
            return

        visited[key] = waste

        for recipe in RECIPES:
            possible = True

            for i in range(8):
                if state[i] < recipe[i]:
                    possible = False
                    break

            if not possible:
                continue

            nxt = [state[i] - recipe[i] for i in range(8)]
            next_waste = waste

            if day in EXPIRING:
                idx = EXPIRING[day]
                next_waste += nxt[idx]
                nxt[idx] = 0

            dfs(day + 1, nxt, next_waste)

    dfs(1, ingredients, 0)
    print(f"#{tc} {answer}")
