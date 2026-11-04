import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Solution {
    static int N, M, minMelt;
    static int[][] map;
    static ArrayList<int[]> zeros;
    static int[] longCandles = new int[2];
    static int[] shortCandles = new int[5];

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line;
        StringTokenizer st = null;

        while ((line = br.readLine()) != null) {
            line = line.trim();
            if (!line.isEmpty()) {
                st = new StringTokenizer(line);
                break;
            }
        }
        if (st == null || !st.hasMoreTokens()) return;

        int T = Integer.parseInt(st.nextToken());
        StringBuilder sb = new StringBuilder();

        for (int tc = 1; tc <= T; tc++) {
            while (st == null || !st.hasMoreTokens()) {
                line = br.readLine();
                if (line == null) break;
                line = line.trim();
                if (!line.isEmpty()) st = new StringTokenizer(line);
            }
            if (st == null || !st.hasMoreTokens()) break;

            N = Integer.parseInt(st.nextToken());
            M = Integer.parseInt(st.nextToken());

            map = new int[N][N];
            zeros = new ArrayList<>();

            for (int r = 0; r < N; r++) {
                for (int c = 0; c < N; c++) {
                    while (!st.hasMoreTokens()) {
                        st = new StringTokenizer(br.readLine());
                    }
                    map[r][c] = Integer.parseInt(st.nextToken());
                    if (map[r][c] == 0) {
                        zeros.add(new int[]{r, c});
                    }
                }
            }

            // 초를 꽂을 빈 칸(0)이 7개 미만이면 바로 불가능
            if (zeros.size() < 7) {
                sb.append("#").append(tc).append(" -1\n");
                continue;
            }

            minMelt = Integer.MAX_VALUE;

            // 1단계: 긴 초 2개 고르기 (조합 시작)
            pickLong(0, 0);

            sb.append("#").append(tc).append(" ")
              .append(minMelt == Integer.MAX_VALUE ? -1 : minMelt)
              .append("\n");
        }

        System.out.print(sb);
    }

    // 1. 긴 초 2개 선택 (조합)
    static void pickLong(int start, int cnt) {
        if (minMelt == 0) return; // 0개면 이미 최솟값이므로 탐색 중단

        if (cnt == 2) {
            // 긴 초를 고른 후, 남은 칸 중에서 짧은 초 5개 고르기
            pickShort(0, 0);
            return;
        }

        for (int i = start; i < zeros.size(); i++) {
            longCandles[cnt] = i;
            pickLong(i + 1, cnt + 1);
        }
    }

    // 2. 짧은 초 5개 선택 (조합)
    static void pickShort(int start, int cnt) {
        if (minMelt == 0) return;

        if (cnt == 5) {
            // 7개 초 선택 완료 -> 조건 검사
            checkCoverage();
            return;
        }

        for (int i = start; i < zeros.size(); i++) {
            // 이미 긴 초로 선택한 자리는 건너뛰기
            if (i == longCandles[0] || i == longCandles[1]) continue;

            shortCandles[cnt] = i;
            pickShort(i + 1, cnt + 1);
        }
    }

    // 3. 밝기 및 녹는 초콜릿 판정
    static void checkCoverage() {
        boolean[][] light = new boolean[N][N];

        // 긴 초 2개 비추기 (범위 M 이하)
        for (int idx : longCandles) {
            int[] pos = zeros.get(idx);
            spreadLight(pos[0], pos[1], M, light);
        }

        // 짧은 초 5개 비추기 (범위 1 이하)
        for (int idx : shortCandles) {
            int[] pos = zeros.get(idx);
            spreadLight(pos[0], pos[1], 1, light);
        }

        // 조건 검사: 케이크의 모든 깨끗한 표면(0)이 밝혀졌는가?
        for (int[] pos : zeros) {
            if (!light[pos[0]][pos[1]]) return; // 한 칸이라도 안 밝혀졌으면 무효
        }

        // 모든 0이 덮였다면, 빛이 닿아서 녹아내린 초콜릿(1) 개수 카운트
        int meltedCount = 0;
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                if (map[r][c] == 1 && light[r][c]) {
                    meltedCount++;
                }
            }
        }

        minMelt = Math.min(minMelt, meltedCount);
    }

    // 맨해튼 거리에 따라 light 배열에 불 밝히기
    static void spreadLight(int cr, int cc, int dist, boolean[][] light) {
        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                if (Math.abs(cr - r) + Math.abs(cc - c) <= dist) {
                    light[r][c] = true;
                }
            }
        }
    }
}