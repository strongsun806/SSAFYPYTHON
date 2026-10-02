import sys
sys.stdin = open("sample_input.txt","r")

T = int(input())
for tc in range(1, T+1):
    text = input()
    editted_text = text
    i = 0
    while len(editted_text) > i :
        if i+1 <len(editted_text) and editted_text[i] == editted_text[i+1] :
            editted_text = editted_text[0:i]+editted_text[i+2:]
            i=0
        else : 
            i+=1

    print(f"#{tc} {len(editted_text)}")
        