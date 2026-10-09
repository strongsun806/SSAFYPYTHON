T = int(input())

for j in range(T):
    a, n = map(str, input().split())
 
    stos = ''
    for i in range(int(a)):
        a = ''
        if n[i].isalpha() == False:
            if len(bin(int(n[i]))[2:]) < 4:
                stos += '0' *(4 - len(bin(int(n[i]))[2:])) 
            stos += bin(int(n[i]))[2:]
        else:
            stos += bin(int(ord(n[i])-65)+10)[2:]
         
    print(f'#{j+1} {stos}')