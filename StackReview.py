# stack: FIFO - Last in First Out. 
# Insert: insert the item O(1)
# Pop: pop the item O(1)
# Top: get the last item O(N), but you can make it as O(1) if you put it as tail
# isEmpty: check if the stack is empty, O(1)


from re import L


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        

class Stack:
    def __init__(self) -> None:
        self.head = None
    
    def isEmpty(self) -> bool:
        return self.head == None

    def pop(self) -> Node:
        # pop the last element that was added
        if self.isEmpty():
            return None
        
        if not self.head.next:
            node = self.head
            self.head = self.head.next
            return node

        rootNode = self.head
        
        self.head = self.head.next

        return Node(rootNode.val)

    def insert(self, val) -> Node:
        newNode = Node(val)
        if self.isEmpty():
            self.head = newNode
            return self.head

        newNode.next = self.head
        self.head = newNode

        return self.head

    def top(self) -> Node:

        if self.isEmpty():
            return 

        if not self.head.next:
            return self.head

        # start traversing
        rootNode = self.head

        while rootNode.next:
            beforeNode = rootNode
            rootNode = rootNode.next

        beforeNode.next = rootNode.next

        return rootNode

if __name__ == "__main__":
    init = Stack()
    for i in range(0,10):
        init.insert(i)
    for i in range(0,10):
        node = init.top()
        print(node.val)
        
    for i in range(0,10):
        init.insert(i)
    for i in range(0,10):
        node = init.pop()
        try:
            print(node.val)
        except:
            print("--")

    