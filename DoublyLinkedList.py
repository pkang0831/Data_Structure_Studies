import os
    # 헤드부터 하는거:
    # 1. 노드 입력 (중간에 삽입 구현)
    # 1.1 sorted insert 구현
    # 2. 노드 출력
    # 3. 노드 삭제 (중간에 삭제 구현)
    # 4. 노드 찾기
    # 6. 노드 업뎃

    # 테일부터 하는거:
    # 1. 노드 입력 (중간에 삽입 구현)
    # 1.1 sorted insert 구현
    # 2. 노드 출력
    # 3. 노드 삭제 (중간에 삭제 구현)
    # 4. 노드 찾기
    # 6. 노드 업뎃

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, print = None) -> None:
        self.head = None
        self.tail = None
        self.head_ggangtong = Node(0)
        self.tail_ggangtong = Node(0)

    def print(self) -> None:
        
        # if self.print == 'front':
        node = self.head
        while node is not None:
            print(node.val, end = '')
            print(' -> ', end = '')
            node = node.next
        # elif self.print == 'back':
        #     node = self.tail
        #     while node.prev is not None:
        #         print(node.val, end = '')
        #         print(' -> ', end = '')
        #         node = node.prev

    def insert(self, val) -> None:

        # two cases: 
        # 1. if linked list is completely empty
        # 2. if node is present.

        node = self.head
        newNode = Node(val)

        # Case 1
        if not node:
            self.head = newNode
            self.tail = newNode
        # Case 2
        else:
            # while node.next is not None:
            #     node = node.next
            # node.next = newNode
            # newNode.prev = node
            # self.tail = newNode
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
    
    def sortedInsert(self, val) -> None:

        node = self.head
        newNode = Node(val)

        if not node:
            self.head = newNode
            self.tail = newNode
        elif node.val >= val:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            self.tail.prev = newNode
        else:
            while node.next is not None and node.next.val <= val:
                self.tail = node.next
                node = node.next #traverse
            
            newNode.next = node.next
            newNode.prev = node
            node.next = newNode
            tr = node
            while tr.next is not None:
                tr = tr.next
                self.tail = tr

            return node


    def remove(self, val) -> None:
        node = self.head

        if not node:
            print("there is nothing to remove")
            return
        else:
            i =0
            while node:
                if node.val != val:
                    before_node = node
                elif node.next is not None:
                    i += 1
                    before_node.next = node.next
                    node.next.prev = before_node
                else:
                    i += 1
                    before_node.next = node.next
                node = node.next
                self.tail = before_node

            if i == 0:
                print("Value does not exist")
                return
            else:
                return node


    def find(self, val) -> None:
        node = self.head
        lens = 0
        while node.next:
            node = node.next
            if node.val == val:
                lens += 1
                print("value exists")
        
        if lens == 0:
            print("value does not exist")
            
    
    def update(self, val, replaceTo) -> None:
        # first find the value:
        node = self.head
        ans = 0
        while node.next is not None: # traverse
            node = node.next
            if node.val == val:
                node.val = replaceTo
                ans += 1
        if ans == 0:
            print('value does not exist')
        return node

def cls():
    os.system("clear")


if __name__ == "__main__":
    cls()
    dll = DoublyLinkedList()
    dll.sortedInsert(4)
    dll.sortedInsert(10)
    dll.sortedInsert(21)
    dll.sortedInsert(14)
    dll.sortedInsert(13)
    # dll.sortedInsert(2)


    dll.print()