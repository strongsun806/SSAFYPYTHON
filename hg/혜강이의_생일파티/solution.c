#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int r, c;
} Point;

/* 정수 내의 1로 켜진 비트 수(녹은 초콜릿 개수) 카운트 */
static inline int get_bit_count(int n) {
    int cnt = 0;
    while (n > 0) {
        n &= (n - 1);
        cnt++;
    }
    return cnt;
}

int main(void) {
    int T;
    if (scanf("%d", &T) != 1) {
        return 0;
    }

    for (int tc = 1; tc <= T; ++tc) {
        int N, M;
        if (scanf("%d %d", &N, &M) != 2) {
            break;
        }

        Point zeros[25];
        Point ones[25];
        int K = 0; /* 깨끗한 표면(0) 개수 */
        int C = 0; /* 초콜릿 장식(1) 개수 */

        for (int r = 0; r < N; ++r) {
            for (int c = 0; c < N; ++c) {
                int val;
                scanf("%d", &val);
                if (val == 0) {
                    zeros[K].r = r;
                    zeros[K].c = c;
                    K++;
                } else {
                    ones[C].r = r;
                    ones[C].c = c;
                    C++;
                }
            }
        }

        /* 깨끗한 표면(0)이 7개 미만이면 조건을 만족할 수 없음 */
        if (K < 7) {
            printf("#%d -1\n", tc);
            continue;
        }

        int target_zeros = (1 << K) - 1;
        int l_zero[25] = {0};
        int l_one[25] = {0};
        int s_zero[25] = {0};
        int s_one[25] = {0};

        /* 전처리: 각 위치에 초를 꽂았을 때 도달하는 범위 비트마스킹 */
        for (int i = 0; i < K; ++i) {
            for (int j = 0; j < K; ++j) {
                int d = abs(zeros[i].r - zeros[j].r) + abs(zeros[i].c - zeros[j].c);
                if (d <= M) l_zero[i] |= (1 << j);
                if (d <= 1) s_zero[i] |= (1 << j);
            }
            for (int j = 0; j < C; ++j) {
                int d = abs(zeros[i].r - ones[j].r) + abs(zeros[i].c - ones[j].c);
                if (d <= M) l_one[i] |= (1 << j);
                if (d <= 1) s_one[i] |= (1 << j);
            }
        }

        int min_melt = 1000000;

        /* 긴 초 2개 선택 (조합) */
        for (int l1 = 0; l1 < K; ++l1) {
            for (int l2 = l1 + 1; l2 < K; ++l2) {
                int base_z = l_zero[l1] | l_zero[l2];
                int base_o = l_one[l1] | l_one[l2];

                /* 남은 후보 인덱스 구성 */
                int rem[25];
                int rem_sz = 0;
                for (int i = 0; i < K; ++i) {
                    if (i != l1 && i != l2) {
                        rem[rem_sz++] = i;
                    }
                }

                /* 짧은 초 5개 선택 (조합) */
                for (int i0 = 0; i0 < rem_sz; ++i0) {
                    for (int i1 = i0 + 1; i1 < rem_sz; ++i1) {
                        for (int i2 = i1 + 1; i2 < rem_sz; ++i2) {
                            for (int i3 = i2 + 1; i3 < rem_sz; ++i3) {
                                for (int i4 = i3 + 1; i4 < rem_sz; ++i4) {
                                    int cur_z = base_z | s_zero[rem[i0]] | s_zero[rem[i1]]
                                                       | s_zero[rem[i2]] | s_zero[rem[i3]] | s_zero[rem[i4]];

                                    /* 모든 빈 칸(0)이 덮였을 때만 초콜릿 개수 계산 */
                                    if (cur_z == target_zeros) {
                                        int cur_o = base_o | s_one[rem[i0]] | s_one[rem[i1]]
                                                           | s_one[rem[i2]] | s_one[rem[i3]] | s_one[rem[i4]];
                                        int cnt = get_bit_count(cur_o);
                                        if (cnt < min_melt) {
                                            min_melt = cnt;
                                            if (min_melt == 0) goto next_l; /* 0개면 조기 종료 */
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            next_l:;
            }
            if (min_melt == 0) break;
        }

        printf("#%d %d\n", tc, (min_melt == 1000000 ? -1 : min_melt));
    }

    return 0;
}