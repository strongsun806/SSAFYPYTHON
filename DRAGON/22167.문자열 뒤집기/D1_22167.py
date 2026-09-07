
test_data = [3, ["hello", "python", "algorithm"]]
N = test_data[0]
words = test_data[1] 

for i in range(N):
    a = words[i]
    reverse_word= "" #문자열 뒵집고 빈상자에 넣기
    
    for j in range(len(a) - 1, -1, -1): #문자열 맨 끝 -> 거꾸로 -> 반대방향으로(-1씩)
        reverse_word = reverse_word + a[j]


    print(reverse_word)