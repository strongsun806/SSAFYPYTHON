# 연결 리스트 형태롤 Stack 만들기
class Node:
    # value와 다음 노드를 가리키는 주소값을 저장할 수 있어야함
    def __init__(self,data):
        self.value = data
        self.next = None

class MyStack:
    # 노드와 노드를 연결해서 stack 구현하기
    # 속성과 행동(메서드)
    # 마지막 정점을 알고 있어야 함
    def __init__(self):
        self.head = None

    def push(self,data): #데이터를 스택에 넣기
        # 노드 만들고,
        new_node =Node(data)
        # 스택이 비었나?
        if self.is_empty():
            self.head=new_node
        else :  #이미 다른 노드가 stack에 있으니까, 마지막에 연결
                # 현재 마지막 노드의 next에 새로 만든 노드 연결해주기
                # 새로 만든 노드의 주소값을 현재 마지막 노드의 next에 넣어주기
                # 마지막 노드 어떻게 찾지?
                # 시작 노드 부터 볼건데, next가 None인애가 마지막 노드
                # 마지막 노드 찾았으니까 방금 만든 노드 연결 해주기
                last = self.get_last
                last.next = new_node
        pass

    def get_last(self):
        last  = self.head
        while last.next is not None:
            last = last.next
        return last
    
    def pop(self):  #마지막 노드의 value 반환하고, 노드 stack에서 삭제
        # 내 다음 요소가 마지막 노드라면 걔가 빠져야 하니까
        # 마지막 요소의 직전요소의 next를 None으로 만들어야 합니다
        # 마지막 요소의 직전요소 찾기
        # 내 다음 요소의 next가 None인 노드 찾기
        last = self.get_last_node()
        if self.is_empty():
            print('스택이 비었습니다')
        else :
            # 현재 요소의 next 보기
            if self.head.next is None:  #스택 요소가 하나 일때,
                last = self.head
                self.head = None
            else:
                current = self.head # 마지막 직전 요소 찾기
                while current.next.next is None:
                    current - current.next
                # 직전 요소 찾았으니 지워주기 
                last = current.next
                current.next = None
        return last.value

    def is_empty(self):
        # 시작 노드가 없네? 스택 비어있는거 아니면 스택 비어있지 않음!
        if self.head is None:
            return True
        return False
    pass