# bit = [0,0,0]
# for i in range(2):
#     bit[0] = i
#     for j in range(2):
#         bit[1] = j
#         for k in range(2):
#             bit[2] = k
#             print(bit)

def power(base, exp):
    if exp == 0:
        return 1

    if exp % 2 == 0:
        newbase = power(base, exp//2)
        return newbase * newbase
    else:
        newbase = power(base, (exp-1)//2)
        return (newbase * newbase) * base

print(power(2, 100))