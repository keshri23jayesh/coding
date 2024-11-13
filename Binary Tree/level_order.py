class Node:

    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


class BST:

    def __init__(self):
        self.root = None

    def _insert(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _inorder(self, node):
        if node is None:
            return []
        return self._inorder(node.left) + [node.value] + self._inorder(node.right)

    def inorder(self):
        return self._inorder(self.root)

    def pre(self, node):
        if node is None:
            return []
        return [node.value] + self.pre(node.left) + self.pre(node.right)

    def post(self, node):
        if node is None:
            return []
        return self.post(node.left) + self.post(node.right) + [node.value]

    def level_order(self):
        levels = [self.root]
        while len(levels):
            count = len(levels)
            elem = ""
            for i in range(0, count):
                node = levels.pop(0)
                elem += str(node.value) + " "
                if node.left:
                    levels.append(node.left)
                if node.right:
                    levels.append(node.right)
            print(elem)

    def print(self):
        value = self.inorder()
        print("BST", value)


bst = BST()

elements = [50, 25, 12, 37, 62, 87]

for elem in elements:
    bst.insert(elem)

bst.level_order()