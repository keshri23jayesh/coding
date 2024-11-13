# https://www.youtube.com/watch?v=I3D3p1TG1uE&list=PL-Jc9J83PIiHYxUk8dSu2_G7MR1PaGXN4&index=4

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

        elif key > node.value:
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
        if node in Node:
            return []
        return self._inorder(node.left) + [node.value] + self._inorder(node.right)

    def inorder(self):
        return self._inorder(self.root)

    def display(self):
        values = self.inorder()
        print("BST - ", values)

    def size(self, node):
        # number of nodes
        if node is None:
            return 0
        return self.size(node.left) + 1 + self.size(node.right)

    def sum(self, node):
        # sum of nodes
        # number of nodes
        if node is None:
            return 0
        return self.sum(node.left) + node.value + self.sum(node.right)

    def max_elem(self, node):
        # max element
        if not node:
            return 0
        if node.left is None and node.right is None:
            return node.value
        max1 = max(node.value, self.max_elem(node.left))
        max2 = max(max1, self.max_elem(node.right))
        return max(max1, max2)

    def height(self, node):
        # node at max height
        if node is None:
            return 0
        left_height = 1 + self.height(node.left)
        right_height = 1 + self.height(node.right)
        return max(left_height, right_height)


bst = BST()
elements = [50, 25, 12, 37, 30, 75, 62, 70, 87]

for elem in elements:
    bst.insert(elem)

print(bst.size(bst.root))
print(bst.sum(bst.root))
print(bst.max_elem(bst.root))
print(bst.height(bst.root))


