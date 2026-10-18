#include <stdio.h>
#include <stdint.h>
#include <limits.h>
#include <string.h>

#define MILK 0
#define TOMATO 1
#define EGG 2
#define ONION 3
#define HASH_SIZE 262147

int recipes[6][8] = {
    {0, 1, 2, 1, 0, 0, 2, 0},
    {2, 0, 0, 1, 0, 0, 0, 2},
    {1, 2, 0, 0, 0, 0, 0, 2},
    {0, 0, 2, 1, 1, 0, 2, 0},
    {0, 0, 1, 0, 0, 2, 2, 0},
    {0, 0, 0, 1, 1, 1, 0, 2}
};

int N;
int answer;

uint64_t hashKey[HASH_SIZE];
int hashWaste[HASH_SIZE];
unsigned char hashUsed[HASH_SIZE];

uint64_t makeState(int day, int a[8]) {
    uint64_t state = (uint64_t)day;

    for (int i = 0; i < 8; i++) {
        state <<= 6;
        state |= (uint64_t)a[i];
    }

    return state;
}

unsigned int getHash(uint64_t key) {
    key ^= key >> 33;
    key *= 0xff51afd7ed558ccdULL;
    key ^= key >> 33;
    return (unsigned int)(key % HASH_SIZE);
}

int checkVisited(uint64_t key, int waste) {
    unsigned int idx = getHash(key);

    while (hashUsed[idx]) {
        if (hashKey[idx] == key) {
            if (hashWaste[idx] <= waste) return 1;
            hashWaste[idx] = waste;
            return 0;
        }

        idx++;
        if (idx == HASH_SIZE) idx = 0;
    }

    hashUsed[idx] = 1;
    hashKey[idx] = key;
    hashWaste[idx] = waste;

    return 0;
}

int expiredIngredient(int day) {
    if (day == 5) return MILK;
    if (day == 8) return TOMATO;
    if (day == 12) return EGG;
    if (day == 15) return ONION;
    return -1;
}

void dfs(int day, int a[8], int waste) {
    if (waste >= answer) return;

    if (day > N) {
        if (waste < answer) answer = waste;
        return;
    }

    if (checkVisited(makeState(day, a), waste)) return;

    for (int food = 0; food < 6; food++) {
        int possible = 1;

        for (int i = 0; i < 8; i++) {
            if (a[i] < recipes[food][i]) {
                possible = 0;
                break;
            }
        }

        if (!possible) continue;

        int next[8];

        for (int i = 0; i < 8; i++) {
            next[i] = a[i] - recipes[food][i];
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

int main(void) {
    int T;
    scanf("%d", &T);

    for (int tc = 1; tc <= T; tc++) {
        scanf("%d", &N);

        int ingredients[8];

        for (int i = 0; i < 8; i++) {
            scanf("%d", &ingredients[i]);
        }

        answer = INT_MAX;
        memset(hashUsed, 0, sizeof(hashUsed));

        dfs(1, ingredients, 0);

        printf("#%d %d\n", tc, answer);
    }

    return 0;
}
