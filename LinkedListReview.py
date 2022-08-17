# Linked List Review

# Singly Linked List
# Double Linked List

class Node:
    def __init__(self,val):
        self.next = None
        self.val = val


class singlyLinkedList():
    def __init__(self):
        self.root = None

    def insertAtEnd(self, value):
        
        # if the linked list is empty:

        if not self.root:
            self.root = Node(value)
            self.root.next = None
            return self.root

        node = self.root
        # traverse till end node is None
        while node.next is not None:
            node = node.next

        # when it reached the end
        node.next = Node(value)
        return node

    def insertAtBeginning(self, value):
        # as usual, check if the node is empty
        if not self.root:
            self.root = Node(value)
            return self.root
        # if not empty, replace the self root with the new node and connect node next to the previous self root.
        node = Node(value)
        node.next = self.root
        self.root = node
        return self.root

    def insertBeforePositionX(self,value,positionIdx):
        # check if the Linked List is empty
        if not self.root:
            print('list is empty. inserting at the beginning')
            self.root = Node(value)
            return self.root

        if positionIdx == 0:
            self.insertAtBeginning(value)
            return
        # if the list is not empty, then we iterate over the given index number reversely
        # Since it is before position X, if the position Idx is longer than the node length, then just add at the end
        node = self.root
        while positionIdx > 0 and node.next is not None:
            # traverse
            beforeNode = node
            node = node.next
            positionIdx -= 1
            

        # add it
        nodeAdd = Node(value)
        if node.next is not None:
            beforeNode.next = nodeAdd
            nodeAdd.next = node
        else:
            node.next = nodeAdd

        return node

    def sortedInsert(self, value):
        # check if the node is empty
        if not self.root:
            self.root = Node(value)
            return
        
        # if it is not empty, traverse it till the value is less than the value
        newNode = Node(value)
        node = self.root
        while node.next is not None and node.val < value:
            beforeNode = node
            node = node.next

        # if it needs to be added at the beginning, insert at beginning
        if self.root.val > value:
            self.insertAtBeginning(value)
            return

        # Check if we are at the end of the node
        if not node.next:
            if node.val < value:
                node.next = newNode
            else:
                beforeNode.next = newNode
                newNode.next = node
        else: # if we are in the middle of the node,
            beforeNode.next = newNode
            newNode.next = node

        return node


    def nodePrint(self):
        # if the list is empty
        nodes = []
        node = self.root
        if not self.root:
            print('node is empty')
            return None
        else:
            while node is not None:
                nodes.append(node.val)
                node = node.next

            nodes = map(str,nodes)
            print(" -> ".join(nodes))


if __name__ == "__main__":
    init = singlyLinkedList()
    init.sortedInsert(4)
    init.sortedInsert(9)
    init.sortedInsert(3)
    init.sortedInsert(20)
    init.sortedInsert(21)
    init.insertBeforePositionX(2000,300)
    init.sortedInsert(8)
    init.sortedInsert(-1)
    init.nodePrint()