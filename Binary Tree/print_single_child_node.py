
class Node:

    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None
        self.bst_max_height = 0

    def _insert(self, node, key):
        if node.value > key:
            if not node.left:
                node.left = Node(key)
                return
            self._insert(node.left, key)
        else:
            if not node.right:
                node.right = Node(key)
                return
            self._insert(node.left, key)

    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def print_single_child_node(self, parent, node):
        if parent:
            if ((parent.right == node and not parent.left) or
                    (parent.left == node and not parent.right)):
                print(node.value)
                return
        self.print_single_child_node(node, node.left)
        self.print_single_child_node(node, node.right)


nodes = [28, 29, 61, 75, 90, 63, 96, 78, 43, 64, 7, 52, 46, 84, 59, 22, 74, 55, 16, 58]

bst = BST()

for node in nodes:
    bst.insert(node)
print(bst.root)

BST().print_single_child_node(node)