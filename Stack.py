# Stack and Queues
# Stack: LIFO - Last in, First out - pizza box stacker - last in, first out; 
# Queue: FIFO - First in , First out - line ups from the restuarants, line ups from the check out cashiers

import os


class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None

class Queue:
    # For Queue, it is First in, First out (fair line ups). to maintain this, we add node at the tail, remove at the head
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def enqueue(self, val):
        # to maintain first in and first out, we add the node at the tail.
        newNode = Node(val)
        # if the node is empty
        if self.isEmpty() is True:
            self.head = newNode
            self.tail = newNode
        else:
            # add the node to the tail
            self.tail.next = newNode
            # update the tail
            self.tail = newNode

    def peek(self):
        # this function prints out the first data on the line
        print(self.head.val)

    def dequeue(self):
        # remeber, it is first in first out, we remove the node at the head

        if self.isEmpty() is True:
            print("nothing to return")
            return
        else:
            self.head = self.head.next

    def print(self) -> None:
        
        # if self.print == 'front':
        node = self.head
        while node is not None:
            print(node.val, end = '')
            print(' -> ', end = '')
            node = node.next

class Stack:
    # For Stack, it is Last in, First out (think of pizza box) to maintain this, we add node at the tail, remove at the tail..? or head..?
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def isEmpty(self) -> None:
        return self.head == None

    def push(self, val) -> None:
        newNode = Node(val)
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            # going to put it at the head
            newNode.next = self.head
            self.head = newNode


    def pop(self) -> None:
        if self.isEmpty():
            print("stack is empty")
            return
        else:
            self.head = self.head.next

    def top(self) -> None: # (맨 뒤에 있는 벨류가 뭔지 가져오기)
        if self.isEmpty():
            print("stack is empty")
            return
        else:
            print(self.tail.val)

    def print(self) -> None:
        
        # if self.print == 'front':
        node = self.head
        while node is not None:
            print(node.val, end = '')
            print(' -> ', end = '')
            node = node.next


def cls():
    os.system("clear")

if __name__ == "__main__":
    cls()
    # que = Queue()
    # que.enqueue(4)
    # que.enqueue(5)
    # que.enqueue(6)
    # que.enqueue(7)
    # que.dequeue()
    # que.dequeue()
    # que.dequeue()
    # que.print()

    stk = Stack()
    stk.push(4)
    stk.push(5)
    stk.push(6)
    stk.push(7)
    stk.top()
    stk.print()


# stack and queue are objects that obfuscate some accessing methods, and usually allow better mechanisms to implement concurrency. If you need to get data by a specific order - stack and queue are the objects for you.

# Vector, at least in C is an implementation over arrays that allow you to increase and decrease the array size in run time without hurting the most important property of arrays - being sequential in memory.

# lists are not sequential in memory but very dynamic - adding and removing items cost less than in vector, at the price of access time (since their not sequential)

# to summarize:

# if you need to get the items one by one, in the order they were given - use queue.

# if you need to get the last item that was inserted first - use stack.

# if you know the number of elements your going to use in advance, and there order does not matter at all - use arrays.

# if the order does not matter , and the number of elements change in run time, while the adding/removing is not often, but querying the data is - use vector.

# if there are more inserts/deletes then querying - use lists. in lists you can also leverage orders cheaply with pointer changes - so this can be used to it too.