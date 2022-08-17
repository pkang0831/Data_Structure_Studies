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
        # check if the tree is empty
        newNode = Node(val)
        if not self.root:
            self.root = newNode
        else:
            self._insert(val, self.root)

        # if the tree is not empty, there are some rules.
        # if the value is less than the parent node value, it goes to left
        # if the value is more than the parent node value, it goes to right
        # new node needs to be entered in a empty space. so children needs to be checked.

    def _insert(self, value, node):
        newNode = Node(value)
        if value < node.val:  # check LEFT

            if node.left is None:  # check if LEFT is empty

                node.left = newNode
                newNode.parent = node

            else:  # if it is not empty

                self._insert(value, node.left)

        else:  # check RIGHT

            if node.right is None:

                node.right = newNode
                newNode.parent = node

            else:

                self._insert(value, node.right)

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
        init.insert(i)

    init.print_tree()
