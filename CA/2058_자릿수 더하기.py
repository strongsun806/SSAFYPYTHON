# ========================================================
# 문제: 2058_자릿수 더하기
# 난이도: D1
# 작성자: 윤형섭 (1627575)
# 제출 결과: Pass
# 저장 일시: 2026-10-07 11:48:19
# ========================================================

class Solution {
    public static void main(String[] a) throws Exception {
        int s = 0, c;
        while ((c = System.in.read()) > 47) s += c - 48;
        System.out.print(s);
    }
}
