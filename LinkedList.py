import random
import os
# 데이터 스트럭쳐 공부
# Linked List - singly/doubly
# Tree - BST / AVL / Red Black
# Trie
# Heaps
# Stack / Queue

# 내가 이해하는대로 링크드 리스트 써보자:
# 일단 모든 데이터 구조는, 클래스로 형성이 된다 - 관리하기 편하기 때문에
class LinkedList():
  # 이니셜라이져: 이 클래스의 중요한 기틀은 이렇다
    class Node():
        # 링크드 리스트에서는, 자기가 가지고 있는 벨류와,포인터가 있음. 포인터의 개념을 이해하여야 한다.
        # 포인터 - 변수가 가르키고 있는 짝대기
        def __init__(self, value) -> None:
            self.value = value
            self.next = None
        # 여기까지 뭘했냐: 난 지금 노드형성을 위한 클래스를 만들었음. 이 클래스는 벨류와 다음 노드를 가르키는 포인터를 가지고 있음.

    # 링크드 리스트의 이니셜라이저는, 시작점을 항상 가지고 있다. 뭐든 간에.
    def __init__(self, sorted) -> None:
        self.head = None
        self.tail = None
        self.front = None # Front half
        self.back = None # Back half
        self.sorted = sorted
    
    # 뭐.. 기본 기틀은 다 됬음. 여기서 이제 기본 기능들을 구현해보자
    # 1. 노드 입력 (중간에 삽입 구현)
    # 1.1 sorted insert 구현
    # 2. 노드 출력
    # 3. 노드 삭제 (중간에 삭제 구현)
    # 4. 노드 찾기
    # 6. 노드 업뎃
    
    # 나중에 mergesort linked list 구현해보기ㅣㅣㅣㅣㅣㅣㅣㅣ

    # 1. 노드 입력
    def insert(self, value):

        if self.sorted:
            self.sortedInsert(value)
            return
        else:
            # 일단, 어디서 뭘 넣을껀지 어디서부터 시작함? 잘 모르니까 일단 시작점을 가져오자.
            node = self.head
            # 일단 노드를 만들자
            new_node = LinkedList.Node(value)
            # 근데 니가 지금 가지고있는 링크드 리스트가, 비어있는지 아닌지 잘 모르잖아? 확인하자
            # 비어있다면:
            if not node:
                self.head = new_node
                return
            # 안 비어있으면, 거 안에 있는 노드들은 class Node 들의 attribute 들을 다 가지고 있으니깐, 넥스트 포인터 접근 가능함: 
            else:
                while node:
                    before_node = node
                    node = node.next
                node = before_node
                # 갈때까지 갔으면, 넥스트 포인터에 뉴노드 추가
                # 근데... 여기서 더 생각을 해보면, 이미 이전 노드의 밸류랑 지금 내가 입력할 노드의 숫자가 같을수 있으니까
                # 만약 같은 경우를 생각해주자. 같으면 인서트 안하고 안같으면 인서트 하고.
                mode = 'overwrite' # 'no overwrite'
                if mode == 'no overwrite':
                    # 아래의 경우는 같아도 무조건 입력하는거고
                    node.next = new_node
                    return node
                else:
                    # 아래의 경우는 같으면 입력을 안하거나, 오버라이트 하는거고.
                    if node.value == new_node.value:
                        return node
                    else:
                        node.next = new_node
                        return node

    def sortedInsert(self, value):
        node = self.head
        newNode = LinkedList.Node(value)

        if not node: # 노드 한개도 없을때 (비어있는 링크드 리스트일때)
            self.head = newNode
            return
        
        elif node.value >= newNode.value: # 노드 한개만 있을때, 이미 있는 노드가 새 노드보다 숫자가 큰 경우엔,
            # newNode ----> self.head ----> None (next ptr)
            newNode.next = node # 새로운 노드의 넥스트 포인터는 루트와 같음
            self.head = newNode
        
        else:
            while node.next is not None and node.next.value <= newNode.value:
                node = node.next # traversing
            newNode.next = node.next
            node.next = newNode

            return node

    def insertNthPosition(self, value, nth = None):
        node = self.head
        newNode = LinkedList.Node(value)

        # 만약 nth 숫자가 이 리스트의 전체 길이보다 길면, 디폴트로 맨 마지막에 넣을꺼임.
        
        if not node:
            self.head = newNode
            return

        else:
            if nth == 0:
                newNode.next = node
                self.head = newNode
                return node
            else:
                while nth > 0 and node.next is not None:
                    before_node = node
                    nth -= 1 # n 번째 자리는 차례대로 적어지면서 자연스럽게 트래버싱을 한다
                    node = node.next
                # 근데 이제 nth 의 숫자가 0 이 되면, 그 자리의 넥스트 포인터에 뉴 노드를 집어넣는다는 뜻이다.
                newNode.next = before_node.next
                before_node.next = newNode
                return before_node

    def deleteNode(self, value):
        
        node = self.head
        
        while node:
            if node.value != value:
                before_node = node
            else: # 그전 노드와 그 다음의 노드를 연결.
                before_node.next = node.next
            node = node.next

        return node

    def deleteNthNode(self, nth):
        
        node = self.head
        
        # 노드가 비어있을대
        if not node:
            print("Node is empty")
            return
        else:
            if nth == 0:
                self.head = node.next
                return node
            else:
                while nth > 0 and node.next is not None:
                    nth -= 1
                    before_node = node
                    node = node.next

                before_node.next = node.next
                return node

    def findNode(self, value):
        # Finding a node that contains the value given the input value of the function.
        node = self.head
        # Traversing
        pos = 0
        while node.next is not None:
            pos += 1
            if node.next.value == value:
                print(f"the given value is in {pos} th position of this linked list")
            node = node.next
        return

    def findNthNode(self, nth):
        node = self.head

        while nth > 0 and node.next is not None:
            nth -= 1
            node = node.next
        
        if nth != 0:
            print('index exceeding the total length')
        else:
            print(node.value)

    def updateNode(self, value, replaceTo):
        # first find the value:
        node = self.head
        ans = 0
        while node.next is not None: # traverse
            node = node.next
            if node.value == value:
                node.value = replaceTo
                ans += 1
        if ans == 0:
            print('value does not exist')
        return node

    def updateNthNode(self, nth, replaceTo):
        node = self.head

        while node.next is not None and nth > 0:
            nth -= 1
            node = node.next

        if nth == 0:
            node.value = replaceTo
        else:
            print('index exceeding the total length of this linked list')

        return node


    def splitList(self):
        slow = self.head
        fast = self.head.next

        if slow is None or fast is None:
            return slow, None

        while fast:
            
            if fast.next: # if the fast traverser has next not null,
                slow = slow.next # traverse once
                fast = fast.next # traverse twice
            fast = fast.next # traverse once
        returnVal = self.head, slow.next
        slow.next = None
        self.front = returnVal[0]
        self.back = returnVal[1]


    def sortTheSplittedMerge(self):
        # handle base case:
        if not self.front:
            self.front = self.back
            return
        elif not self.back:
            self.back = self.front
            return

        # compare if the front value is less than the back --> don't swap else: swap
        print(self.front.value)
        print(self.back.value)
        if self.front.value <= self.back.value:
            self.front = self.front.next
            self.front.next = self.sortTheSplittedMerge()
        else:
            self.back = self.back.next
            self.back.next = self.sortTheSplittedMerge()

        
    def nodeSort_merge(self):
        # implement merge sort
        if self.head is None or self.head.next is None: # handle when the linked list is empty or only 1 node.
            # print('should nto be run')
            return

        # split the linked list 
        self.splitList()
        self.nodeSort_merge()
        self.sortTheSplittedMerge()

    # 링크드 리스트 출력
    def print(self):
        # 그냥 한바뀌씩 다 돌면서 출력하셈
        # 모양대로 출력해볼까
        nodes = []
        node = self.head
        if not node:
            print("Node is empty")
            return
        while node:
            nodes.append(node.value)
            node = node.next
        nodes = map(str,nodes)
        print(" -> ".join(nodes))

def cls():
    os.system("clear")

def print_splitted(front, back):

    fronts, backs = [], []
    while front:
        fronts.append(front.value)
        front = front.next
    
    while back:
        backs.append(back.value)
        back = back.next

    fronts = map(str,fronts)
    backs = map(str,backs)
    
    fronts = " -> ".join(fronts)
    backs = " -> ".join(backs)
    print(f"fronts {fronts}")
    print(f"backs {backs}")
        

#용수형한테: 이거 왜하는거에여?
if __name__ == "__main__":
    cls()
    ll = LinkedList(sorted = True)
    i = 0
    for _ in range(0,21):
        ll.insert(random.randint(0,200))
        i += 1
    ll.print()