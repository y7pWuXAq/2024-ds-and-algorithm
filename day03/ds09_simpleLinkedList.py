# date : 20240214
# file : ds09_simpleLinkedList.py
# desc : 단순 연결 리스트 전체 구현

# 노드 클래스 선언
class Node() :
    data = None # 실제 데이터 변수
    link = None # 다음 노드를 지정하는 변수

    def __init__(self) -> None:
        self.data = None # 클래스 자신이 self 이므로 클래스의 변수에 접근 하려면 반드시 self. 사용
        self.link = None

# start부터 시작해서 끝까지 노드 .data 출력
def printNodes(start) : 
    curr = start # start == head
    if curr == None : return
    while True :
        if curr.link == None : # 연결할 노드가 더이상 없으며
            print(curr.data) # 자기 데이터만 출력하고
            break # 반복문 탈출
        else : 
            print(curr.data, end=' > ') # 연결할 노드가 있으니까 연결 표시를 해주고
            curr = curr.link # 자기 뒤의 데이터를 curr로 바꿔줌

# 노드 삽입 함수
def insertNode(find, data) :
    global head, prev, curr # 전역 변수를 insertNodes에서 사용하겠다고 선언

    if head.data == find : # 맨 첫번째 노드
        node = Node()
        node.data = data
        node.link = head 
        head = node
        return # 함수 탈출
    
    curr = head
    while curr.link != None : # 중간에 노드 삽입
        prev = curr
        curr = curr.link
        if curr.data == find :
            node= Node()
            node.data = data 
            node.link = curr # 찾은 노드 앞에 새 노드 연결
            prev.link = node # 이전 노드 뒤에 새 노드 연결
            return # 함수 탈출

    node = Node() # 맨 마지막에 노드 삽입
    node.data = data
    curr.link = node
    return

# 노드 삭제 함수
def deleteNode(data) :
    global head, prev, curr

    if head.data == data : # 첫번째 노드 삭제면
        curr = head
        head = head.link
        del(curr)
        return
    
    curr = head
    while curr.link != None : # 첫번째 외 노드 삭제
        prev = curr
        curr = curr.link
    
        if curr.data == data :
            prev.link = curr.link
            del(curr)
            return

# 노드 검색 함수
def findNode(find) :
    global head, curr

    curr = head
    if curr.data == find :
        return curr # 현재 노드를 리턴해주고 함수 탈출
    while curr.link != None :
        curr = curr.link # 다음 노드로 넘어감
        if curr.data == find :
            return curr
    return Node() # 위의 함수를 만족 모하면 빈노드 리턴 함수 탈출

# 전역변수
head, prev, curr = None, None, None
originData = ['다현', '정연', '쯔위', '사나', '지효']

# 메인코드 영역
if __name__ == '__main__' :
    node = Node()
    node.data = originData[0] # 리스트에 다현을 할당.
    head = node

    for name in originData[1:] : # 1번 인덱스부터 리스트 끝까지 반복이라는 의미
        prev = node
        node = Node()
        node.data = name
        prev.link = node
    
    # 연결 리스트 구성 완료
    print('최초 구성된 연결 리스트')
    printNodes(head) # 구성된 연결 리스트가 맞는지 출력 확인

    print('맨 앞에 노드 삽입')
    insertNode('다현', '정국')
    printNodes(head)

    print('중간 노드 삽입')
    insertNode('사나', '미미')
    printNodes(head)

    print('마지막 노드 삽입')
    insertNode('재남', '미나')
    printNodes(head)

    # 노드 검색
    fNode = findNode('다현')
    printNodes(head)
    print(f'찾은 노드 : {fNode.data}')
