# https://www.youtube.com/watch?v=p_8c3QYbDJ8&list=PL-Jc9J83PIiHYxUk8dSu2_G7MR1PaGXN4&index=16

class Node:

    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


class BST:

    def __init__(self):
        self.root = None
        self.value = []
        self.path = []
        self.found = False

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

    def node_to_root_path(self, node, key):
        if not node:
            return False
        if node.value == key:
            self.value.append(key)
            return True
        found = self.node_to_root_path(node.left, key)
        if found:
            self.value.append(node.value)
            return True
        found = self.node_to_root_path(node.right, key)
        if found:
            self.value.append(node.value)
            return True

    def nnode_to_root_path(self, elem, node):
        if not node:
            return False
        if node.value == elem:
            self.path.append(node)
            self.found = True
            return

        if not self.found:
            self.nnode_to_root_path(elem, node.left)
        if not self.found:
            self.nnode_to_root_path(elem, node.right)
        if self.found:
            self.path.append(node)

bst = BST()

elements = [50, 25, 12, 37, 75, 62, 87, 90]

for elem in elements:
    bst.insert(elem)

# print(bst.root)

# bst.node_to_root_path(bst.root, 62)
bst.nnode_to_root_path(62, bst.root)
print(bst.value)
print(bst.path)