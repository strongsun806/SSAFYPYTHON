# ========================================================
# 문제: 13112_5204. [파이썬 S/W 문제해결 구현] 4일차 - 병합 정렬
# 난이도: D3
# 작성자: 윤형섭 (1627575)
# 제출 결과: Pass
# 저장 일시: 2026-10-07 11:27:35
# ========================================================

def merge_sort(arr):
    global count
    if len(arr) <= 1:
        return arr
     mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
          if left[-1] > right[-1]:
        count += 1
     merged = []
    i = 0
    j = 0    
       while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
     merged.extend(left[i:])
    merged.extend(right[j:])
         return merged
 T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
         count = 0
    sorted_arr = merge_sort(arr)
          print(f"#{tc} {sorted_arr[N//2]} {count}")
