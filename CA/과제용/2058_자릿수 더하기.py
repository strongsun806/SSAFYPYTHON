# Problem: 2058_자릿수 더하기
# Author: 윤형섭_1627575 (Pass)
# Saved by Aura for Boss 💋

class Solution {
    public static void main(String[] a) throws Exception {
        int s = 0, c;
        while ((c = System.in.read()) > 47) s += c - 48;
        System.out.print(s);
    }
}
