
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

    def remove_leafs(self, parent, node):
        if parent:
            if not node.left and not node.right:
                if node == parent.left:
                    parent.left = None
                else:
                    parent.right = None
        self.remove_leafs(parent, node.left)
        self.remove_leafs(parent, node.right)

    def remove_leafs_approach2(self, node):
        if not node:
            return None

        if not node.left and not node.right:
            return None

        node.left = self.remove_leafs_approach2(node.left)
        node.right = self.remove_leafs_approach2(node.right)

        return node



nodes = [28, 29, 61, 75, 90, 63, 96, 78, 43, 64, 7, 52, 46, 84, 59, 22, 74, 55, 16, 58]

bst = BST()

for node in nodes:
    bst.insert(node)
print(bst.root)
