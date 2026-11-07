import sys
sys.stdin = open("sample_input.txt","r")

T=int(input())
for tc in range(1,T+1):
    N=int(input())
    tree=[0]*(N+1)
    number = 1
    def inorder(node):
        global