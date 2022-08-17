import os
import random

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class LinkedList:

    def __init__(self) -> None:
        self.root = None

    def insert_at_end(self,val) -> "LinkedList":
        node = self.root

        if not node: # if the list is empty
            newNode = Node(val)
            self.root = newNode
            return
        else:
            while node.next is not None:
                node = node.next
            
        newNode = Node(val)
        node.next = newNode
        return node

    def insert_at_front(self, val) -> "LinkedList":
        node = self.root
        newNode = Node(val)

        if not node:
            self.root = newNode
            return
        else:
            self.root = newNode
            newNode.next = node
            return node

    def insert_before_node(self, val, node_val) -> "LinkedList":
        node = self.root
        # newNode = Node(val)

        if not node:
            self.root = newNode
            return
        else:
            while node.next is not None:

                if node.next.val == node_val:
                    newNode = Node(val)
                    newNode.next = node.next
                    node.next = newNode
                    node = node.next.next
                else:
                    node = node.next
            return node

    def sorted_insert(self,val) -> "LinkedList":
        node = self.root

        if not node:
            self.root = Node(val)
            return
        elif node.val >= val:
            newNode = Node(val)
            newNode.next = node
            self.root = newNode
            
        else:
            # TODO: Understand this while loop conditions
            while node.next is not None and node.next.val <= val:
                node = node.next
            newNode = Node(val)
            newNode.next = node.next
            node.next = newNode
            return node

    def search(self, val) -> "Node":
        node = self.root
        pos = 0
        while node.next is not None:
            pos += 1
            if node.next.val == val:
                print(f"the node is in {pos}th position")
            node = node.next
        return
    def searchNthPosition(self, nth_pos) -> "Node":
        node = self.root
        while node.next is not None and nth_pos > 0 :
            node = node.next
            nth_pos -= 1

        if nth_pos != 0:
            print("index out of range")
        else:
            print(node.val)


    def print(self) -> None:
        node = self.root
        nodearr = []
        if not node:
            print("node is empty")
            return
        else:
            while node is not None:
                nodearr.append(node.val)
                node = node.next

        nodearr = list(map(str,nodearr))
        print(" -> ".join(nodearr))

    def delete(self) -> "LinkedList":
        pass # YOUR CODE HERE
    def replace(self) -> "LinkedList":
        pass # YOUR CODE HERE

def cls():
    os.system("clear")

if __name__ == "__main__":
    cls()
    ll = LinkedList()
    # ll.insert_at_front("root_node")
    listToBeInserted = [random.randint(0,3000) for i in range(0,20)]
    # listToBeInserted = [1,2,3,4,5,5,6,5,67,7,9]
    for i in listToBeInserted:
        ll.sorted_insert(i)
    # ll.insert_before_node(333,5)
    ll.search(listToBeInserted[2])

    ll.print()