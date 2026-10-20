import java.io.*;
import java.util.*;

public class Solution {
    static final int MILK = 0;
    static final int TOMATO = 1;
    static final int EGG = 2;
    static final int ONION = 3;

    static final int[][] RECIPES = {
        {0, 1, 2, 1, 0, 0, 2, 0},
        {2, 0, 0, 1, 0, 0, 0, 2},
        {1, 2, 0, 0, 0, 0, 0, 2},
        {0, 0, 2, 1, 1, 0, 2, 0},
        {0, 0, 1, 0, 0, 2, 2, 0},
        {0, 0, 0, 1, 1, 1, 0, 2}
    };

    static int N;
    static int answer;
    static HashMap<String, Integer> visited;

    static int expiredIngredient(int day) {
        if (day == 5) return MILK;
        if (day == 8) return TOMATO;
        if (day == 12) return EGG;
        if (day == 15) return ONION;
        return -1;
    }

    static String makeKey(int day, int[] a) {
        StringBuilder sb = new StringBuilder();
        sb.append(day).append('/');
        for (int x : a) sb.append(x).append(',');
        return sb.toString();
    }

    static void dfs(int day, int[] a, int waste) {
        if (waste >= answer) return;

        if (day > N) {
            answer = waste;
            return;
        }

        String key = makeKey(day, a);
        Integer old = visited.get(key);

        if (old != null && old <= waste) return;
        visited.put(key, waste);

        for (int[] recipe : RECIPES) {
            boolean possible = true;

            for (int i = 0; i < 8; i++) {
                if (a[i] < recipe[i]) {
                    possible = false;
                    break;
                }
            }

            if (!possible) continue;

            int[] next = a.clone();

            for (int i = 0; i < 8; i++) {
                next[i] -= recipe[i];
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

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder out = new StringBuilder();

        int T = Integer.parseInt(br.readLine().trim());

        for (int tc = 1; tc <= T; tc++) {
            N = Integer.parseInt(br.readLine().trim());

            int[] ingredients = new int[8];
            StringTokenizer st = new StringTokenizer(br.readLine());

            for (int i = 0; i < 8; i++) {
                ingredients[i] = Integer.parseInt(st.nextToken());
            }

            answer = Integer.MAX_VALUE;
            visited = new HashMap<>();

            dfs(1, ingredients, 0);

            out.append('#').append(tc).append(' ')
               .append(answer).append('\n');
        }

        System.out.print(out);
    }
}
