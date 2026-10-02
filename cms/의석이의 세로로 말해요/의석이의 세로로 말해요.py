import sys
sys.stdin = open("sample_input.txt","r")

T= int(input())
for tc in range(1,T+1):
    longest = 0
    words=[]
    for _ in range(5):
        word = input()
        words.append(word)
        if len(word)>longest:
            longest=len(word)

    result =[]
    for i in range(longest):
        for j in range(5):
            try :
                result.append(words[j][i])
            except IndexError : 
                continue


    print(f"#{tc} {''.join(result)}")