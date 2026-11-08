# ========================================================
# 문제: 1936_1대1 가위바위보
# 난이도: D1
# 작성자: 윤형섭 (1627575)
# 제출 결과: Pass
# 저장 일시: 2026-10-07 11:48:00
# ========================================================

import java.util.Scanner;
 class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
         int A = sc.nextInt();
        int B = sc.nextInt();
        if (A-B==-1 ||A-B== 2){
            System.out.println("B");}
        else{
            System.out.println("A");
        }
        sc.close();
    }
}
