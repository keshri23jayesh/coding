# https://www.youtube.com/watch?v=KvcfuGcdDMg&list=PL-Jc9J83PIiHYxUk8dSu2_G7MR1PaGXN4&index=22

class Node:

    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None

    def _insert(self, root, key):
        if key < root.value:
            if not root.left:
                root.left = Node(key)
                return
            self._insert(root.left, key)
        else:
            if not root.right:
                root.right = Node(key)
                return
            self._insert(root.right, key)

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _print_level(self, node, current_level, level):
        if not node or current_level > level:
            return
        if level == current_level:
            print(node.value)
            return
        self._print_level(node.left, current_level+1, level)
        self._print_level(node.right, current_level+1, level)

    def print_level(self, level):
        self._print_level(self.root, 1, level)


bst = BST()

elements = [50, 25, 12, 37, 75, 62, 87, 90]

for elem in elements:
    bst.insert(elem)

# print(bst.root)
bst.print_level(4)
