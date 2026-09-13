s1 = input()
s2 = input()

ans = "YES"

for ch in s1:
    if ch not in s2:
        ans = "NO"
        break   # for ch
print(ans)
