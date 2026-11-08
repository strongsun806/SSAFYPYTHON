# ========================================================
# 문제: 2063_중간값 찾기
# 난이도: D1
# 작성자: 윤형섭 (1627575)
# 제출 결과: Pass
# 저장 일시: 2026-10-07 11:48:37
# ========================================================

import java.util.Scanner;
 class Solution
{
    public static void main(String args[]) throws Exception
    {
        Scanner sc = new Scanner(System.in);
         if (!sc.hasNextInt()) return;
        int n = sc.nextInt();
         int[] scores = new int[n];
        for (int i = 0; i < n; i++) {
            scores[i] = sc.nextInt();
        }
         for (int i = 1; i < n; i++) {
            int key = scores[i];
            int j = i - 1;
                         while (j >= 0 && scores[j] > key) {
                scores[j + 1] = scores[j];
                j--;
            }
            scores[j + 1] = key;
        }
         System.out.println(scores[n / 2]);
    }
}
