N = int(input())
txt = [input() for _ in range(N)]

ans = "NO"

# for row in txt :
#     if "Z" in row:
#         ans = "YES"
#         break   # for row

# print(ans)

def find_Z(txt, N):
    for i in range(N):
        for j in range(N):
            if txt[i][j]=="Z":
                return "YES"
    return "NO"

print(find_Z(txt,N))