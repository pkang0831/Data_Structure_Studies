import random
from collections import deque

# this script is for implementing binary tree with nodes

# # Binary Tree
#       tree
#       ----
#        j    <-- root
#      /   \
#     f      k
#   /   \      \
#  a     h      z    <-- leaves

# Why Trees?
# 1. One reason to use trees might be because you want to store information that naturally forms a hierarchy. For example, the file system on a computer:
# file system
# -----------
#      /    <-- root
#   /      \
# ...       home
#       /          \
#    ugrad        course
#     /       /      |     \
#   ...      cs101  cs112  cs113

class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
        self.parent = None


class Tree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, val) -> None:
        newNode = Node(val)
        if not self.root:
            self.root = newNode
        else:
            self._insert(val, self.root)

        
    def _insert(self, val, node):
        newNode = Node(val)

        if val < node.val:
            # traverse left
            if not node.left:
                node.left = newNode
            else:
                self._insert(val, node.left)

        else:
            # traverse right
            if not node.right:
                node.right = newNode
            else:
                self._insert(val, node.right)

        
    def preorder(self) -> list:
        # pre order traversal:
        # visit root, visit left, visit right
        if not self.root:
            return None
        else:
            mylist = self._preorder(self.root)
        
        return mylist

    def _preorder(self, node):
        mylist = []
        if node:
            mylist.append(node.val)
            
            mylist = mylist + self._preorder(node.left)
        
            mylist = mylist + self._preorder(node.right)

        else:
            return [None]

        return mylist

    def reversePreorder(self):
        if not self.root:
            return None
        else:
            mylist = self._reversePreorder(self.root)

        return mylist

    def _reversePreorder(self, node):

        mylist = []
        
        if node:

            mylist.append(node.val)

            mylist = mylist + self._reversePreorder(node.right)

            mylist = mylist + self._reversePreorder(node.left)

        else:
            return [None]

        return mylist


    def inorder(self) -> list:
        if not self.root:
            return None
        else:
            mylist = self._inorder(self.root)

        return mylist

    def _inorder(self, node):
        mylist = []
        if node:

            mylist = mylist + self._inorder(node.left)

            mylist.append(node.val)
        
            mylist = mylist + self._inorder(node.right)

        else:
            return [None]

        return mylist

    def postorder(self) -> list:
        if not self.root:
            return
        else:
            mylist = self._postorder(self.root)
        
        return mylist

    def _postorder(self, node):

        mylist = []

        if node:

            mylist = mylist + self._postorder(node.left)

            mylist = mylist + self._postorder(node.right)

            mylist.append(node.val)

        else:

            return [None]

        return mylist


    def binary_search(self, val) -> bool:
        # I think this is an automatic implementation of binary search.

        if not self.root:
            return False
        else:
            return self._binary_search(self.root, val)
        # if not self.root.left and not self.root.right:
        #     if self.root == val:
        #         return True
        #     else:
        #         return False

    def _binary_search(self, node, val):

        if node:
            if node.val == val:
                print(node.val)
                return True
            elif node.val < val:
                return self._binary_search(node.right, val)
            elif node.val > val:
                return self._binary_search(node.left, val)
        else:
            return False


    def dfs(self, val):
        if not self.root:
            return
        else:
            bool1 = self._dfs(self.root, val)

        return bool1  

    def _dfs(self, node, val):
        # visited = []

        # visited.append(node.val)

        if not node:
            return

        # if node.val in visited:
        #     return

        if node.val == val:
            return True

        if node:
            bool1 = False
            if node.left:
                bool1 = self._dfs(node.left, val)
            elif node.right:
                bool1 = self._dfs(node.right, val)

            return bool1
        else:
            return


    def height(self):
        '''
        returns height of the current tree
        '''
        
        if not self.root:
            return 0
        else:
            return self._height(self.root)

    def _height(self, node):

        if not node:
            return 0
            
        leftHeight = self._height(node.left)
        rightHeight = self._height(node.right)

        return max(leftHeight, rightHeight) + 1


    def rotateLeft(self):
        raise NotImplementedError

    def rotateRight(self):
        raise NotImplementedError


    def print_tree(self, val="val", left="left", right="right"):
        root = self.root
        def display(root, val=val, left=left, right=right):
            """Returns list of strings, width, height, and horizontal coordinate of the root."""
            # No child.
            if getattr(root, right) is None and getattr(root, left) is None:
                line = '%s' % getattr(root, val)
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            # Only left child.
            if getattr(root, right) is None:
                lines, n, p, x = display(getattr(root, left))
                s = '%s' % getattr(root, val)
                u = len(s)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
                second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

            # Only right child.
            if getattr(root, left) is None:
                lines, n, p, x = display(getattr(root, right))
                s = '%s' % getattr(root, val)
                u = len(s)
                first_line = s + x * '_' + (n - x) * ' '
                second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

            # Two children.
            left, n, p, x = display(getattr(root, left))
            right, m, q, y = display(getattr(root, right))
            s = '%s' % getattr(root, val)
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * \
                '_' + s + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + \
                (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + \
                [a + u * ' ' + b for a, b in zipped_lines]
            return lines, n + m + u, max(p, q) + 2, n + u // 2

        lines, *_ = display(root, val, left, right)
        for line in lines:
            print(line)


if __name__ == "__main__":
    init = Tree()

    for i in range(0,10):
        init.insert(random.randint(0,200))
        # init.insert(i)

    init.print_tree()
    lists = init.inorder()
    lists2 = init.preorder()
    lists3 = init.postorder()
    lists4 = init.reversePreorder()
    bool1 = init.binary_search(7)
    bool2 = init.dfs(30)
    heights = init.height()
    print(lists)
    print(lists2)
    print(lists3)
    print(lists4)
    print(bool1)
    print(bool2)
    print(heights)