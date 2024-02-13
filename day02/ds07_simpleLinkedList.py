# date : 20240213
# file : ds07_simpleLinkedList.py
# desc : 단순 연결 리스트 일반 구현

memory = [] # 컴퓨터 메모리를 유사 구성
# head, curr, prev 일반 변수
# head = node
head, curr, prev = None, None, None

class Node() :
    # datam link 두개의 멤버 변수 존재
    # 생성자 추가
    def __init__(self, name) -> None:
        self.data = name
        self.link = None

# 클래스 끝
def printNodes(start) : # 클래스의 멤버 함수가 아님.
    curr = start
    if curr == None : return # 함수를 빠져나감
    print(curr.data, end=' > ')
    while curr.link != None :
        curr = curr.link # 내 노드의 다음 노드가 curr가 됨
        print(curr.data, end=' > ') # end > 로 해서 줄바꿈 되지 않음
    print() # 줄바꿈 추가

dataArray = ['미나', '모모', '사나', '채연', '정연', '나연']

# 메인 시작
if __name__ == '__main__' :
    node = Node(dataArray[0]) # '미나' 데이터 담은 노드 생성
    head = node # 첫번째 값을 head가 가리킴
    memory.append(node) # 가짜 메모리에 집어 넣음

    for data in dataArray[1:] : # 두번째 노드부터 끝까지
        prev = node
        node = Node(data) # 모모
        prev.link = node
        memory.append(node)

    printNodes(head)