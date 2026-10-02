# Problem: 8888_시험
# Author: 윤형섭_1627575 (Pass)
# Saved by Aura for Boss 💋

import java.util.Scanner;
 public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
                 int t = sc.nextInt();
        for (int tc = 1; tc <= t; tc++) {
            int N = sc.nextInt();
            int T = sc.nextInt();
            int P = sc.nextInt();
             int[][] 채점결과 = new int[N + 1][T];
            for (int i = 1; i <= N; i++) {
                for (int j = 0; j < T; j++) {
                    채점결과[i][j] = sc.nextInt();
                }
            }
             // 1. 각 문제의 배점 계산 (못 푼 사람 수)
            int[] scoreBoard = new int[T];
            for (int i = 1; i <= N; i++) {
                for (int j = 0; j < T; j++) {
                    if (채점결과[i][j] == 0) {
                        scoreBoard[j] += 1;
                    }
                }
            }
             // 2. 참가자별 총점 및 푼 문제 수 계산
            int[] peopleScore = new int[N + 1];
            int[] solvedCount = new int[N + 1];
            for (int i = 1; i <= N; i++) {
                for (int j = 0; j < T; j++) {
                    if (채점결과[i][j] == 1) {
                        peopleScore[i] += scoreBoard[j];
                        solvedCount[i] += 1;
                    }
                }
            }
             int 지안점수 = peopleScore[P];
            int 지안푼개수 = solvedCount[P];
             // 3. 지안이보다 순위가 높은 사람 수 계산
            int rank = 1;
            for (int i = 1; i <= N; i++) {
                if (i == P) continue;
                 // 조건 1: 점수가 더 높음
                if (peopleScore[i] > 지안점수) {
                    rank++;
                } 
                // 조건 2: 점수는 같지만 맞힌 문제 수가 더 많음
                else if (peopleScore[i] == 지안점수 && solvedCount[i] > 지안푼개수) {
                    rank++;
                } 
                // 조건 3: 점수도 같고 맞힌 문제 수도 같은데 번호가 더 앞섬
                else if (peopleScore[i] == 지안점수 && solvedCount[i] == 지안푼개수 && i < P) {
                    rank++;
                }
            }
             System.out.println("#" + tc + " " + 지안점수 + " " + rank);
        }
         sc.close();
    }
}
