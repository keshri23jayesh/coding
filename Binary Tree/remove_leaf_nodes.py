# https://www.youtube.com/watch?v=x_0KUwgdm1c&list=PL-Jc9J83PIiHYxUk8dSu2_G7MR1PaGXN4&index=42

class Node:

    def __init__(self, key):
        self.value = key
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None
        self.path = []
        self.found = False

    def _insert(self, root, key):
        if key <= root.value:
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

    def level_order(self, node):
        if not node:
            return
        level = [node]
        while len(level):
            count = len(level)
            current_level = ""
            for i in range(0, count):
                elem = level.pop(0)
                current_level += str(elem.value) + " "
                if elem.left:
                    level.append(elem.left)
                if elem.right:
                    level.append(elem.right)
            print(current_level)

    def remove_leaf(self, node):
        if not node:
            return
        if not node.left and not node.right:
            return
        node.left = self.remove_leaf(node.left)
        node.right = self.remove_leaf(node.right)
        return node


nodes = [50, 25, 12, 37, 75, 62, 87, 90]

bst = BST()

for node in nodes:
    bst.insert(node)
print(bst.root)

bst.level_order(bst.root)
bst.remove_leaf(bst.root)
print("-----------")
bst.level_order(bst.root)
