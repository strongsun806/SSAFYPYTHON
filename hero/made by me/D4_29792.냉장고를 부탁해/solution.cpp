#include <iostream>
#include <array>
#include <map>
#include <climits>
using namespace std;

const int MILK = 0;
const int TOMATO = 1;
const int EGG = 2;
const int ONION = 3;

const int RECIPES[6][8] = {
    {0, 1, 2, 1, 0, 0, 2, 0},
    {2, 0, 0, 1, 0, 0, 0, 2},
    {1, 2, 0, 0, 0, 0, 0, 2},
    {0, 0, 2, 1, 1, 0, 2, 0},
    {0, 0, 1, 0, 0, 2, 2, 0},
    {0, 0, 0, 1, 1, 1, 0, 2}
};

int N;
int answer;
map<array<int, 9>, int> visited;

int expiredIngredient(int day) {
    if (day == 5) return MILK;
    if (day == 8) return TOMATO;
    if (day == 12) return EGG;
    if (day == 15) return ONION;
    return -1;
}

void dfs(int day, array<int, 8> a, int waste) {
    if (waste >= answer) return;

    if (day > N) {
        answer = waste;
        return;
    }

    array<int, 9> key;
    key[0] = day;
    for (int i = 0; i < 8; i++) key[i + 1] = a[i];

    auto it = visited.find(key);
    if (it != visited.end() && it->second <= waste) return;
    visited[key] = waste;

    for (int food = 0; food < 6; food++) {
        bool possible = true;

        for (int i = 0; i < 8; i++) {
            if (a[i] < RECIPES[food][i]) {
                possible = false;
                break;
            }
        }

        if (!possible) continue;

        array<int, 8> next = a;

        for (int i = 0; i < 8; i++) {
            next[i] -= RECIPES[food][i];
        }

        int nextWaste = waste;
        int idx = expiredIngredient(day);

        if (idx != -1) {
            nextWaste += next[idx];
            next[idx] = 0;
        }

        dfs(day + 1, next, nextWaste);
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    for (int tc = 1; tc <= T; tc++) {
        cin >> N;

        array<int, 8> ingredients;
        for (int i = 0; i < 8; i++) cin >> ingredients[i];

        answer = INT_MAX;
        visited.clear();

        dfs(1, ingredients, 0);

        cout << "#" << tc << " " << answer << '\n';
    }

    return 0;
}
