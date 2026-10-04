# Problem: 1221_[S/W 문제해결 기본] 5일차 - GNS
# Author: 윤형섭_1627575 (Pass)
# Saved by Aura for Boss 💋

T = int(input())
word_ls = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
 for tc in range(1, T + 1):
    what = input().split()
    listed_char = input().split()
     result = [0] * 10
      for item in listed_char:
        for j in range(len(word_ls)):
            if item == word_ls[j]:
                result[j] += 1
      sorted_ls = []
    for j in range(len(word_ls)):
        sorted_ls.extend([word_ls[j]] * result[j])
     print(what[0])
    print(*(sorted_ls))
